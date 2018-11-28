#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <cassert>
#include <queue>
#include <cctype>
using namespace std;

typedef long double Real;

const Real o = 1e-8;
const Real pi = acos(-1.0);

const int max_n = 16;

int T, I;
int s[max_n];
vector<pair<int, int> > ans;
int res;
int d, k, D;

void input() {
	scanf("%d %d", &d, &k);
	for (int i = 0; i < k; i++)
		scanf("%d", &s[i]);
}

bool is_prime(int a) {
	for (int i = 2; i * i <= a; i++) {
		if (a % i == 0)
			return false;
	}
	return true;
}

long long gcd(long long a, long long b, long long &x, long long &y){
    long long t, ret;
    if (!b) {
        x = 1;
		y = 0;
        return a;
    }
    ret = gcd(b, a % b, x, y);
    t = x;
	x = y;
	y = t - a / b * y;
    return ret;
}

int linear_solve(long long a, long long b, long long p) {
	long long d, e, x, y;
    d = gcd(a, p, x, y);
	assert(d == 1);
    e = (x % p) * (b % p) % p + p;
    return e % p;
}

void solve() {
	if (k == 1) {
		res = -1;
		return;
	}
	if (s[0] == s[1]) {
		res = s[0];
		return;
	}
	if (k == 2) {
		res = -1;
		return;
	}
	for (int i = 0; i + 1 < k; i++) {
		if (s[i] == s[i + 1]) {
			res = s[i];
			return;
		}
	}
	D = 1;
	for (int i = 0; i < d; i++)
		D *= 10;
	ans.clear();
	for (int p = 2; p <= D; p++) {
		if (!is_prime(p))
			continue;
		bool valid = true;
		for (int i = 0; i < k; i++) {
			if (s[i] >= p) {
				valid = false;
				break;
			}
		}
		if (!valid)
			continue;
		int a = -1;
		for (int i = 0; i + 2 < k; i++) {
			int x = linear_solve((s[i] - s[i + 1] + p) % p, (s[i + 1] - s[i + 2] + p) % p, p);
			if (a == -1)
				a = x;
			else if (x != a) {
				a = -1;
				break;
			}
		}
		if (a != -1) {
			ans.push_back(make_pair(p, a));
		}
	}

	res = -1;
	for (size_t j = 0, E = ans.size(); j < E; j++) {
		int p = ans[j].first, a = ans[j].second;
		int b = -1;
		for (int i = 0; i + 1 < k; i++) {
			int x = ((long long)s[i + 1] - (long long)a * s[i]) % p;
			while (x < 0)
				x += p;
			if (b == -1)
				b = x;
			else if (x != b) {
				b = -2;
				break;
			}
		}
		assert(b != -1);
		if (b < 0) // no b satisfies all
			continue;
		int next = ((long long)s[k - 1] * a + b) % p;
		if (res == -1)
			res = next;
		else if (res != next) {
			res = -2;
			break;
		}
	}
	assert(res != -1);
}

void output() {
	cerr << "!!!\n";
	if (res < 0)
		printf("Case #%d: I don't know.\n", I + 1);
	else
		printf("Case #%d: %d\n", I + 1, res);
}

int main() {
	scanf("%d", &T);
	for (I = 0; I < T; I++) {
		input();
		solve();
		output();
	}
	return 0;
}

