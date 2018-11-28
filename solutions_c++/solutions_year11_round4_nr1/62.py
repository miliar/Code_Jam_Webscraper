#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<utility>

using namespace std;

const int maxn = 3000;

multiset<pair<double,double> > T;
int X, S, R, N;
double t;
pair<pair<int,int>,int> p[maxn];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int ntest;
	scanf("%d", &ntest);
	for(int test=1; test<=ntest; test++)
	{
		scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
		R -= S;
		for(int i=0; i<N; i++)
		{
			scanf("%d%d%d", &p[i].first.first, &p[i].first.second, &p[i].second);
		}
		sort(p, p+N);

		T.clear();
		int st = 0;
		for(int i=0; i<N; i++)
		{
			T.insert(make_pair(S, p[i].first.first - st));
			T.insert(make_pair(S + p[i].second, p[i].first.second - p[i].first.first));
			st = p[i].first.second;
		}

		T.insert(make_pair(S, X - st));

		double ans = 0;

		while(!T.empty())
		{
			double L = T.begin()->second;
			double V = T.begin()->first;
			double TIME = L / (V + R);
			if(TIME < t)
			{
				t -= TIME;
				ans += TIME;
			}
			else
			{
				TIME = t + (L - (V+R) * t) / V;
				ans += TIME;
				t = 0;
			}
			T.erase(T.begin());
		}
		printf("Case #%d: %.10lf\n", test, ans);
	}
	return 0;
}
