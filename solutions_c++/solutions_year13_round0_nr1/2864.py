#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define clr(x, v) memset(x, v, sizeof(x))
#define rep(i, l, u) for(int i = (l); i < (u); i++)
#define repv(i, v) for(i = 0; i < (int)v.size(); i++)
#define repi(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)


bool chk (vector<string> vs, char c) {
	int i, j, k3 = 0, k4 = 0;
	for (i = 0; i < 4; ++i) {
		int k1 = 0, k2 = 0;
		for (j = 0; j < 4; ++j) {
			k1 += (vs[i][j] == c || vs[i][j] == 'T') ? 1 : 0;
			k2 += (vs[j][i] == c || vs[j][i] == 'T') ? 1 : 0;
		}
		if (k1 == 4 || k2 == 4) return true;
		k3 += (vs[i][i] == c || vs[i][i] == 'T') ? 1 : 0;
		k4 += (vs[i][3-i] == c || vs[i][3-i] == 'T') ? 1 : 0;
	}
	return (k3==4) || (k4==4);
}

int main () {
	int i, j, k;
	int T, ca;

	freopen ("A.txt", "w", stdout);
	for (cin >> T, ca = 1; ca <= T; ca++) {
		vector<string>vs;
		string s;
		k = 0;
		for (i = 0; i < 4; ++i) { 
			cin >> s; vs.push_back(s);
			for (j = 0; j < 4; ++j) if (vs[i][j] == '.') k++;
		}
		cout << "Case #" << ca << ": ";
		if (chk(vs, 'X')) cout << "X won" << endl;
		else if (chk(vs, 'O')) cout << "O won" << endl;
		else if(k == 0) cout << "Draw" << endl;
		else cout << "Game has not completed" << endl;
	}
	return 0;
}
