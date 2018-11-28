#include	<cstdio>
#include	<iostream>
#include	<algorithm>
using namespace std;
struct tim{
	int		dep, arr;
}a[100], b[100];
int		f[1500], g[1500];
bool cmp(tim x, tim y)
{
	return x.dep<y.dep;
}
int main()
{
	int		n, t, na, nb, i, j, h, m, tota, totb, k;
	char	c;
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &n);
	for (i=1; i<=n; ++i) {
		scanf("%d", &t);
		scanf("%d%d", &na, &nb);
		memset(f, 0, sizeof(f));
		memset(g, 0, sizeof(g));
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		tota=0; totb=0;
		for (j=0; j<na; ++j) {
			scanf("%d%c%d", &h, &c, &m);
			a[j].dep=h*60+m;
			scanf("%d%c%d", &h, &c, &m);
			a[j].arr=h*60+m;
		}
		for (j=0; j<nb; ++j) {
			scanf("%d%c%d", &h, &c, &m);
			b[j].dep=h*60+m;
			scanf("%d%c%d", &h, &c, &m);
			b[j].arr=h*60+m;
		}
		int la=0, lb=0;
		sort(a, a+na, cmp);
		sort(b, b+nb, cmp);
		for (j=0; j<1440; ++j) {
			if (j>0) { f[j]+=f[j-1]; g[j]+=g[j-1]; }
			for (k=la; k<na; ++k) 
				if (a[k].dep==j) {
					if (!f[j]) tota++;
					else f[j]--;
					g[a[k].arr+t]++;
				} else break;
			la=k;
			for (k=lb; k<nb; ++k)
				if (b[k].dep==j) {
					if (!g[j]) totb++;
					else g[j]--;
					f[b[k].arr+t]++;
				} else break;
			lb=k;
		}
		printf("Case #%d: %d %d\n", i, tota, totb);
	}
}
