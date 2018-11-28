#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <cctype>
#include <cassert>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < (n); i++)
#define repr(i,b,e) for(int i = (b); i <= (e); i++)
#define INF (1001001001)
#define EPS (1e-15)

#define pr(x) do{cout << (#x) << " = " << (x) << endl;}while(0)
#define pri(x,i) do{cout << (#x) << "[" << i << "] = " << (x[i]) << endl;}while(0)
#define pra(x,n) rep(__i,n) pri(x,__i);
#define prar(x,b,e) repr(__i,b,e) pri(x,__i);

typedef long long llint;
typedef pair<int, int> pint;
typedef vector<int> vint;

int in() {
	int a;
	scanf("%d ", &a);
	return a;
}

#define SIZ 100010

bool furui[SIZ];
int primes[100000];
int nPrimes = 0;

int main() {
	// make primes
	rep(i, SIZ) furui[i] = true;
	furui[0] = furui[1] = false;
	for(int i = 2; i < SIZ; i++) {
		if(furui[i]) {
			primes[nPrimes++] = i;
			for(int k = i + i; k < SIZ; k += i) {
				furui[k] = false;
			}
		}
	}
	/*
	cout << "Successfully made primes. " << nPrimes << endl;
	return 0;
	*/
	int T = in();
	rep(tst, T) {
		printf("Case #%d: ", tst + 1);
		llint N;
		scanf("%lld", &N);
		
		if(N == 1) {
			cout << 0 << endl;
			continue;
		}
		
		llint ans = 1;
		rep(i, nPrimes) {
			int p = primes[i];
			llint hoge = p * p;
			if(hoge > N) break;
			
			int add = 0;
			while(hoge <= N) {
				add++;
				hoge *= p;
			}
			ans += add;
		}
		
		cout << ans << endl;
	}
	return 0;
}
