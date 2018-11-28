#include <valarray>
#include <bitset>
#include <string>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <iostream>
#include <cstring>
#include <cctype>
#include <cstdio>
#include <cmath>
#define PB push_back
#define MP make_pair
#define REP(i, n) for(int _n = n, i = 0; i < _n; ++i)
#define FOR(i, a, b) for(int i = (a), _b = (b); i <= _b; ++i)
#define FORD(i, a, b) for(int i = (a), _b = (b); i >= _b; --i)
#define EACH(it, c) for(__typeof((c).begin()) it = (c).begin(), it_ = (c).end(); it != it_; ++it)
#define ALL(c) (c).begin(), (c).end()

using namespace std;
template<class T> inline T abs(const T &x) { return x < 0 ? -x : x; }

int main(){
	int Tests;
	scanf("%d ", &Tests);
	FOR(Test, 1, Tests){
		int p, x;
		scanf("%d", &p);
		vector<int> M;
		REP(i, 1 << p){
			scanf("%d", &x);
			M.PB(x);
		}
		vector<int> C[p];
		FOR(i, 1, p){
			REP(q, 1 << (p - i)){
				scanf("%d", &x);
				C[i-1].PB(x);
			}
		}
		int result = 0;
		while(M.size() > 1){
			vector<int> N;
			for(int i = 0; i < M.size(); i += 2){
				x = min(M[i], M[i + 1]);
				if(x == 0){
					++result;
				}
				else{
					--x;
				}
				N.PB(x);
			}
			M = N;
		}
		if(M[0] == 0) ++result;
		printf("Case #%d: %d\n", Test, result - 1);
	}
}
