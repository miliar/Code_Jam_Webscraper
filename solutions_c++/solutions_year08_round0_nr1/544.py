#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <string>
using namespace std;
#define MAXN 110
#define MAXM 1010
#define INF 1000000

string a[MAXN];
string b[MAXM];
int n, m;
int g[MAXN];

void read (int *n,string a[]) {
	char tmp[110];
	int i;
	scanf("%d",n);
	gets(tmp);
	for (i=1; i<=*n; i++) {
		gets(tmp);
		a[i]=(string)tmp;
	}
}

int main () {
	int c, t, i, j;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	for (scanf("%d",&c), t=1; t<=c; t++) {
		read(&n,a);
		read(&m,b);
		memset(g, 0, sizeof(g));
		for (i=1; i<=m; i++) {
			j=(int)(find(a+1,a+n+1,b[i])-a);
			g[j]=INF;
			g[j]=*min_element(g+1,g+n+1)+1;
		}
		printf("Case #%d: %d\n", t, *min_element(g+1,g+n+1));
	}
	return 0;
}