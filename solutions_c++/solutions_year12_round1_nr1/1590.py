#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue> 
#include <cfloat>
#include <string> 
#include <climits> 
#include <cstring> 
#include <cassert> 
#include <complex>

using namespace std;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3FFFFFFFFFLL
#define EPS 1e-7

#define FILL(X, V) memset(X, V, sizeof(X))
#define TI(X) __typeof((X).begin())

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FORIT(it, i) for(typeof((i).begin()) it = (i).begin(); it != (i).end(); it++)

#define ALL(V) V.begin(), V.end()
#define S(V) (int)V.size()

#define pb push_back
#define mp make_pair

template<typename T> T inline SQR( const T &a ){ return a*a; }

typedef long long int64;
typedef unsigned long long uint64;

int a, b;

int main(){
	ios::sync_with_stdio( false );
	int t, tes = 1;
	cout<<fixed<<setprecision(6);
	cin>>t;
	while(t--){
		cin>>a>>b;
		vector<double> p(a);
		REP(i, a) cin>>p[i];
		vector<double> probs((1 << a));
		
		vector<double> vals(a + 2);
		REP(i, (1 << a)){
			double prob = 1.;
			REP(j, a){
				if(i & (1 << j)) prob *= p[j];
				else prob *= (1. - p[j]);
			}
			
			probs[i] = prob;
			int cnt = __builtin_popcount(i);
			if(cnt == a){
				vals[0] += probs[i]*(b - a + 1);
			}else{
				vals[0] += probs[i]*(b - a + 2 + b);
			}
			
			vals[a+1] += probs[i] * (b + 2);
			
			FOR(j, 1, a+1){
				int cnt2 = 0;
				REP(k, a-j){
					if(i & (1 << k)) cnt2++;
				}
				
				if(cnt2 == a-j){
					vals[j] += probs[i]*(b - a + 2*j + 1);
				}else{
					vals[j] += probs[i]*(b - a + 2*j + 2 + b);
				}
			}
		}
		
		double ans = vals[0];
		FOR(i, 1, a+2){
			ans = min(ans, vals[i]);
		}
		
		cout<<"Case #"<<tes++<<": "<<ans<<'\n';
	}
	return 0;
}
