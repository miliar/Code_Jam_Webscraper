#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std; 

#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define INF 1000000000
#define EPS 0.0000000001
#define X first
#define Y second
#define pb push_back
#define sz size()

typedef pair<int, int> PII;
typedef long long i64; 

int main() {
	freopen("A-large.in", "rt", stdin);
	int t; cin >> t;
	REP(test,t){
		int n,m; scanf("%d%d\n", &n, &m);
		string s;
		set<string> a;
		int res = 0;
		REP(i,n){
			getline(cin,s);
			string dir; dir += s[0];
			dir.reserve(s.sz);
			FOR(j,1,s.sz){
				if (s[j]=='/' || j==s.sz-1) {
					if (j==s.sz-1) dir += s[j];
					a.insert(dir);
				}
				if (j<s.sz-1) dir += s[j];
			}
		}
		REP(i,m){
			getline(cin,s);
			string dir; dir += s[0];
			dir.reserve(s.sz);
			FOR(j,1,s.sz){
				if (s[j]=='/' || j==s.sz-1) {
					if (j==s.sz-1) dir += s[j];
					if (a.find(dir)==a.end()) {
						a.insert(dir);
						++res;
					}
				}
				if (j<s.sz-1) dir += s[j];
			}
		}
		cout << "Case #" << (test+1) << ": " << res << endl;
	}
}
