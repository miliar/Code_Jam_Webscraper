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
#define PI acos(-1.0)

map<char, char> M;
int main () {
	string a1 = "our language is impossible to understand";
	string a2 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string b1 = "there are twenty six factorial possibilities";
	string b2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string c1 = "so it is okay if you want to just give up";
	string c2 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

	int n = a2.length();
	rep (i, 0, n)
		M[a2[i]] = a1[i];
	n = b2.length ();
	rep (i, 0, n)
		M[b2[i]] = b1[i];

	n = c2.length();
	rep (i, 0, n)
		M[c2[i]] = c1[i];

	M['q'] = 'z';
	M['z'] = 'q';

	int T;
	string s;
	freopen ("/home/shuo/Desktop/A.in", "r", stdin);
	freopen ("/home/shuo/Desktop/ot", "w", stdout);
	cin >> T; cin.ignore();
	for (int ca = 1; ca <= T; ca ++) {
		getline (cin, s);
		n = s.length();
		rep (i, 0, n)
			s[i] = M[s[i]];
		cout << "Case #" << ca << ": " << s << endl;
	}
	return 0;
}
