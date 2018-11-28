#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

/* Prewritten code begins */
#define LL          long long
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,a,b)  for(int i=(a); i<=(b); ++i)
/* Prewritten code ends */

int p10[] = {1,10,100,1000,10000,100000,1000000,10000000};
int a[1000];
inline int rev(int a, int p) {
	int n = p-2, r = 1; 
	a %= p;
	while(n) {
		if(n&1) r = (LL)r*a%p;
		a = (LL)a*a%p;
		n >>= 1;
	}
	return r;
}
int gcd(int a, int b) { return b?gcd(b,a%b):a; }
inline int isPrime(int x) {
	if(x%2==0) return x == 2;
	if(x<2) return 0;
	for(int i=3;i*i<=x;i+=2) if(x%i==0) return 0;
	return 1;
}
inline int mod(LL x, int p) {
	if(x<0) return (p-(-x)%p)%p;
	return x%p;
}
#define FAIL { printf("I don't know.\n"); return; }
void fff() {
	int D, K;
	cin >> D >> K;
	REP(i,K) cin >> a[i];
	if(K == 1) FAIL
	if(count(a,a+K,a[0])==K) { printf("%d\n",a[0]); return; }
	if(K == 2) FAIL
	int cand = -1;
	FOR(p,*max_element(a,a+K)+1,p10[D]) if(isPrime(p)) {
		int b = -1, aa, c1, c2, t;
		FOR(i,2,K-1) {
			c1 = mod((LL)a[i-1]*a[i-1]-(LL)a[i-2]*a[i],p), c2 = mod(a[i-1]-a[i-2],p);
			if(c2 != 0) {
				t = mod((LL)c1 * rev(c2,p),p);
				if(b<0) b = t; else if(b != t) goto C;
			} else if(c1 != 0) goto C;
		}
		if(b != -1) {
			aa = -1; int tt;
			FOR(i,1,K-1) {
				int t1 = mod(a[i]-b,p), t2 = a[i-1];
				if(t2 != 0) {
					tt = mod((LL)t1*rev(t2,p),p);
					if(aa<0) aa = tt; else if(aa != tt) goto C;
				}
			}
		} else aa = -1;
		FOR(A,aa<0?0:aa,aa<0?p-1:aa) {
			t = mod(a[1]-(LL)A*a[0],p);
			if(b != -1 && t != b) goto D;
			FOR(i,2,K-1) if(mod(a[i]-(LL)A*a[i-1],p)!=t) goto D;
		   	t = mod((LL)A*a[K-1]+t,p);
			if(cand < 0) cand = t; else if(cand != t) FAIL	
D:;		}
C:;	}
/*	REP(A,p) {
		int b = mod(a[1]-A*a[0],p);
		FOR(i,2,K-1) if(mod(a[i-1]*A+b,p)!=a[i]) goto C;
		t = mod(a[K-1]*A+b,p);
		if(cand == -1) cand = t; else if(cand!=t) FAIL
C:;	}*/
	printf("%d\n",cand);
}
int main() {
	int T;
	scanf("%d",&T);
	FOR(cs,1,T) printf("Case #%d: ",cs),fff();
	return 0;
}
