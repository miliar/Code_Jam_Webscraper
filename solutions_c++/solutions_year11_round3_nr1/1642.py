#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

using namespace std;

#define REP(i, a, b) for (int i = int(a); i < int(b); i++)
#define TRvi(c, it)  for (vi::iterator it = (c).begin(); it != (c).end(); it++)

#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) //traverse containers
#define pb push_back
#define mp make_pair

#define dbg(x) cout << #x << " = " << x << "\n";
#define dbg2(x, y) cout << #x << " = " << x << "  " << #y << " = " << y << "\n";
#define dbg3(x, y, z) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "\n";
#define dbg4(x, y, z, w) cout << #x << " = " << x << "  " << #y << " = " << y << "  " << #z << " = " << z << "  " << #w << " = " << w << "\n";

#define ALL(x) (x).begin(),(x).end()
#define CLR(a,b) memset(a, b, sizeof a)

int r, c;

int my[4] = { 0, 0, 1, 1 };
int mx[4] = { 0, 1, 0, 1 };

char car[4] = { '/', '\\', '\\', '/' };

bool in(int y, int x) {
	return (y >= 0 && x >= 0 && y < r && x < c);
}

int main() {
	int t;
	scanf("%d", &t);
	REP(i, 0, t) {
		scanf("%d %d", &r, &c);
		vector < string > v;
		string pal;
		REP(j, 0, r) {
			cin >> pal;
			v.pb(pal);
		}
		
		bool bo = true;
		
		REP(j, 0, r) {
			REP(k, 0, c) {
				if (v[j][k] == '#') {
					REP(p, 0, 4) {
						int nj = j + my[p];
						int nk = k + mx[p];
						if (!in(nj, nk) || v[nj][nk] != '#') {
							bo = false;
							break;
						}
						v[nj][nk] = car[p];
						
					}
				}
				if (!bo) break;
			}
			if (!bo) break;
		}
		printf("Case #%d:\n", i + 1);
		if (!bo) {
			cout << "Impossible\n";
		}
		else {
			REP(j, 0, r) {
				cout << v[j] << "\n";
			}
		}
	}
	
	return 0;
}