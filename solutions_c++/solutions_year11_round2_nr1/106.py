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
#define eps 1e-9
#define FOR(x, s, e) for(int x = (s); x < (e); ++x)
#define FORc(x, s, e, c) for(int x = (s); x < (e) && (c); ++x)
#define STEP(x, s, e, d) for(int x = (s); x < (e); x+=(d))
#define ROF(x, s, e) for(int x = (s); x >= (e); --x)
#define ROFc(x, s, e, c) for(int x = (s); x >= (e) && (c); --x)
#define vb vector<bool>
#define vi vector<int>
#define vii vector<pair<int, int> >
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define LL long long
#define pii pair<int, int>
#define x first
#define y second
#define gcd(x, y) __gcd((x), (y))
#define countbit(x) __builtin_popcount(x)

using namespace std;

int main(int argc, char **argv){
	int T;
	cin >> T;
	FOR(Ca, 1, T+1){
		printf("Case #%d:\n", Ca);
		int N;
		cin >> N;
		int st[N][N];
		string s;
		FOR(i, 0, N){
			cin >> s;
			FOR(j, 0, N) if (s[j] == '.') st[i][j] = -1; else st[i][j] = s[j] == '1';
		}
		double WP[N];
		memset(WP, 0, sizeof(WP));
		FOR(i, 0, N){
			int C = 0, W = 0;
			FOR(j, 0, N) if (st[i][j] != -1) C++, W += st[i][j];
			WP[i] = 1.*W/C;
		}
		double OP[N];
		memset(OP, 0, sizeof(OP));
		FOR(i, 0, N){
			int D = 0;
			double sum = 0;
			FOR(j, 0, N)
				if (st[i][j] != -1){
					D++;
					int cc=0, ww=0;
					FOR(k, 0, N) if (st[j][k] != -1 && k != i){
						cc++;
						ww += st[j][k];
					}
					sum += 1.*ww/cc;
				}
			OP[i] = sum / D;
		}
		double OOP[N];
		memset(OOP, 0, sizeof(OOP));
		FOR(i, 0, N){
			int D = 0;
			FOR(j, 0, N) if (st[i][j] != -1) OOP[i] += OP[j], D++;
			OOP[i] /= D;
		}
		FOR(i, 0, N) printf("%.10f\n", .25*WP[i]+.5*OP[i]+.25*OOP[i]);
	}
	return 0;
}
