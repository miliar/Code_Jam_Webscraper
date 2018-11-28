#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;

#define FOI(i, A, B) for(i=A; i<=B; i++)
#define FOD(i, A, B) for(i=A; i>=B; i--)
#define PI		acos(-1.0)
#define INF		1<<30
#define EPS		1e-9
#define sqr(x)	(x)*(x)

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t;
	cin >> T;
	FOI(t, 1, T){
		int N;
		cin >> N;
		string mat[N];
		int i, j, k;
		FOI(i, 0, N-1)
			cin >> mat[i];
		double RPI[N], WP[N], OWP[N], OOWP[N], WWP[N];
		FOI(i, 0, N-1){
			double tot = 0, win = 0;
			FOI(j, 0, N-1){
				if (mat[i][j] != '.')
					tot += 1.0;
				if (mat[i][j] == '1')
					win += 1.0;
			}
			WP[i] = win / tot;
		}
		FOI(i, 0, N-1){
			double tot = 0, wwt = 0;
			FOI(j, 0, N-1){
				if (mat[i][j] != '.'){
					double tt = 0, ww = 0;
					FOI(k, 0, N-1){
						if (mat[j][k] != '.' && k != i)
							tt += 1.0;
						if (mat[j][k] == '1' && k != i)
							ww += 1.0;
					}
					tot += 1.0;
					wwt += ww / tt;
				}
			}
			OWP[i] = wwt / tot;
		}
		FOI(i, 0, N-1){
			double tot = 0, wpt = 0;
			FOI(j, 0, N-1){
				if (mat[i][j] != '.'){
					tot += 1.0;
					wpt += OWP[j];
				}
			}
			OOWP[i] = wpt / tot;
		}
		cout << "Case #" << t << ":\n";
		FOI(i, 0, N-1){
			RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
			cout << RPI[i] << endl;
		}
	}
	return 0;
}
