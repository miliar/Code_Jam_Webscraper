#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 1010
int N;
double X, S, R, T;
struct way{
	double b, e, w;
};
way n[MAXN];
double d[MAXN];

int CMP(const void *a, const void *b){
	way x = *(way*)a;
	way y = *(way*)b;
	if(x.b > y.b) return 1;
	return -1;
}

int main()
{
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		memset(n, 0, sizeof(n));
		memset(d, 0, sizeof(d));
		scanf("%lf%lf%lf%lf%d", &X, &S, &R, &T, &N);
		for(int i = 0;i < N; i++){
			scanf("%lf%lf%lf", &n[i].b, &n[i].e, &n[i].w);
		}


		qsort(n, N, sizeof(way), CMP);
		double walkdis = 0;
		double now = 0;
		for(int i = 0;i < N; i++){

			walkdis += n[i].b - now;
			//cout<<walkdis<<" "<<(int)n[i].w<<endl;
			now = n[i].e;
			d[(int)n[i].w] += n[i].e - n[i].b;
		}
		walkdis += X - now;
		//cout<<walkdis<<endl;
		//cout<<walkdis<<endl;
		d[0] += walkdis;

		double ans = 0;
		double rleft = T;
		for(int i = 0;i < MAXN; i++){
			if(d[i] == 0)continue;
			double rspeed = ((double)i + R);
			double wspeed = ((double)i + S);
			//cout<<"==="<<i<<" "<<S<<" "<<R<<" "<<d[i]<<endl;
			if(rleft * rspeed >= d[i]){
				ans += d[i] / rspeed;
				rleft = rleft - d[i] / rspeed;
				//cout<<"1 "<<ans<<" "<<rleft<<endl;

			}
			else{
				d[i] = d[i] - rleft * rspeed;
				ans += rleft + d[i] / wspeed;
				//cout<<"2 "<<ans<<" "<<rleft<<" "<<d[i] / wspeed<<endl;
				rleft = 0;

			}
		}


		printf("Case #%d: %.8lf\n", casenum++, ans);

	}
	return 0;
}

