#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,n) FORD(i,0,n)
#define VAR(v,w) __typeof(w) v=(w)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define SIZE(c) ((int)(c).size())
#define MP make_pair
#define FT first
#define SD second
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<double> VD;
typedef vector<LD> VLD;
typedef vector<LL> VLL;
typedef vector<bool> VB;
typedef istringstream ISS;
typedef ostringstream OSS;

int main() {
	int ccc;
	cin >> ccc;
	REP(cc,ccc) {
		int k;
		string s;
		cin >> k >> s;
		int p[5];
		REP(i,k)
			p[i] = i;
		int res = 1000000000;
		do {
			string s1;
			for (int j = 0; j < SIZE(s); j += k)
				REP(i,k)
					s1.PB(s[j + p[i]]);
			int r = 1;
			REP(i,SIZE(s)-1)
				if (s1[i] != s1[i+1])
					r++;
			res <?= r;
		} while (next_permutation(p, p+k));
		cout << "Case #" << cc+1 << ": " << res << endl;
	}
}
