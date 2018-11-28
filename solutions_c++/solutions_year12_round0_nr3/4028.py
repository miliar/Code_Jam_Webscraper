#include <algorithm>
#include <cmath>
#include <cstring>
#include <cctype>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(c) (c).begin(),(c).end()
#define TRACE(x) cerr << "TRACE(" #x ")" << endl;
#define DEBUG(x) cerr << #x << " = " << x << endl;

typedef long long ll;
typedef long double ld;
typedef unsigned long ulong;
typedef unsigned long long ull;

int ten[10];
int v[6] = { 0, };

int f(int num, int a) {
	memset(v, (char)0, sizeof(v));
	int N = 0;
	int n = 0, res = 0;
	for (int x = num; x; x /= 10)
		++n;
	//cerr << num << ":";
	FOR(i,1,n-1) {
		int x = (num%ten[i])*ten[n-i]+num/ten[i];
		//cerr << " " << x;
		if (x < num && a <= x) {
			bool mod = true;
			REP(j,N)
				if (v[j] == x) {
					mod = false;
					break;
				}
			if (mod) {
				v[N++] = x;
				++res;
			}
		}
	}
	//cerr << endl;
	return res;
}

int main() {
	ten[0] = 1;
	FOR(i,1,9)
		ten[i] = ten[i-1] * 10;
	
	int tnum;
	scanf("%d", &tnum);
	REP(ti,tnum) {
		int res = 0, a, b;
		scanf("%d%d", &a, &b);
		FOR(k,a,b)
			res += f(k, a);
		printf("Case #%d: %d\n", 1+ti, res);
	}
	return 0;
}