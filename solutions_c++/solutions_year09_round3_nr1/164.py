#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_n=(b);i<=_n;i++)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n;i--)
#define REP(i,n) FOR(i,0,n-1)
typedef long long int64;
#define two(X) (1<<(X))
#define two64(X) (((int64)1)<<(X))
#define contain(S,x) (((S)&two(x))>0)

int64 res;
int used[256];
int cha[256];
int hash[81];
char str[81];

int main() {
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );

	int ntc;
	scanf( "%d",&ntc );
	getchar();
	REP(tc,ntc) {
		gets(str);
			
		int nangka=0;
		memset( used,0,sizeof(used) );
		REP(i,strlen(str)) if ( !used[str[i]] ) 
			nangka++, used[str[i]]=1;
		if ( nangka==1 ) nangka++;

		memset(cha,-1,sizeof(cha));
		memset(hash,0,sizeof(hash));
		
		hash[0]=1;
		cha[str[0]]=1;
		
		int go=0;
		FOR(i,1,strlen(str)-1) 
			if ( cha[str[i]] != -1 )
				hash[i] = cha[str[i]];
			else {
				hash[i] = go;
				cha[str[i]]=go;
				if ( go==0 ) go+=2;
				else go++;
			}
		
		//REP(i,strlen(str)) printf( "%d ", hash[i] );
		//printf( "\n" );

		res = 0;
		int64 p = 1;
		FORD(i,strlen(str)-1,0)
			res += hash[i]*p, p*=nangka;
		
		printf( "Case #%d: %I64d\n", tc+1, res );
	}
	return 0;
}
