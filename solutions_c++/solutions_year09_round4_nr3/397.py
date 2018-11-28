#include <stdio.h>
#include <algorithm>
#include <vector>
#define MN 16
#define MK 25
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
int c[MN][MN];
vector<int> path[MN];
void back(int p, int v)
{
	if (v >= r) return;
	if (p == n) {
		r = v;
		return;
	}
	int i, j;

	for (i = 0; i < v; i++) {
		for (j = 0; j < path[i].size(); j++) {
			if (!c[path[i][j]][p]) break;
		}
		if (j == path[i].size()) {
			path[i].push_back(p);
			back(p+1,v);
			path[i].pop_back();
		}
	}
	path[v].clear();
	path[v].push_back(p);
	back(p+1,v+1);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T;
	int i, j, k;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		scanf("%d%d",&n,&K);
		for (i = 0; i < n; i++) {
			for (j = 0; j < K; j++)
				scanf("%d",&d[i].v[j]);
		}
		sort(d,d+n,cmp);
		for (i = 0; i < n; i++) {
			for (j = i+1; j < n; j++) {
				for (k = 0; k < K; k++) {
					if (d[j].v[k] <= d[i].v[k]) break;
				}
				c[i][j] = k == K;
			}
		}
		r = n;
		path[0].clear(); path[0].push_back(0);
		back(1,1);
		printf("%d\n", r);
	}
	return 0;
}
/*#include <stdio.h>
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
}*/