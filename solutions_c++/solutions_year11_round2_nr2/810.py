#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
struct group
{
	double right;
	double left;
	double distLeft;
	double distRight;
	group(double _left = 0, double _right = 0, double _distLeft = 0, double _distRight = 0)
	{
		right = _right;
		left = _left;
		distLeft = _distLeft;
		distRight = _distRight;
	}
};
pair<int, int> I[1000146];
void solve()
{
	int N;
	int D;
	scanf ("%d%d", &N, &D);
	vector<group> S;
	for (int i = 0; i < N; ++i)
	{
		int pos, cnt;
		scanf ("%d%d", &pos, &cnt);
		I[i] = make_pair(pos, cnt);
	}
	sort(I, I + N);
	for (int i = 0; i < N; ++i)
	{
		int pos, cnt;
		pos = I[i].first;
		cnt = I[i].second;
		double dLeft = (cnt - 1) * D / 2.;
		double dRight = dLeft;
		double left = pos - dLeft;
		double right = pos + dRight;
		while (S.size() != 0 && S[S.size() - 1].right + D > left)
		{
			int last = S.size() - 1;
			double mov = S[last].right + D - left;
			if (S[last].distLeft + mov < dRight)
			{
				left = S[last].left - mov;
				dLeft = max(S[last].distLeft + mov, dLeft);
				dRight = max(S[last].distRight - mov, dRight);
			}
			else
			{
				if (S[last].distLeft > dRight + mov)
				{
					right += mov;
					left = S[last].left;
					dLeft = max(S[last].distLeft, dLeft - mov);
					dRight = max(S[last].distRight, dRight + mov);
				}
				else
				{
					mov = (S[last].right + D - left + S[last].distLeft + dRight) / 2;
					double movLeft = mov - S[last].distLeft;
					double movRight = mov - dRight;
					left = S[last].left - movLeft;
					right += movRight;
					dLeft = max(S[last].distLeft + movLeft, dLeft);
					dRight = max(S[last].distRight, dRight + movRight);
				}
			}			
			S.pop_back();
		}
		S.push_back(group(left, right, dLeft, dRight));
	}
	double ans = 0;
	for (int i = 0; i < S.size(); ++i)
	{
		if (S[i].distLeft > ans)		
		{
			ans = S[i].distLeft;
		}
		if (S[i].distRight > ans)		
		{
			ans = S[i].distRight;
		}
	}
	printf ("%.10lf\n", ans);
}
int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}