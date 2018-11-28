#include <stdio.h>
#include <algorithm>
#define MN 1001
using namespace std;
struct DATA {
	int L, w, x;
};
bool cmp(DATA a, DATA b)
{return a.x < b.x;}
int n, X, S, R;
DATA d[MN];
double r, t;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt, T, i, j, k;

	scanf("%d",&T);
	for (tt = 1; tt <= T; tt++) {
		printf("Case #%d: ",tt);
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&n);
		d[n].L = X; d[n].w = 0;
		for (i = 0; i < n; i++) {
			scanf("%d%d%d",&j,&k,&d[i].w);
			d[i].L = k-j;
			d[n].L -= d[i].L;
		}
		n++;
		for (i = 0; i < n; i++)
			d[i].x = (d[i].w+S)*(d[i].w+R);
		sort(d,d+n,cmp);
		r = 0;
		for (i = 0; i < n; i++) {
			if (d[i].L / (d[i].w+R+0.0) <= t) {
				t -= d[i].L / (d[i].w+R+0.0);
				r += d[i].L / (d[i].w+R+0.0);
			}
			else {
				r += t;
				r += (d[i].L - (d[i].w+R) * t)/(d[i].w+S);
				t = 0;
			}
		}
		printf("%.10lf\n",r);
	}
	return 0;
}