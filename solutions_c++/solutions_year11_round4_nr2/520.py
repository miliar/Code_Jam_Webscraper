#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <cfloat>
#include <cctype>
#include <algorithm>
#include <sstream>
#include <bitset>

#define REP(i,a) for(i=0;i<a;++i)
#define FOR(i,a,b) for(i=a;i<=b;++i)
#define all(x) (x).begin(),(x).end()
#define pb(x) push_back(x)
#define sz(x) (int)(x).size()
using namespace std;

int di[501][501];
long long dj[501][501];
long long dk[501][501];
long long dd[501][501];

void main() {
	int T;
	cin >> T;
	int i,j,k;
	int R,C,D;
	REP(i,T) {
		memset(di, 0x00, sizeof(di));
		memset(dj, 0x00, sizeof(dj));
		memset(dk, 0x00, sizeof(dk));
		memset(dd, 0x00, sizeof(dd));
		cin >> R >> C >> D;
		string w;
		REP(j,R) {
			cin >> w;
			REP(k,C) {
				di[j][k] = w[k] - '0' + D;
			}
		}

		REP(j,R) {
			dj[j][0] = 0;
			dk[j][0] = 0;
		}
		REP(k,C) {
			dj[0][k] = 0;
			dk[0][k] = 0;
		}

		FOR(j,1,R) {
			FOR(k,1,C) {
				dj[j][k] = dj[j-1][k] + dj[j][k-1] - dj[j-1][k-1] + di[j-1][k-1] * j;
				dk[j][k] = dk[j-1][k] + dk[j][k-1] - dk[j-1][k-1] + di[j-1][k-1] * k;
				dd[j][k] = dd[j-1][k] + dd[j][k-1] - dd[j-1][k-1] + di[j-1][k-1];
			}
		}

		int maxv = min(R,C);

		int res = -1;
		REP(j,R) {
			REP(k,C) {
				//cout << j << "," << k << " dx " << dj[j][k] << " dy " << dk[j][k] << " dz " << dd[j][k] << endl;
				int x = j + 2;
				int y = k + 2;
				int len = 3;
				while (x < R && y < C) {
					long long dx = dj[x+1][y+1] - dj[j][y+1] - dj[x+1][k] + dj[j][k] - di[j][k] * (j+1) - di[x][y] * (x+1) - di[j][y] * (j+1) - di[x][k] * (x+1);
					long long dy = dk[x+1][y+1] - dk[j][y+1] - dk[x+1][k] + dk[j][k] - di[j][k] * (k+1) - di[x][y] * (y+1) - di[j][y] * (y+1) - di[x][k] * (k+1);
					long long dz = dd[x+1][y+1] - dd[j][y+1] - dd[x+1][k] + dd[j][k] - di[j][k] - di[x][y] - di[j][y] - di[x][k];
					//cout << j << "," << k << " ~ " << x << " ," << y << " => " << dx << "," << dy << "," << dz << endl;
					int nx = (j + x) + 2;
					int ny = (k + y) + 2;
					//cout << nx << " - " << ny << endl;
					if (nx * dz == dx * 2 && ny * dz == dy * 2) {
						res = max(res, len);
					}
					++x;
					++y;
					++len;
				}
			}
		}

		if (res == -1)
			cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i+1 << ": " << res << endl;
	}
}