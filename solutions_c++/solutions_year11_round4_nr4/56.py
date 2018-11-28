#include <stdio.h>
#include <memory.h>
#include <algorithm>
#define MN 400
#define ll long long
using namespace std;
int n;
int d[MN][MN];
pair<int,int> c[MN][MN]; int _c[MN][MN];
int f(int p, int q, int i)
{
	int r, j;

	r = 0;
	for (j = 0; j < n; j++) {
		if (d[0][j] == d[0][q]) {
			if (d[p][j] == 1 || d[q][j] == 1 || d[i][j] == 1) r++;
		}
	}
	return r-1;
}
pair<int,int> C(int p, int q)
{
	if (_c[p][q]) return c[p][q];
	_c[p][q] = 1; c[p][q] = make_pair(n+1,0);
	int i;
	pair<int,int> re;
	if (d[0][q] == d[0][1]) {
		if (q == 1) {
			c[p][q] = make_pair(0,0);
			for (i = 0; i < n; i++) {
				if (d[0][i] == d[0][q] && d[p][i] == 1)
					c[p][q].second++;
			}
			return c[p][q];
		}
		else return c[p][q];
	}

	for (i = 0; i < n; i++) {
		if (i != p && i != q && d[0][i] == d[0][q]+1 && d[i][q] == 1) {
			if (i == 1) {
				re = C(q,i);
				re.first++; re.second += f(p,q,q);
			}
			else {
				re = C(q,i);
				re.first++; re.second += f(p,q,i);
			}
			if (c[p][q].first > re.first || c[p][q].first == re.first && c[p][q].second < re.second)
				c[p][q] = re;
		}
	}
	return c[p][q];
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tt, T, m, i, j, k;
	pair<int,int> r, re;

	scanf("%d",&T);
	for (tt = 1; tt <= T; tt++) {
		printf("Case #%d: ",tt);
		scanf("%d%d",&n,&m);
		memset(d,0,sizeof(d));
		while (m--) {
			scanf("%d,%d",&i,&j);
			d[i][j] = d[j][i] = 1;
		}
		for (k = 0; k < n; k++) {
			for (i = 0; i < n; i++) {
				for (j = 0; j < n; j++) {
					if (d[i][k] && d[k][j]) {
						if (d[i][j] == 0 || d[i][j] > d[i][k]+d[k][j])
							d[i][j] = d[i][k]+d[k][j];
					}
				}
			}
		}
		for (i = 0; i < n; i++) d[i][i] = 0;
		if (d[0][1] == 1) {
			k = 0;
			for (i = 1; i < n; i++) {
				if (d[0][i] == 1) k++;
			}
			printf("0 %d\n",k);
		}
		else {
			memset(_c,0,sizeof(_c));
			r = make_pair(n+1,0);
			for (i = 1; i < n; i++) {
				if (d[0][i] == 1) {
					re = C(0,i);
					if (r.first > re.first || r.first == re.first && r.second < re.second)
						r = re;
				}
			}
			printf("%d %d\n",r.first,r.second);
		}
	}
	return 0;
}