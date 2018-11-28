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
	freopen("a-large.in", "rt", stdin);
	int t,n,k;
	cin >> t;
	REP(step,t){
		cin >> n >> k;
		int p = 1<<n;
		bool on = (k%p == p-1);
		cout << "Case #" << (step+1) << ": " << (on?"ON":"OFF") << endl;
	}
}
