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

using namespace std;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

const string query = "welcome to code jam";
int N;
string text;
int tab[20][600];

int rek(int q, int p) {
	if (q == sz(query)) return 1;
	if (p >= sz(text)) return 0;
	int &res = tab[q][p];
	if (res != -1) return res;
	res = 0;
	FOR(i, p, sz(text)) {
		if (text[i] == query[q]) res = (res + rek(q+1, i+1)) % 10000;
	}
	return res;
}

int main() {
	cin >> N;
	getline(cin, text);
	FOR(cs, 1, N+1) {
		getline(cin, text);
		memset(tab, -1, sizeof(tab));
		int res = rek(0, 0);
		cout << "Case #" << cs << ": ";
		ostringstream os;
		os << res;
		string s = os.str();
		while (sz(s) < 4) s = "0" + s;
		cout << s << endl;
	}
	return 0;
}
