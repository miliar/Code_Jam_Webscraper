#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_n=(b);i<=_n;i++)
#define FORD(i,a,b) for(int i=(a),_n=(b);i>=_n;i--)
#define REP(i,n) FOR(i,0,n-1)
typedef long long int64;
#define two(X) (1<<(X))
#define two64(X) (((int64)1)<<(X))
#define contain(S,x) (((S)&two(x))>0)

int L,D,N;
int freq[25][27];
char buf[1005];
char str[5005][25];

int main() {
	scanf( "%d%d%d",&L,&D,&N );
	REP(i,D) scanf( "%s", str[i] );
	REP(i,N) {
		scanf( "%s",buf );
		int len = strlen(buf);
		int res=0,ii=0,ng=0;

		memset( freq,0,sizeof(freq) );
		while ( ii<len ){
			if ( buf[ii]=='(' ) {
				ii++;
				while ( ii<len && buf[ii]!=')' ) 
					freq[ng][buf[ii]-'a']=1, ii++;
				ng++;
			}
			else freq[ng++][buf[ii]-'a']=1;
			ii++;
		}
		REP(j,D) {
			int ok=1;
			REP(k,strlen(str[j])) if ( freq[k][str[j][k]-'a']==0 )
			{ ok=0; break; }
			if ( ok ) {
				res++;
			}
		}
		printf( "Case #%d: %d\n", i+1,res ); 
	}
	return 0;
}
