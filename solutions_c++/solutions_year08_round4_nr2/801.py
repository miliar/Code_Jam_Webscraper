#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 
#define INT_INF 0x7FFFFFFF
// BEGIN CUT HERE
#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)

string itos(int x) { stringstream ss; ss << x; return ss.str(); }
vector<string> split(string s) { vector<string> r; string t; stringstream ss(s); while(ss >> t) r.push_back(t); return r; }


int main() {
	int NC,N,M,A;
	scanf("%d",&NC);
	
	long long tab[51][51];
	rep(i,51) {
		rep(j,51) {
			tab[i][j] = i*j;
		}
	}
	
	rep(i,NC) {
		scanf("%d %d %d", &N,&M,&A);
		
		if (A < 100000)
		rep(y1,M+1) {
			rep(x2,N+1) {
				rep(x3, N+1) {
					rep(y3, M+1) {
						if (abs( tab[x2][y3] + tab[x3][y1] - tab[y1][x2] ) == A) {
							printf("Case #%d: %d %d %d %d %d %d\n",i+1, 0,y1,x2,0,x3,y3);
							goto fim;
						}
					}
				}
			}
		}
		
		printf("Case #%d: IMPOSSIBLE\n",i+1);
		fim:;
	}
}













