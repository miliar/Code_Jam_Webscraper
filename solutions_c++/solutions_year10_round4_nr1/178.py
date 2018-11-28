#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn=550, INF=1000000000;

char a[maxn][maxn], num[maxn];
char s[maxn];
int task, T=0, n, m, ret, cur;

int calc(int x, int y){
	for (int i=0; i<m; i++){
		for (int q=y, p=y; 0<=q && p<m; q--, p++)
		if ( a[i][q]!=a[i][p] && a[i][q]!=' ' && a[i][p]!= ' ' )
			return INF;
		for (int q=x, p=x; 0<=q && p<m; q--, p++)
		if ( a[q][i]!=a[p][i] && a[q][i] != ' ' && a[p][i] != ' ' )
			return INF;
	}
	int cur = n + abs(x-(n-1)) + abs(y-(n-1));
	return cur*cur-n*n;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);

	for( scanf("%d", &task); task--; ){
		scanf("%d", &n); gets(s);
		m = n*2-1;
		for (int i=0; i<m; i++){
			memset( a[i], 0, sizeof(a[i]) );
			gets(a[i]);
			for (int j=strlen(a[i]); j<m; j++) 
				a[i][j] = ' ';
		}

		ret = INF;
		for (int i=0; i<m; i++)
		for (int j=0; j<m; j++)
			ret = min( ret, calc( i, j ) );

		printf("Case #%d: %d\n", ++T, ret);
	}
	return 0;
}
