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
	freopen("B-large.in", "rt", stdin);
	int t; cin >> t;
	REP(test,t){
		int n,k,b,t,xi,vi;
		vector<int> x,v;
		cin >> n >> k >> b >> t;
		REP(i,n) cin >> xi, x.pb(xi);
		REP(i,n) cin >> vi, v.pb(vi); 
		int c = 0;
		int res = 0;
		FORD(i,n-1,0){
			if (c == k) break;
			double ti = (b-x[i]+0.)/v[i];
			if (ti > double(t)) {
				continue;
			}
			int sw = 0;
			FOR(j,i+1,n){
				double tj = (b-x[j]+0.)/v[j];
				if (tj > double(t)) {
					++sw;
				}
			}
			res +=sw;
			++c;
		}
		cout << "Case #" << (test+1) << ": ";
		if (c==k) cout << res; else cout << "IMPOSSIBLE";
		cout << endl;
	}
}
