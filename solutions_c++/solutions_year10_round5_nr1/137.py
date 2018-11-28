#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <queue>
#include <map>
#include <sstream>
#include <string>

using namespace std;

typedef long long ll;
typedef stringstream sstream;

#define fn(i,n)	for (int i = 0; i < n; ++i)

#define filename "A-large"

ll primes[1024 * 1024];
int s[1024];

int mod_pow (ll a, ll p, ll m) {
	ll res = 1;
	while (p) {
		if (p & 1) {
			res = res * a % m;
			--p;
		} else {
			a = a * a % m;
			p >>= 1;
		}
	}
	return res;
}

int main()
{
	freopen (filename ".in", "rt", stdin);
	freopen (filename ".out", "wt", stdout);

	int pn = 1;
	primes[0] = 2;
	for (int p = 3; p < 1000000; p += 2) {
		bool prime = true;
		for (int i = 3; i*i <= p; i += 2)
			if (p % i == 0) {
				prime = false;
				break;
			}
		if (prime)
			primes[pn++] = p;
	}

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		int d, k;
		cin >> d >> k;
		int border = mod_pow (10, d, 1000000000);
		
		bool ok = true;
		int next = -1;
		if (k == 1) {
			cin >> next;
			ok = false;
		} else if (k == 2) {
			cin >> s[0] >> s[1];
			if (s[0] == s[1])
				next = s[0];
			else
				ok = false;
		} else {
			int max_s = -1;
			for (int i = 0; i < k; ++i) {
				cin >> s[i];
				if (s[i] > max_s) max_s = s[i];
			}
			if (s[0] == s[1])
				next = s[0];
			else {
				int pi;
				for (pi = 0; pi < pn; ++pi) {
					if (primes[pi] > max_s)
						break;
				}
				for (; pi < pn && primes[pi] < border && ok; ++pi) {
					ll a, b;
					ll &pp = primes[pi];
					a = (s[1] - s[2] + pp) * mod_pow(s[0] - s[1] + pp, pp - 2, pp) % pp;
					b = (pp * pp + s[1] - s[0] * a) % pp;

					bool check = true;
					for (int i = 1; i < k; ++i)
						if ((pp * pp + s[i-1]*a + b) % pp != s[i])
							check = false;
					int next_ = (pp * pp + s[k-1]*a + b) % pp;
					if (check) {
						if (next == -1)
							next = next_;
						else if (next != next_)
							ok = false;
					}
				}
				if (next == -1) ok = false;
			}
		}

		cout << "Case #" << test << ": ";
		if (ok)
			cout << next << endl;
		else
			cout << "I don't know." << endl;
	}

	return 0;
}