#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <utility>
#include <cassert>
using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,N) for(int i = 0;i < (N); ++i )
#define EACH(it,mp) for( __typeof(mp.begin()) it(mp.begin()); it != mp.end(); ++it )
#define REPV(i,ar) for(int i = 0; i < (ar).sz; ++i )
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i )
#define INF (int(1e7))
#define sz size()
#define pb push_back
#define mkp make_pair

typedef pair<int,int> PII;
typedef long long int LL;
typedef vector<int> VI;


int main(){
	int T = GI;
	char Str[1024];
	FOR(tt,1,T){
		int K = GI;
		scanf("%s",Str);
		
		VI V;
		REP(i,K) V.pb( i );
		int ans = INT_MAX;
		do {
			char NStr[1024] = {};
			for( int i = 0,l = 0; Str[i] ; l += K ){
				REP(j,K){
					NStr[i] = Str[l + V[j]];
					i++;
				}
				//cout << NStr << endl;
			}
			char prev = 0;
			int cnt = 0;
			for(int i = 0; NStr[i]; ++i ) {
				if( NStr[i] != prev ) cnt++, prev = NStr[i];
			}
			ans <?= cnt;
		} while( next_permutation( V.begin() , V.end() ) );
		printf("Case #%d: %d\n",tt,ans);
		
	}
	return 0;
}
