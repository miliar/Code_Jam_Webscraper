#include <iostream>
#include <vector>

using namespace std;

#define ABS(x) ((x)  >= 0 ? (x) : ((-1)*(x)))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
class score
{
public:
	int a, b ,c;

	score() { a = b = c = 0; }
	bool next_score()
	{
		if(c < 10) c++;
		else
		{
			c = 0;
			if(b < 10) b++;
			else 
			{
				b = 0;
				if(a < 10) a++;
				else return false;
			}
		}
		return true;
	}

	bool is_surprising() const
	{
		return ABS(a-b) >=2 || ABS(b-c) >=2 || ABS(c-a) >= 2;
	}

	bool is_valid() const
	{
		return ABS(a-b) <=2 && ABS(b-c) <=2 && ABS(c-a) <= 2;		
	}

	int total() const { return a + b + c; }
	int best() const { return MAX(MAX(a,b),c); }
};

int g_ans = 0;
int process(int N, int S, int p, const vector<int> &totals, int empi, vector<score> scores)
{
	score sc;

	do
	{
		if(sc.is_valid() && sc.total() == totals[empi] && (!sc.is_surprising() || S > 0))
		{
			if(N - 1 > 0)
			{
				vector<score> tsc = scores;
				tsc.push_back(sc);;
				process(N-1, (sc.is_surprising() ? S-1 : S), p, totals, empi + 1, tsc);
			}
			else
			{
				int maxp = 0;
				for(int i = 0; i < scores.size(); i++)
					if(scores[i].best() >= p) maxp++;
				if(sc.best() >= p) maxp++;
				if(maxp > g_ans) g_ans = maxp;
			}
		}
	} while(sc.next_score());
	return g_ans;
}

int main()
{
	int cases;
	cin  >> cases;

	for(int i = 0; i < cases; i++)
	{
		int N, S, p;
		vector<int> totals;
		vector<score> scores;
		cin >> N;
		cin >> S;
		cin >> p;
		for(int j = 0; j < N; j++)
		{
			int t;
			cin >> t;
			totals.push_back(t);
		}
		g_ans = 0;
		cout << "Case #" << (i+1) << ":  " << process(N, S, p, totals, 0, scores) << endl;
	}
}