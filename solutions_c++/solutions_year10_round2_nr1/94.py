#include <stdio.h>
#include <string>
#include <map>
#define ML 128
#define MX 10000
using namespace std;
string d;
int cnt;
map<string,int> c[MX];
void f(int p, int read)
{
	if (read == d.size()) return;
	int i, j;

	for (i = read+1; i < d.size(); i++) {
		if (d[i] == '/') break;
	}
	j = c[p][d.substr(read+1,i-read-1)];
	if (j == 0) {
		c[p][d.substr(read+1,i-read-1)] = cnt;
		c[cnt].clear();
		f(cnt++,i);
	}
	else f(j,i);
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, n, m, r, i;
	char str[ML];

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&m);
		cnt = 0; c[cnt++].clear();
		for (i = 0; i < n; i++) {
			scanf("%s",str); d = str;
			f(0,0);
		}
		r = cnt;
		for (i = 0; i < m; i++) {
			scanf("%s",str); d = str;
			f(0,0);
		}
		printf("%d\n",cnt-r);
	}
	return 0;
}