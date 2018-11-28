//      hello world


//DS includes
#include<bitset>
#include<complex>
#include<deque>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

//Other Includes
#include<algorithm>
#include<cassert>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iostream>
#include<sstream>

#define oo 			0xBADC0DE
#define s(n)			scanf("%d",&n)
#define sl(n) 			scanf("%lld",&n)
#define sf(n) 			scanf("%lf",&n)
#define fill(a,v) 		memset(a, v, sizeof a)
#define ull 			unsigned long long
#define ll 				long long
#define bitcount 		__builtin_popcount
#define all(x) 			x.begin(), x.end()
#define pb( z ) 		push_back( z )
#define gcd				__gcd

#define FOR(i,n) for (int i=0; i < (n); i++)

using namespace std;

int n;
vector<int> bpos, opos;
int main(int argc, char** argv) {
	
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	//freopen("A-small-attempt3.in", "r", stdin); freopen("A-small-attempt3.out", "w", stdout);
	
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	
	int runs;
	cin>>runs;
	for (int X=1; X <= runs; X++) {
		printf("Case #%d: ", X);
		cin>>n; bpos.clear(); opos.clear();
		string moves = "";
		for (int i=0; i < n; i++) {
			string z; int p;
			cin>>z>>p;
			if (z == "O") {
				opos.pb(p);
			} else {
				bpos.pb(p);
			}
			moves += z;
		}
		int op = 1, bp = 1;
		int ob = 0, bb = 0;
		int prevTime = 0;
		int bTime = 0, oTime = 0;
		while (ob < opos.size() || bb < bpos.size()) {
			int turn = moves[ ob + bb ] == 'O' ? 1 : 0;
			if (turn) {
				int cur = opos[ob++]; 
				int reachAndPushTime = 1 + abs(cur - op);
				if (reachAndPushTime + oTime > prevTime) {
					prevTime = reachAndPushTime + oTime;
				} else {
					prevTime = 1 + prevTime;
				}
				oTime = prevTime;
				op = cur;
			} else {
				int cur = bpos[bb++]; 
				int reachAndPushTime = 1 + abs(cur - bp);
				if (reachAndPushTime + bTime > prevTime) {
					prevTime = reachAndPushTime + bTime;
				} else {
					prevTime = 1 + prevTime;
				}
				bTime = prevTime;
				bp = cur;
			}
		}
		cout << prevTime << endl;
	}
	return 0;
}
