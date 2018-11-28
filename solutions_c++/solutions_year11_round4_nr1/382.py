// twitter.com/P_E

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>
using namespace std;

const double eps = 1e-9;

void solve(int acase)
{
	int X, S, R, t, N;
	scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);

	vector< pair<int, int> > wws;
	for (int i = 0; i < N; ++i)
	{
		int B, E, w;
		scanf("%d %d %d", &B, &E, &w);
		X -= E - B;
		wws.push_back(make_pair(w, E - B));
	}
	assert(X >= 0);
	wws.push_back(make_pair(0, X));
	sort(wws.begin(), wws.end());
	
	double totalTime = 0;
	double tleft = t;
	for (int p = 0; p < (int)wws.size(); ++p)
	{
		int w = wws[p].first;
		int L = wws[p].second;
		if (tleft > 0)
		{
			double tReq = (double)L / (R + w);
			if (tReq < tleft)
			{
				tleft -= tReq;
				totalTime += tReq;
			}
			else
			{
				totalTime += tleft;	
				double Dleft = L - (R + w) * tleft;
				totalTime += Dleft / (S + w);
				tleft = 0;
			}
		}
		else
			totalTime += (double)L / (S + w);
	}

	printf("Case #%d: %.9lf\n", acase, totalTime);
}

int main()
{
	freopen("al.in", "r", stdin);
	freopen("al.out", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for (int tc = 0; tc < cases; ++tc) 
		solve(tc + 1);

	return 0;
}
