#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <functional>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <cstdarg>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <numeric>
#include <utility>
#include <cmath>
using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for (int i=0; i<int(n); i++)
#define all(a) a.begin(), a.end()

typedef long double ldb;
typedef long long lld;
typedef vector<int> vi;
typedef complex<double> cd;

double const eps=1e-9;
ldb const epsl=1e-9;
int const inf=0x3fffffff;
lld const infl=0x3fffffffffffffffLL;
template <class T>
inline T sqr(const T &a) {
	return a*a;
}



int nv;
vector<string> s;
vector< map<string,int> > v;


int main () {
	freopen("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int nt;
	cin >> nt;
	for (int it=1; it<=nt; it++) {
		s.resize(1);
		s[0].clear();
		v.resize(1);
		v[0].clear();
		nv=0;
		int n, m;
		if (it==11)
			it=it;
		cin >> n >> m;
		for (int i=0; i<n; i++) {
			int ps=0;
			string d; cin >> d;
			while(!d.empty()) {
				d=d.substr(1);
				int t=d.find_first_of("/");
				if (t<0) t=d.size();
				string cr=d.substr(0, t);
				if (!v[ps][cr]) {
					v[ps][cr]=++nv;
					s.resize(nv+1);
					v.resize(nv+1);
				}
				if (t==d.size()) break;
				d=d.substr(t);
				ps=v[ps][cr];
			}
		}
		int res=0;
		for (int i=0; i<m; i++) {
			int ps=0;
			string d; cin >> d;
			while(!d.empty()) {
				d=d.substr(1);
				int t=d.find_first_of("/");
				if (t<0) t=d.size();
				string cr=d.substr(0, t);
				if (!v[ps][cr]) {
					v[ps][cr]=++nv;
					s.resize(nv+1);
					v.resize(nv+1);
					res++;
				}
				if (t==d.size()) break;
				d=d.substr(t);
				ps=v[ps][cr];
			}
		}
		cout << "Case #" << it << ": " << res << endl;
	}

	return 0;
}