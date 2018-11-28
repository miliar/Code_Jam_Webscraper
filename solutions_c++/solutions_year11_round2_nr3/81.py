#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
#define N 8
int b[N], e[N], c[N], u[N], w[N][N];
vector <int> v[N], r[N];
int next(int i, int j)
{
	int k;
	for(k=0; k<v[i].size() && v[i][k]!=j; k++);
	if(k==v[i].size()-1) return v[i][0];
	else return v[i][k+1];
}
int main()
{
	int i, j, n, m, k, l, h, p, t, ts, bk, bm;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d", &n, &k), i=0; i<k; scanf("%d", &b[i]), b[i]--, i++);
		for(i=0; i<k; scanf("%d", &e[i]), e[i]--, i++);
		for(i=0; i<n; v[i].clear(), r[i].clear(), i++);
		for(i=0; i<n; v[i].push_back((i+1)%n), v[i].push_back((i+n-1)%n), i++);
		for(i=0; i<k; v[b[i]].push_back(e[i]), v[e[i]].push_back(b[i]), i++);
		for(i=0; i<n; sort(v[i].begin(), v[i].end()), i++);
		for(i=0; i<n; i++)
			for(j=0; j<n; w[i][j]=0, j++);
		for(h=0, i=0; i<n; i++)
			for(j=0; j<v[i].size(); j++)
			{
				k=v[i][j];
				if(w[i][k]) continue;
				for(l=i; k!=i; r[h].push_back(k), w[l][k]=1, p=l, l=k, k=next(k, p));
				r[h].push_back(k);
				w[l][k]=1;
				h++;
			}
		for(m=1, i=0; i<n; m*=n, i++);
		for(bk=0, bm=0, m--; m>=0; m--)
		{
			for(i=0; i<n; u[i]=0, i++);
			for(j=m, i=0; i<n; c[i]=j%n, j/=n, u[c[i]]=1, i++);
			for(i=0; i<n && u[i]; i++);
			k=i;
			for(; i<n && !u[i]; i++);
			if(i<n) continue;
			for(i=0; i<h; i++)
			{
				for(j=0; j<k; u[j]=0, j++);
				for(j=0; j<r[i].size(); u[c[r[i][j]]]=1, j++);
				for(j=0; j<k && u[j]; j++);
				if(j<k) break;
			}
			if(i<h) continue;
			if(k>bk) { bk=k; bm=m; }
		}
		for(printf("Case #%d: %d\n", t+1, bk), i=0; i<n-1; printf("%d ", bm%n+1), bm/=n, i++);
		printf("%d\n", bm+1);
	}
	return 0;
}