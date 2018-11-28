#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;

typedef long long ll;
typedef long double ld;
typedef unsigned long ulong;
typedef unsigned long long ull;

int main() {
	int tnum;
	cin >> tnum;
	char a[100][100];
	int wins[100], cnt[100];
	ld wp[100], owp[100];
	ld oowp[100];
	REP(ti,tnum) {
		int n;
		cin >> n;
		REP(i,n) {
			cnt[i] = wins[i] = 0;
			wp[i] = owp[i] = oowp[i] = 0.0;
		}
		string s;
		REP(i,n) {
			cin >> s;
			REP(j,n) {
				a[i][j] = s[j];
				if (a[i][j] != '.')
					++cnt[i];
				if (a[i][j] == '1')
					++wins[i];
			}
			wp[i] = wins[i]/(ld)cnt[i];
		}
		REP(i,n) {
			REP(j,n) {
				if (a[i][j] != '.') {
					if (a[j][i] == '1')
						owp[i] += (wins[j]-1)/(ld)(cnt[j]-1);
					else
						owp[i] += wins[j]/(ld)(cnt[j]-1);
				}
			}
			owp[i] = owp[i]/(ld)cnt[i];
		}
		REP(i,n) {
			REP(j,n) {
				if (a[i][j] != '.')
					oowp[i] += owp[j];
			}
			oowp[i] /= cnt[i];
		}
		printf("Case #%d:\n", ti+1);
		REP(i,n) {
			printf("%.6Lf\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}
	}
	return 0;
}