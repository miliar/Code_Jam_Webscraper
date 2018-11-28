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
#define INF (int(1e-9))
#define sz size()
#define pb push_back
#define mkp make_pair

typedef pair<int,int> PII;
typedef long long int LL;
typedef vector<int> VI;

int main(){
	int T = GI;
	FOR(tt,1,T){
		LL n,A,B,C,D,x0,y0,M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		vector< pair<LL,LL> > Pts;
		LL x = x0, y = y0;
		Pts.pb( mkp(x,y) );
		REP(i,n-1){
			x = (A*x + B)%M;
			y = (C*y + D)%M;
			Pts.pb( mkp(x,y) );
			
		}
		LL Matrix[9] = {};
		set<int> S;
		EACH(it,Pts){
			int x = (it->first)%3, y = (it->second)%3;
			Matrix[x*3 + y]++;
		}
		LL tot = 0;
		REP(i,9) REP(j,9) REP(k,9) if( j >= i && k >= j ){
			int xtot = i/3 + j/3 + k/3;
			int ytot = i%3 + j%3 + k%3;
			if( xtot%3 != 0 || ytot%3 != 0 ) continue;
			//cout << i <<" "<< j <<" "<< k << endl;
			if( i != j && j != k && k != i ){
				tot += Matrix[i]*Matrix[j]*Matrix[k];
			}
			else if( i == j && k != j && k != i ) {
				tot += Matrix[i]*(Matrix[i]-1)/2 * Matrix[k];
			}
			else if( i == j && j ==k ){
				tot += Matrix[i]*(Matrix[i]-1)*(Matrix[i]-2)/(3*2);
			}			
		}
		printf("Case #%d: ",tt);
		cout << tot << endl;
	}
	return 0;
}
