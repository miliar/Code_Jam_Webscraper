#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int T, N, M, mask[11000][26], res[11000];
string dict[11000];
vi data[11000];
string lists[110];

int main() {
	cin >> T;
	FOR(cs, 1, T+1) {
		cin >> N >> M;
		FOR(i, 0, N) cin >> dict[i];
		memset(mask, 0, sizeof(mask));
		FOR(i, 0, N) FOR(j, 0, sz(dict[i])) mask[i][dict[i][j] - 'a'] |= (1 << j);
		FOR(i, 0, M) cin >> lists[i];
		cout << "Case #" << cs << ":";
		FOR(i, 0, M) {
			FOR(j, 0, N) {
				data[j].clear();
				data[j].push_back(sz(dict[j]));
				FOR(k, 0, 26) data[j].push_back(mask[j][lists[i][k] - 'a']);
				data[j].push_back(j);
			}
			sort(data, data + N);
			memset(res, 0, sizeof(res));
			FOR(j, 1, 27) {
				FOR(k, 0, N) {
					if (data[k][j] != 0 || k == N-1 || data[k+1][j] == 0) continue;
					int kk = k;
					while (1) {
						bool match = true;
						FOR(m, 0, j) {
							if (data[kk][m] != data[k+1][m]) {
								match = false;
								break;
							}
						}
						if (!match) break;
						res[kk]++;
						kk--;
						if (kk < 0) break;
					}
				}
			}
			pii best(-1, -1);
			FOR(j, 0, N) {
				pii v(res[j], -data[j][27]);
				best = max(best, v);
			}
			cout << ' ' << dict[-best.second];
		}
		cout << endl;
	}
	return 0;
}
