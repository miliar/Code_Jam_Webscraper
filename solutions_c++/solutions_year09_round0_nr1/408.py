#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdarg>
#include <cassert>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <set>
#include <list>
#include <algorithm>
#include <utility>
#include <unistd.h>
#include <cstdlib>
#include <map>
#include <sstream>
using namespace std;

#define REP(i,N) for(int i = 0;i < (N); ++i )
#define REPV(i,ar) for(int i = 0;i < (ar).sz; ++i )
#define EACH(it,mp) for( __typeof(mp.begin()) it(mp.begin()); it != mp.end(); ++it )
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i )
#define sz size()
#define pb push_back
#define mkp make_pair
#define INF (int(1e9))
#define GI ({int t;scanf("%d",&t);t;})
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long int LL;

char s[1024];
bool A[32][1024];


int main(){
	freopen("temp.cpp.out" , "w", stdout );
	int L = GI, D = GI, N = GI;
	set<string> S;
	REP(i,D) {
		scanf("%s",s);
		S.insert( s );
	}
	
	REP(ii,N){
		memset( A , 0 , sizeof( A ) );
		scanf("%s",s);
		
		for( int i = 0, p = 0; s[i]; ++i ) {
			if( s[i] >= 'a' && s[i] <= 'z' ) A[p][s[i]] = 1;
			else {
				assert( s[i] == '(' );
				++i;
				while( s[i] != ')' ) A[p][ s[i++] ] = 1;			
			}
			p++;		
		}
		
		int ans = 0;
		EACH(it,S){
			const string& s = (*it);
			assert( s.sz == L );
			bool found = 1;
			REPV(i,s) if( A[i][s[i]] == 0 ) found = 0;
			ans += found;		
		}
		printf("Case #%d: %d\n", ii+1, ans );
	}
	
		
	return 0;
}