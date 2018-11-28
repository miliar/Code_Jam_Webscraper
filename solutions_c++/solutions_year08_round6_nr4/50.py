#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define FOR(i,a,b) for( int i=(a); i<(b); ++i)
#define FORD(i,a,b) for( int i=(a); i>(b); --i)
#define REP(i,n) for(int i=0; i<(n); ++i)
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) (int)(X).size()
#define FORE(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it)

int d[16][16];
int d2[16][16];

int main(){

	freopen("out", "w", stdout);
	freopen("smallin", "r", stdin);


	int tn, cn;
	cn = 1;
	cin >> tn;
	while(tn--){
		
		int n, m;
		printf("Case #%d: ", cn++);
		cin >> n;
		
		memset( d, 0, sizeof(d) );
		memset (d2, 0, sizeof(d2) );

		REP( i, n-1 ){
			int u, v;
			cin >> u >> v;
				u--, v--;
			d[u][v] = 1;
			d[v][u] = 1;
		}

		
		cin >> m;

		REP( i, m-1 ){
			int u, v;
			cin >> u >> v;
			u--, v--;
			d2[u][v] = 1;
			d2[v][u] = 1;
		}

		int mat[16];
		REP( i, n ) mat[i] = i;
		
		do{
		
			int flag = 1;
			REP( i , n ){
				REP( j, n ) if( d2[i][j] && !d[mat[i]][mat[j]] ) flag = 0;
			}
			if( flag ){
				goto yes;
			}
		}while( next_permutation( mat, mat + n ) );

		printf("NO\n");
		continue;
yes:
		printf("YES\n");
	}

}