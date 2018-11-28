#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<list>
#include<string>
#include<cstring>
#include<cstdlib>
#include<set>
#include<map>
#include<vector>
using namespace std;

#define MAX 1005
int N;
int test_case;
bool path[ MAX ][ MAX ];
bool visit[ MAX ];
int cnt[ MAX ];
bool ok ;


void dfs( int node, int startNode ) {
//	printf("%d\t", node);
	for( int i = 1; i <= N; i ++ ) {
		if( path[ node ][ i ] ) {
			cnt[ i ] ++ ;
			if( cnt [ i ] >= 2 ) ok = true;
			if( !visit[ i ] ){
				visit[ i ] = true;
				dfs( i, startNode ) ;
				visit[ i ] = false ;
			}
		}
	}
}

int main(){
	//freopen("a.txt", "r", stdin);
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("outsmall.txt", "w", stdout);
	int i,j,a,b;
	scanf("%d", &test_case);
	for( int caseId = 1; caseId <= test_case; caseId ++ ) {
		scanf("%d", &N);
		memset( path, false, sizeof( path ) ) ;
		memset( visit, false , sizeof( visit ) ) ;
		for( i = 1; i <= N; i ++ ) {
			scanf("%d", &a);
			for( j = 0; j < a; j ++ ) {
				scanf("%d", &b);
				path[ i ][ b ] = true;

			}
		}

		ok = false;
		for( i = 1; i <= N;  i ++ ) {
				memset( cnt, 0, sizeof( cnt ) ) ;
				dfs( i, i );
			
			
		}

		if( ok ) printf("Case #%d: Yes\n",caseId);
		else printf("Case #%d: No\n", caseId);
	}
	return 0;
}