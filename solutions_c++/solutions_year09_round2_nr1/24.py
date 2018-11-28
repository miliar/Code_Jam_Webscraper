#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <queue>

using namespace std;

#define ll long long
#define ld long double
#define mp make_pair
#define pb push_back
#define re return
#define fi first
#define se second
#define sqr(x) (x)*(x)
#define sz(x) (x).size ()
#define all(x) x.begin(), x.end ()
#define fill(x,y) std::memset(x,y,sizeof(x))

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vii;
typedef set<int> si;
typedef map<int, int> mii;

template <class T>T abs (T x) { if (x < 0) return -x; else return x; }

vi v[200];
string feat[200];
int q[200], was[200];
double mul[200];
set<string> all;

int main () {
	int tt;
	scanf ("%d\n", &tt);
	for (int it = 0; it < tt; it++) {
		int n;
		scanf ("%d\n", &n);
		string cur = "";
		for (int i = 0; i < n; i++) v[i].clear ();
		int i = 0;
		int r = 0;
		fill (was, 0);
		while (true) {
			char c = getchar ();
			if (c == '(') {
				if (cur != "") {
					was[i] = 0;
					feat[i] = cur;
					i++;
				}
				if (r > 0) v[q[r - 1]].push_back (i);
				scanf ("%lf", &mul[i]);
				q[r++] = i;
                        	cur = "";
                        } else
                        if (c == ')') {
                        	if (!was[i]) {
                        		was[i] = 1;
                        		i++;
                        	}
                        	r--;
                        } else
                        if (c >= 'a' && c <= 'z') cur += c;
                        if (r == 0) break;
		}
		int m;
		scanf ("%d\n", &m);
		printf ("Case #%d:\n", it + 1);
		for (int i = 0; i < m; i++) {
			all.clear ();
			int k;
			string tmp;
			cin >> tmp >> k;
			for (int j = 0; j < k; j++) {
				cin >> tmp;
				all.insert (tmp);
			}
			int cur = 0;
			double res = 1;
			while (true) {
				res *= mul[cur];
				if (v[cur].size ()) {
					if (all.find (feat[cur]) != all.end ()) cur = v[cur][0]; else cur = v[cur][1];
				} else break;
			}
			printf ("%.7f\n", res);
		}
	}
}                
