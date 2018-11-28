#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

char perm[26];

void learn(string a, string b) {
		REP (i, sz(a)) {
				if (isalpha(a[i]))
						perm[a[i]-'a'] = b[i];
		}
}

int main () {
#ifdef LocalHost
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
#endif
		learn("yeq", "aoz");
		learn("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
		learn("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
		learn("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
		learn("z", "q");
		int t;
		cin >> t;
		string s;
		getline(cin, s);
		REP (i, t) {
				getline(cin, s);
				cout << "Case #" << (i+1) << ": "; 
				REP (i, sz (s)) {
						if (isalpha(s[i]))
								cout << perm[s[i]-'a'];
						else
								cout << s[i];
				}
				cout << endl;
		}
    return 0;
}
