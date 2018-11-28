#include <stdio.h>
#include <math.h>
#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
int x[3], y[3], r[3];
double sub(int i, int j, int k)
{return max(r[i],(sqrt(0.0+(x[j]-x[k])*(x[j]-x[k])+(y[j]-y[k])*(y[j]-y[k]))+r[j]+r[k])/2);}
int n;
double R;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	int i;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%d",&n);
		for (i = 0; i < n; i++)
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		if (n == 1) R = r[0];
		if (n == 2) R = max(r[0],r[1]);
		if (n == 3) {
			R = min(sub(0,1,2),sub(1,2,0));
			R = min(R,sub(2,0,1));
		}
		printf("%lf\n",R);
	}
	return 0;
}
/*
#include <stdio.h>
#include <algorithm>
#define MK 25
#define MN 100
using namespace std;
struct Array {
	int v[MK];
}d[MN];
int n, K, r;
bool cmp(Array &a, Array &b)
{
	for (int i = 0; i < K; i++) {
		if (a.v[i] != b.v[i]) return a.v[i] < b.v[i];
	}
	return 0;
}
bool ch[MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	int i, j, k, p;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&K);
		for (i = 0; i < n; i++) {
			for (j = 0; j < K; j++)
				scanf("%d",&d[i].v[j]);
		}
		sort(d,d+n,cmp);
		memset(ch,0,sizeof(ch));
		r = 0;
		for (i = 0; i < n; i++) {
			if (ch[i]) continue;
			++r; ch[i] = 1; p = i;
			for (j = i+1; j < n; j++) {
				if (ch[j]) continue;
				for (k = 0; k < K; k++) {
					if (d[p].v[k] >= d[j].v[k]) break;
				}
				if (k == K) {ch[j] = 1; p = j;}
			}
		}
		printf("%d\n",r);
	}
	return 0;
}
*/