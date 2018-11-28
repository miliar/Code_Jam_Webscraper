#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
#define forn(i,n) for(int i=0; i<(n); i++)

long long gcd(long long a, long long b) {
	return b == 0 ? a : gcd(b, a % b);
}
bool solve(long long n, long long pd, long long pg) {
	long long md = gcd(100LL, pd);
	long long d = 100LL/md;
	if(d > n) return false;
	if(pd!=100 && pg ==100) return false;
	if(pg==0 && pd != 0) return false;
	return true;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int ncase; cin >> ncase;
	forn(icase, ncase) {
		long long n, pd, pg;
		cin >> n >> pd >> pg;
		printf("Case #%d: %s\n", icase+1, solve(n,pd,pg)?"Possible":"Broken");
		
	}
}
