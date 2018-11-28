/*
 ID: edusanche1
 PROG: camelot
 LANG: C++
 */
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

typedef long long			ll;
typedef vector<int>			vi;
typedef pair<int, int>		ii;
typedef vector<ii>			vii;
typedef set<int>			si;
typedef map<string, int>	msi;

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

int main() {
	int n, p, t;
	char ch;
	scanf("%d", &n);
	REP(i, 0, n) {
		scanf("%d", &t);
		int po = 1, pb = 1, mo = 0, mb = 0;
		REP(j, 0, t) {
			cin >> ch >> p;
			if (ch == 'O') {
				mo = max(mo + abs(po - p), mb) + 1;
				po = p;
			}
			else {
				mb = max(mb + abs(pb - p), mo) + 1;
				pb = p;
			}
			//dbg4(po, pb, mo, mb);
		}
		printf("Case #%d: %d\n", i + 1, max(mo, mb)); 
	}
}