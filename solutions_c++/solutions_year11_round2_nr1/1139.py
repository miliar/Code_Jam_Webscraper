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
#include <assert.h>
#include <hash_map>
#define rep(x,n) for(int x=0;x<n;x++)
#define mem(a, b) memset(a, b, sizeof(a))
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
using namespace std;
using namespace  stdext;

char matches[101][101];
double wp[101], owp[101], oowp[101], rpi[101];

int main(){

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int t, n;
	cin >> t;
	rep(c, t){
		cin >> n;
		rep(i, n) rep(j, n) cin >> matches[i][j];

		rep(i, n){
			double tot = 0.0, win = 0.0;
			double _owp = 0.0, cnt = 0.0;
			rep(j, n){
				if(matches[i][j] != '.'){
					cnt++;
					tot++;
					if(matches[i][j] == '1') win++;
					double tot2 = 0.0, win2 = 0.0;
					rep(k, n) if(k != i){
						if(matches[j][k] != '.'){
							tot2++;
							if(matches[j][k] == '1') win2++;
						}
					}
					_owp += (win2 / tot2);
				}
			}
			wp[i] = win / tot;
			owp[i] = _owp / cnt;
		}

		rep(i, n){
			double _oowp = 0.0;
			double cnt = 0.0;
			rep(j, n){
				if(matches[i][j] != '.'){
					cnt++;
					_oowp += owp[j];
				}
				oowp[i] = _oowp / cnt;
			}
		}

		printf("Case #%d:\n", c + 1);
		rep(i, n){
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.9lf\n", rpi[i]);
		}
	}
	return 0;
}