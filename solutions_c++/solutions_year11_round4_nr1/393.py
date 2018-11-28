#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<double,double> PII;

#define maxn (10000)
#define PB push_back
#define MP make_pair
#define A first
#define B second

double f[maxn];
int m,r,v;
double t;
int n;

const int bound=100;

int main(){
	int T; scanf("%d",&T);

	for (int tt=1;tt<=T;tt++) {
		printf("Case #%d: ",tt);

		scanf("%d%d%d%lf%d",&m,&v,&r,&t,&n);

		int last=0; memset(f,0,sizeof(f));
		for (int i=1;i<=n;i++) {
			int st,ed,V; scanf("%d%d%d",&st,&ed,&V);

			if (last<st) f[0]+=(double) (st-last);
			f[V]+=(double) (ed-st);

			last=ed;
		}

		if (last<m) f[0]+=(double) (m-last);

		//for (int i=0;i<=bound;i++) if (f[i]>1e-13) printf("%lf\n",f[i]);

		double ans=0.;
		for (int i=0;i<=bound;i++) if (f[i]>1e-13) {
			double R=((double) i+r),V=((double) i+v);
			//printf("%lf %lf\n",R,V);

			if (t>1e-13) {
				if (R*t<f[i]) ans+=t,f[i]-=R*t,t=0.;
				else t-=f[i]/R,ans+=f[i]/R,f[i]=0.;
			}

			ans+=f[i]/V;
		}

		printf("%.10lf\n",ans);
	}

	return 0;
}
