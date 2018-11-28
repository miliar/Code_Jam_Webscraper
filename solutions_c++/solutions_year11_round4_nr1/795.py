#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <sstream>

using namespace std;

#define EPS 1e-10
#define EQ(a,b) (abs((a)-(b))<EPS)

int main(void)
{
	int T;
	scanf("%d", &T);

	for(int caseN=1;caseN<=T;caseN++)
	{
		double t, X, S, R;
		int N;
		scanf("%lf %lf %lf %lf %d", &X, &S, &R, &t, &N);
		pair<double, double> walk[1001];

		int totlen=0;

		for(int i=0;i<N;i++)
		{
			double s, e, speed;
			scanf("%lf %lf %lf", &s, &e, &speed);
			walk[i]=make_pair(speed, e-s);
			totlen+=(e-s);
		}

		double leftlen=X-totlen;
		walk[N]=make_pair(0, leftlen);

		sort(walk, walk+N+1);
		double ans=0;

		for(int i=0;i<=N;i++)
		{
			if(t>0)
			{
				double runTime=walk[i].second/((double)(walk[i].first+R));
				if(runTime<=t)
				{
					t-=runTime;
					ans+=runTime;
				}
				else
				{
					double _leftlen=walk[i].second-(walk[i].first+R)*t;
					ans+=t+_leftlen/(walk[i].first+S);
					t=0;					
				}
			}
			else ans+=walk[i].second/(double)(walk[i].first+S);
		}

		printf("Case #%d: %.10lf\n", caseN, ans);
	}
	return 0;
}
