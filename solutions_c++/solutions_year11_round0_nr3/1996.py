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
	int n, tc, nro;
	scanf("%d", &tc);
	REP(itc, 0, tc) {
		scanf("%d", &n);
		int mini = (1 << 30);
		int t = -1;
		int suma = 0;
		REP(i, 0, n) {
			scanf("%d", &nro);
			mini = min(mini, nro);
			if (t == -1) t = nro;
			else t ^= nro;
			suma += nro;
		}
		if (t == 0) printf("Case #%d: %d\n", itc + 1, suma - mini);
		else printf("Case #%d: NO\n", itc + 1);
	}
	return 0;
}








