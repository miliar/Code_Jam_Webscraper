#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int n;
int mat[200][200];
double wp[200];
double owp[200];
double oowp[200];
string s;

int main() {
	int casos, res;
	cin >> casos;
	REP(caso, casos) {
		cin >> n;
		REP(i, n) {
			cin >> s;
			int played = 0;
			wp[i] = 0;
			REP(j, n) {
				if (s[j] == '1') {
					mat[i][j] = 1;
					wp[i] += 1.0;
					played++;
				} else if (s[j] == '0') {
					mat[i][j] = 0;
					played++;
				} else {
					mat[i][j] = 2;
				}
			}
			wp[i] /= played;
		}
		REP(i, n) {
			owp[i] = 0.0;
			int nop = 0;
			REP(i2, n) if (i2 != i && mat[i][i2] != 2) {
				double twp = 0.0;
				int played = 0;
				REP(j, n) if (j != i) {
					if (mat[i2][j] == 1) {
						twp += 1.0;
						played++;
					} else if (mat[i2][j] == 0) {
						played++;
					}
				}
				twp /= played;
				owp[i] += twp;
				nop++;
			}
			owp[i] /= nop;
		}
		REP(i, n) {
			oowp[i] = 0.0;
			int nop = 0;
			REP(i2, n) if (i2 != i && mat[i][i2] != 2) {
				oowp[i] += owp[i2];
				nop++;
			}
			oowp[i] /= nop;
		}
		cout << "Case #" << caso+1 << ":" << endl;
		REP(i, n) cout << fixed << setprecision(7) << .25*wp[i] + .5 * owp[i] + .25*oowp[i] << endl;
	}
	return 0;
}
