#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_n=(b);i<=_n;i++)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n;i--)
#define REP(i,n) FOR(i,0,n-1)
typedef long long int64;
#define two(X) (1<<(X))
#define two64(X) (((int64)1)<<(X))
#define contain(S,x) (((S)&two(x))>0)

char n[31];
int np, ni, na;
int permut[31];
int init[31];

int main() {

	freopen( "B-large.in", "r", stdin );
	freopen( "B-large.out", "w", stdout );
	
	int ntc;
	scanf("%d",&ntc);
	getchar();

	REP(tc,ntc) {
		gets(n);
		
		np = ni = na = 0;
		REP(i,strlen(n)) {
			permut[np++] = n[i]-'0';
			init[ni++] = n[i]-'0';
		}

		sort( init,init+ni );
		next_permutation(permut,permut+np);
		
		int same=1;
		REP(i,np) if ( permut[i]!=init[i] ) {
			same = 0;
			break;
		}
		
		printf( "Case #%d: ", tc+1 );
		if ( same ) {
			REP(i,np) if ( init[i]!=0 ) { 
				swap( init[0], init[i] );
				break;
			}
			printf( "%d0", init[0] );
			FOR(i,1,np-1) printf( "%d",init[i] );
			printf( "\n" );
		}
		else {
			REP(i,np) printf( "%d", permut[i] );
			printf( "\n" );
		}
	}
	return 0;
}
