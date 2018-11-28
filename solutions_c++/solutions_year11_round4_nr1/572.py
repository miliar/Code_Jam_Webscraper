#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;


struct Way
{
	double l, w;
};

bool operator<(const Way& w1, const Way& w2)
{
	return w1.w < w2.w;
}

void solve_case(int caseNumber)
{
	double X, S, R, t;
	double N;

	cin >> X >> S >> R >> t >> N;

	R -= S;

	vector<Way> ways;

	for(int i=0; i<N; i++)
	{
		Way w;
		double b, e;
		cin >> b >> e >> w.w;

		w.l = e - b;
		w.w += S;

		ways.push_back(w);

		X -= w.l;
	}

	Way w;
	w.l = X;
	w.w = S;

	ways.push_back(w);

	sort(ways.begin(), ways.end());

	double timeTotal = 0.0;

	for(int i=0; i<ways.size(); i++)
	{
		Way w = ways[i];
		if (w.l / double(w.w + R) <= t)
		{
			timeTotal += w.l / double(w.w + R);
			t -= w.l / double(w.w + R);
		}
		else
		{
			double dist = double(w.w + R) * t;

			timeTotal += t + double(w.l - dist) / double(w.w);
			t = 0.0;
		}
	}

	printf("Case #%d: %lf\n", caseNumber, timeTotal);
	//cout << "Case #" << caseNumber << ": " << timeTotal << endl;
}

int main()
{
	int T;

	cin >> T;

	for(int i = 0; i < T; i++)
		solve_case(i + 1);

	return 0;
}