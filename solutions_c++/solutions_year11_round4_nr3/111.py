#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
using namespace std;

#define FOR(i,a,b) for(int i=(a); i<(int)(b); ++i)
#define ALL(a) (a).begin(),(a).end()
#define PB(a) push_back(a)
#define MP(a,b) make_pair((a),(b))
#define sqr(a) ((a)*(a))
typedef long long i64;
typedef unsigned long long u64;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

long long nextLong() {
	long long x;
	scanf("%I64d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

const int BUFSIZE = 1000000;
char buf[BUFSIZE + 1];
string nextString() {
	scanf("%s", buf);
	return buf;
}

int gcd(long long a, long long b) {
	return b == 0 ? a : gcd(b, a % b);
}

int calls(vector<int> a) {
	int res = 1;
	long long lcm = a[0];
	for (int i = 1; i < a.size(); ++i) {
		if (lcm % a[i]) {
			lcm = lcm / gcd(lcm, a[i]) * a[i];
			++res;
		}
	}
	return res;
}

long long fact(int n) {
	return n <= 1 ? 1 : n * fact(n - 1);
}

void brute(int n) {
	vector<int> a(n);
	for (int i = 0; i < n; ++i) {
		a[i] = i + 1;
	}
	int mn = INT_MAX, mx = -1;
	int run = 0;
	do {
		int c = calls(a);
		if (run == 0 || run == fact(n) - 1) {
			for (int i = 0; i < a.size(); ++i) {
				cout << a[i] << " ";
			}
			cout << " : " << c << endl;
		}
		mn = min(mn, c);
		mx = max(mx, c);
		++run;
	} while (next_permutation(a.begin(), a.end()));
	cout << mn << " " << mx << endl;
}

bool isPrime(long long x) {
	for (long long i = 2; i * i <= x; ++i) {
		if (x % i == 0) {
			return false;
		}
	}
	return true;
}

bool isPrimePow(long long x) {
	for (long long i = 2; i * i <= x; ++i) {
		if (x % i == 0) {
			while (x % i == 0) {
				x /= i;
			}
			return x == 1;
		}
	}
	return true;
}

long long solveMaxBrute(long long n) {
	int res = 1;
	for (long long p = 2; p <= n; ++p) {
		if (isPrime(p)) {
			long long x = p;
			while (x <= n) {
				++res;
				x *= p;
			}
		}
	}
	return res;
}

long long solveMinBrute(long long n) {
	if (n == 1) {
		return 1;
	}
	int res = 0;
	for (long long p = 2; p <= n; ++p) {
		if (isPrime(p)) {
			++res;
		}
	}
	return res;
}

long long solveMax(long long n) {
	return solveMaxBrute(n);
}

long long solveMin(long long n) {
	return solveMinBrute(n);
}

long long solve(long long n) {
	long long mx = solveMax(n); 
	long long mn = solveMin(n);
	return mx - mn;
}

int P;
int primes[1000000];

long long solveFast(long long n) {
	if (n == 1) {
		return 0;
	}
	int res = 1;
	for (int i = 0; i < P; ++i) {
		long long p = primes[i];
		if (p * p > n) {
			break;
		}
		long long x = p;
		while (x <= n) {
			++res;
			x *= p;
		}
		--res;
	}
	return res;
}

int main() {
	P = 0;
	for (int i = 2; i <= 1000000; ++i) {
		if (isPrime(i)) {
			primes[P++] = i;
		}
	}
	//for (int i = 1; i <= 10000; ++i) {
	//	if (solve(i) != solveFast(i)) {
	//		cout << "!";
	//		return 0;
	//	}
	//	if (i % 1000 == 0) {
	//		cout << i << endl;
	//	}
	//}
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		long long n = nextLong();
		//brute(n);
		//cout << endl;
		long long res = solveFast(n);
		cerr << cas << endl;
		printf("Case #%d: %I64d\n", cas, res);
	}
	return 0;
}
