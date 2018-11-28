// C++11

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
#include <unordered_map>
#include <unordered_set>
#include <tuple>
using namespace std;


typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define FORD(i,a,b) for(int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for(__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define pb push_back
#define mp make_pair

const string samplein =
	"yeqz"
	"ejp mysljylc kd kxveddknmc re jsicpdrysi"
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
	"de kr kd eoya kw aej tysr re ujdr lkgc jv";
const string sampleout =
	"aozq"
	"our language is impossible to understand"
	"there are twenty six factorial possibilities"
	"so it is okay if you want to just give up";

bool az(char c) {
	return c >= 'a' && c <= 'z';
}

int main () {
	map<char,char> tr;

	if (sz(samplein) != sz(sampleout)) return 2;
	FOR(i, 0, sz(samplein)) {
		if (!az(samplein[i])) continue;
		if (!az(sampleout[i])) return 3;

		tr.insert(mp(samplein[i], sampleout[i]));
	}
	FOR(i,'a', 'z'+1) {
		if (tr.find(char(i)) == tr.end()) return 4;
	}

	int N;
	cin >> N;
	cin.ignore(42, '\n');

	FOR(i,1,N+1) {
		string line;
		getline(cin, line);
		string out (sz(line), ' ');

		FOR(p,0,sz(line)) {
			out[p] = az(line[p]) ? tr[line[p]] : line[p];
		}
		cout << "Case #" << i << ": " << out << endl;
	}

	return 2;
}
