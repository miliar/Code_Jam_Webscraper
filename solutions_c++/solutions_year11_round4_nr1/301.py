#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)
#define MAXN 1005
#define EPS 1e-8

struct Walkway {
	int B, E;
	double w;
	double L;
} walk[MAXN];

double X,S,R;
int N;
double t;

bool comp(Walkway &a, Walkway &b) {
	return a.w < b.w;
}


int main() {
	int T,kase=1;
	int i;
	double L1,L2,tm;
	scanf(" %d",&T);
	while(T--) {
		printf("Case #%d: ",kase++);
		scanf(" %lf %lf %lf %lf %d",&X, &S, &R, &t, &N);
		L2 = 0;
		rep(i,N) {
			scanf(" %d %d %lf",&walk[i].B, &walk[i].E, &walk[i].w);
			walk[i].L = walk[i].E - walk[i].B;
			L2 += (walk[i].E - walk[i].B);
		}
		sort(walk, walk+N, comp);
		L1 = X - L2;
		tm = 0;
		
		if(R * t >= L1) {
			t -= (L1/(double)R);
			tm += (L1/(double)R);
		}
		else {
			tm += t;
			L1 -= (t * R);
			tm += (L1 / (double)S);
			t = 0;
		}

		rep(i,N) {
			if(t > 0) {
				if(t * (R + walk[i].w) >= walk[i].L) {
					t -= walk[i].L / (double)(R + walk[i].w);
					tm += walk[i].L / (double)(R + walk[i].w);
				}
				else {
					tm += t;
					walk[i].L -= (t * (R + walk[i].w) );
					t = 0;
					tm += (walk[i].L / (double)(S+walk[i].w));
				}
			}
			else {
				tm += (walk[i].L / (double)(S + walk[i].w));
			}
		}

	


		printf("%.12lf\n",tm);
	}
	return 0;
}