#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>

#define INF 1000000000
#define EPS 1E-8
#define PI 3.14159265358979

using namespace std;

typedef long long ll;

int mod_pow(int a, int n, int p) {
	int res = 1;
	for(; n; n >>= 1) {
		if(n & 1) res = (ll)res * a % p;
		a = (ll)a * a % p;
	}
	return res;
}

int primes[10000000];
int isprime[10000000];
int ps[10];

int ar[20];

int norm(ll a, int p) {
	return (a % p + p) % p;
}

int calc(int p, int n) {
	int rev = mod_pow(norm(ar[1] - ar[0], p), p - 2, p);
	int A = (ll) rev * norm(ar[2] - ar[1], p) % p;
	int B = norm(ar[1] - (ll) A * ar[0] % p, p);
	bool ok = true;
	for(int i = 0; i < n - 1; ++i) {
		if(norm((ll)ar[i] * A + B, p) != ar[i + 1]) return -1;
	}
	return norm((ll)ar[n - 1] * A + B, p);
}

int main() {
	int N, pn = 0;
	for(int i = 2; i < 10000000; ++i) if(!isprime[i]){
		primes[pn++] = i;
		for(int j = 2 * i; j < 10000000; j += i) isprime[j] = 1;
	}
	cin >> N;
	ps[0] = 1;
	for(int i = 1; i < 10; ++i) ps[i] = ps[i - 1] * 10;
	for(int t = 0; t < N; ++t) {
		printf("Case #%d: ", t + 1);
		int d, n;
		cin >> d >> n;
		for(int i = 0; i < n; ++i) cin >> ar[i];
		if(n == 1) puts("I don't know.");
		else {
			int same = -1;
			for(int i = 0; i < n - 1; ++i) if(ar[i] == ar[n - 1]) same = i;
			if(same != -1) printf("%d\n", ar[same + 1]);
			else if(n == 2) puts("I don't know.");
			else {
				int res = -1;
				bool no = false;
				for(int i = 0; i < pn && primes[i] <= ps[d]; ++i) {
					bool ok = true;
					for(int j = 0; j < n; ++j) if(ar[j] >= primes[i]) ok = false;
					if(!ok) continue;
					int r = calc(primes[i], n);
					if(r == -1) continue;
					if(res != -1 && r != res) no = true;
					else if(res == -1) res = r;
				}
				if(res == -1) cerr << "error" << endl;
				if(no || res == -1) puts("I don't know.");
				else printf("%d\n", res);
			}
		}
	}
	return 0;
}
