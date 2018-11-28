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
		int D[105][105], r, t = 1;
		scanf("%d", &r);
		FOR(i, 0, 102){
			FOR(j, 0, 102){
				D[i][j] = 0;
			}
		}
		int count = 0;
		REP(R, r){
			int a, b, c, d;
			scanf("%d %d %d %d", &a, &b, &c, &d);
			FOR(i, a, c){
				FOR(j, b, d){
					if(D[i][j] == 0) ++count;
					D[i][j] = 1;
				}
			}
		}
		while(count){
			FOR(i, 0, 102){
				FOR(j, 0, 102){
					if(D[i][j] == 0){
						if(D[i-1][j] == t && D[i][j-1] == t){
							D[i][j] = t + 1;
							++count;
						}
					}
				}
			}
			FOR(i, 0, 102){
				FOR(j, 0, 102){
					if(D[i][j] == t){
						if(D[i-1][j] == 0 && D[i][j-1] == 0){
							--count;
							D[i][j] = 0;
							if(D[i+1][j] == t) D[i+1][j]++;
							if(D[i][j+1] == t) D[i][j+1]++;
						}
					}
				}
			}
			FOR(i, 0, 102){
				FOR(j, 0, 102){
					if(D[i][j] == t){
						D[i][j]++;
					}
				}
			}
			++t;
		}
		printf("Case #%d: %d\n", Test, t - 1);
	}
}
