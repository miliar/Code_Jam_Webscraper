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
	int c, d, n, tc;
	char ch;
	scanf("%d", &tc);
	
	REP(itc, 0, tc) {
		map < ii, int > changes;
		bool vop[28][28];
		CLR(vop, 0);
		scanf("%d", &c);
		char buf[110];
		REP(i, 0, c) {
			scanf("%s", buf);
			int a = buf[0] - 'A';
			int b = buf[1] - 'A';
			int c = buf[2] - 'A';
			changes[mp(a, b)] = c;
			changes[mp(b, a)] = c;
		}
		
		scanf("%d", &d);
		
		REP(i, 0, d) {
			scanf("%s", buf);
			int a = buf[0] - 'A';
			int b = buf[1] - 'A';
			vop[a][b] = 1;
			vop[b][a] = 1;
		}
		
		scanf("%d", &n);
		
		scanf("%s", buf);
		int lista[110];
		lista[0] = buf[0] - 'A';
		int fin = 0;

		REP(i, 1, n) {
			fin++;
			lista[fin] = buf[i] - 'A';
			//dbg(lista[fin]);
			while (fin >= 1 && changes.count(mp(lista[fin], lista[fin - 1])) != 0) {
				lista[fin - 1] = changes[mp(lista[fin], lista[fin - 1])];
				fin--;
			}
			REP(j, 0, fin) {
				if (vop[lista[j]][lista[fin]]) {fin = -1; break; }
			}
		}
		
		printf("Case #%d: [", itc + 1);
		REP(i, 0, fin + 1) {
			if (i == fin) printf("%c", (char)('A' + lista[i]));
			else printf("%c, ", (char)('A' + lista[i]));
		}
		printf("]\n");
	}
}