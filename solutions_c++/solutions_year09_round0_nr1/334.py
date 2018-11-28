/*
TASK: 
LANG: C++
USER: smilitude1
*/


#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)

#define sz size()
#define pb push_back
#define ALL(x) x.begin(), x.end()

#define i64 long long
#define SET(t,v) memset((t), (v), sizeof(t))
#define REV(x) reverse( ALL( x ) )

#define IO freopen("in.in","r",stdin); freopen("out.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl

int L, D, N;
char word[100];
vector< string > v;
char ok[100][26];

int ans() {
	int ret = 0;
	REP(i,D) {
		bool p = true;
		REP(j,L) if( !ok[ j ][ v[i][j] - 'a' ] ) p = false;
		ret += p;
	}
	return ret;
}

int main() {
	int ncase = 0;	

	IO

	scanf("%d %d %d",&L,&D,&N);
	REP(i,D) {
		scanf("%s",word);	
		v.pb( word );
	}
	
	while( N-- ) {
		char buff[1000];
		scanf("%s",buff);
		int len = strlen( buff );
		SET( ok, 0 );
		int i, j; i = j = 0;
		while( i < len ) {
			if( buff[i] == '(' ) {
				++i;
				while( buff[i] != ')' ) {
					ok[ j ][ buff[i] - 'a' ] = 1;
					++i;
				}
				j++, i++;
			}else ok[ j ][ buff[i] - 'a' ] = 1, j++, i++;
		}
		printf("Case #%d: %d\n", ++ncase, ans() );
	}

	return 0;
}
