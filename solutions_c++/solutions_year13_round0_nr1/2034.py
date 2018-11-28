#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <climits>
#include <map>
#include <stack>
#include <queue>
#include <complex>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo (1<<30)
#define M 1001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

string a[4], b[4];

int main() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
		freopen("o.txt", "wt", stdout);
#endif
	int t, tt = 1;
	cin >> t;
	while (t--) {
		int cs = -1, dot = 0;
		FOR (i , 0 , 4) {
			cin >> a[i];
			b[i] = a[i];
			FOR (j , 0 , sz(a[i])) {
				if (a[i][j] == 'T')
					a[i][j] = 'X', b[i][j] = 'O';
				dot += (a[i][j] == '.');
			}
		}
		string dig1 = "", dig2 = "", col = "", dig3 = "", dig4 = "";
		FOR (i , 0 , 4) {
			if (a[i] == "XXXX" || b[i] == "XXXX") {
				cs = 1;
				break;
			}
			if (a[i] == "OOOO" || b[i] == "OOOO") {
				cs = 2;
				break;
			}
			string t1 = "", t2 = "";
			FOR (j, 0 , 4) {
				t1 += a[j][i];
				t2 += b[j][i];
			}
			if (t1 == "XXXX" || t2 == "XXXX") {
				cs = 1;
				break;
			}
			if (t1 == "OOOO" || t2 == "OOOO") {
				cs = 2;
				break;
			}
			dig1 += a[i][i];
			dig2 += b[i][i];
			dig3 += a[i][3 - i];
			dig4 += b[i][3 - i];
		}
		if (dig1 == "XXXX" || dig2 == "XXXX" || dig3 == "XXXX" || dig4 == "XXXX")
			cs = 1;
		if (dig1 == "OOOO" || dig2 == "OOOO" || dig3 == "OOOO" || dig4 == "OOOO")
			cs = 2;
		switch (cs) {
		case 1:
			printf("Case #%d: X won\n", tt++);
			break;
		case 2:
			printf("Case #%d: O won\n", tt++);
			break;
		case -1:
			if (dot)
				printf("Case #%d: Game has not completed\n", tt++);
			else
				printf("Case #%d: Draw\n", tt++);
			break;
		}
	}
	return 0;
}
