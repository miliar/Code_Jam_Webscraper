#include<iostream>
using namespace std;

int sw[256];
#define maxn 100010
#define maxm 26
int child[maxn][maxm], is[maxn], end;

struct Tree{
	void Init() {
		end = 0;
		memset(child, 0, sizeof(child) );
		memset(is, 0, sizeof(is));
	}
	void Insert( char *ss ) {
		int p = 0;
		for( ; *ss; ss ++ ) {
			int c = sw[ *ss ];
			if( child[p][c] == 0 ) 
				child[p][c] = ++ end;
			p = child[p][c];
		}
		is[p] = 1;
	}
}my;

int lens, n, m, ans;
char str[maxn];

void DFS( int deep, int x, int p ) {
	if( str[x] == 0 ) {
		ans += is[p];
		return;
	}
	if( str[x] != '(' ) {
		if( child[p][ sw[str[x] ]] != 0 )
			DFS( deep + 1, x + 1, child[p][ sw[str[x]] ]);
		return;
	}
	bool hash[26] = {0};
	int j = x + 1;
	while( str[j] != ')' ) j ++;
	for( int i = x + 1; i < j; i ++ ) {
		if( hash[ sw[str[i]] ] ) continue;
		hash[ sw[str[i] ] ] = 1;
		if( child[p][ sw[str[i]] ] ) {
			DFS( deep + 1, j + 1, child[p][ sw[str[i] ]] );
		}
	}
}


int main() {
	freopen("D:\\in.in", "r", stdin);
	freopen("D:\\laout.out", "w", stdout);
	for( int i = 'a'; i <= 'z'; i ++ )
		sw[i] = i - 'a';
	while( scanf("%d %d %d",&lens,&n, &m) != EOF ) {
		my.Init();
		for( int i = 0; i < n; i ++ ) {
			scanf("%s", str);
			my.Insert( str );
		}
		for( int i = 1; i <= m; i ++ ) {
			scanf("%s", str);
			ans = 0;
			DFS( 0, 0, 0);	
			printf("Case #%d: %d\n", i, ans);
		}
	}
	return 0;
}