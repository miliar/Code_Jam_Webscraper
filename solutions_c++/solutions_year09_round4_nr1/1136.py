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


char A[64][64];

int N, Z[64];

int det( int r ) {
	int max_pos = -1;
	for( int i = 0; A[r][i]; i++ ) if( A[r][i] == '1' ) max_pos = i;
	return max_pos;
}



int main(){
	int T = GI;
	freopen("a.cpp.out","w",stdout);
	REP(tt,T){
		VI perm;
		N = GI;
		REP(i,N) scanf("%s",A[i]), Z[i] = det( i );
				
		int swaps = 0;
		REP(i,N) {			
			int f = i;
			while( f < N ) {
				if( Z[f] <= i ) break;
				f++;
			}
			while( f > i ) swap( Z[f], Z[f-1] ), swaps++, f--;			
		}				

		printf("Case #%d: %d\n",tt+1,swaps);
		
	}	
	return 0;
}