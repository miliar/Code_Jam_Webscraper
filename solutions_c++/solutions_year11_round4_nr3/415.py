#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define REP(i, n) for (int i(0), _n(n); i!=_n; ++i)
#define CL(v, x) memset((v), (x), sizeof(v))
#define SZ(v) (int)((v).size())

// Definition goes here
bool prime[2000000];

void init() {
	CL(prime, 1);
	for (int i=2; i<=2000000; ++i) if (prime[i]) {
		for (int j=i+i; j<=2000000; j+=i) prime[j] = 0;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	
	init();
	REP(t, T) {
		// add code here
		ll n;
		scanf("%lld", &n);
		
		ll a = 0, b = 0;
		ll ed = min((ll)2000000, n);
		for (ll i=2; i<=ed; ++i) if (prime[i]){
			++a;
			
			ll now = n;
			while (now >= i) {
				++b;
				now /= i;
			}
		}
		if (a == 0) a += 1;
		b += 1;
//		printf("%d %d\n", a, b);
		
		cout << "Case #" << t + 1 <<": " << b - a << endl;
		// printf solution here		
	}
	
	return 0;
}