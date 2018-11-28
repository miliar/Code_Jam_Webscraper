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

vector<bool> poss[35];
vector<int> sums(35);
int dp[110][110];
int n, s, p;

int solve(int pos, int nsur){
	if(nsur > s) return -INF;
	if(pos == n) return 0;
	
	int &val = dp[pos][nsur];
	if(val != -1) return val;
	
	val = solve(pos+1, nsur);
	REP(i, S(poss[sums[pos]])) val = max(val, 1 + solve(pos+1, nsur + poss[sums[pos]][i]));
	
	return val;
}

int main(){
	ios::sync_with_stdio( false );
	int t, tes = 1;
	cin>>t;
	while(t--){
		cin>>n>>s>>p;
		set<int> vals;
		REP(i, n){
			cin>>sums[i];
			vals.insert(sums[i]);
		}
		
		REP(i, 11){
			REP(j, 11){
				REP(k, 11){
					if(abs(i - j) <= 2 && abs(i - k) <= 2 && abs(j - k) <= 2){
						if(vals.count(i + j + k) && max(i, max(j, k)) >= p){
							poss[i+j+k].pb(abs(i - j) == 2 || abs(i - k) == 2 || abs(j - k) == 2);
						}
					}
				}
			}
		}
		
		REP(i, n+2) REP(j, s+2) dp[i][j] = -1;
		cout<<"Case #"<<tes++<<": "<<solve(0, 0)<<'\n';
		
		FORIT(it, vals){
			poss[*it].clear();
		}
	}
	return 0;
}
