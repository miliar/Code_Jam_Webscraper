#define _CRT_SECURE_NO_DEPRECATE

#include <stdint.h>
#include <climits>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;

//#include <gmpxx.h>
//typedef mpz_class mpz;
//typedef mpq_class mpq;
//typedef mpf_class mpf;

//mpz int64_to_mpz(int64_t x) { return (mpz(int32_t(x >> 32)) << 32) | mpz(uint32_t(x & 0xFFFFFFFF)); }
//int64_t mpz_to_int64(mpz x) { mpz xh = x >> 32, xl = x & 0xFFFFFFFF; return (int64_t(xh.get_si()) << 32) | uint64_t(xl.get_ui()); }
//int is_prime(int64_t x, int iter = 8) { return mpz_probab_prime_p(int64_to_mpz(x).get_mpz_t(), iter); }
//int64_t next_prime(int64_t x) { mpz p; mpz_nextprime(p.get_mpz_t(), int64_to_mpz(x).get_mpz_t()); return mpz_to_int64(p); }
//int64_t sq(int32_t x) { return int64_t(x)*x; }
//int32_t isqrt(int64_t x) { int32_t q = int32_t(sqrt(double(x))); if (sq(q) > x) q--; if (q < _I32_MAX && sq(q+1) <= x) q++; return q; }
//int32_t isqrtc(int64_t x) { int32_t q = int32_t(ceil(sqrt(double(x)))); if (sq(q) < x) q++; if (q > 0 && sq(q-1) >= x) q--; return q; }
//int is_square(int64_t x) { return (sq(isqrt(x)) == x); }
//mpz z_pow(mpz x, int n) { mpz r; mpz_pow_ui(r.get_mpz_t(), x.get_mpz_t(), n); return r; }
//int f_int(mpf x) { return mpf_get_si(x.get_mpf_t()); }
//mpf f_sqrt(int n) { mpf r; mpf_sqrt_ui(r.get_mpf_t(), n); return r; }
//mpf f_abs(mpf x) { mpf r; mpf_abs(r.get_mpf_t(), x.get_mpf_t()); return r; }
//mpf f_floor(mpf x) { mpf r; mpf_floor(r.get_mpf_t(), x.get_mpf_t()); return r; }
//template<typename T> T sq(T x) { return x * x; }

#define SZ 1024
pii p[SZ];
pii s[SZ];

int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, w, h; scanf("%d %d %d", &n, &w, &h);
		for (int i = 0; i < n; i++)
			scanf("%d", &p[i].first), p[i].second = i;
		sort(p, p + n, std::greater<pii>());
		swap(w, h); // solved in two runs, first with original dimension, second with swapped!, manuali integrated
		
		int r0 = p[0].first;
		s[p[0].second] = pii(0, 0);
		vector<pii> vb;
		vb.push_back(pii(-r0, +r0));
		vb.push_back(pii(+r0, -r0));

		for (int i = 1; i < n; i++) {
			int r = p[i].first;
			int k;
			for (k = 0; k < (int) vb.size(); k++) {
				if (vb[k].first + r <= w &&
					vb[k].second + r <= h)
					break;
			}
			if (k >= (int) vb.size()) {
				printf("Case #%d: ERROR\n", t);
				break;
			}
			
			vector<pii> vbn;
			pii vb_k = vb[k];
			vb_k.first = max(vb_k.first, -r);
			vb_k.second = max(vb_k.second, -r);
			int y0 = 2000000000;
			for (int j = 0; j <= k; j++) {
				vb[j].second = max(vb[j].second, vb_k.second + 2 * r);
				if (vb[j].second < y0) vbn.push_back(vb[j]);
				y0 = vb[j].second;
			}
			vb[k] = vb_k;
			int x0 = -1;
			for (int j = k; j < (int) vb.size(); j++) {
				vb[j].first = max(vb[j].first, vb_k.first + 2 * r);
				if (vb[j].first > x0) vbn.push_back(vb[j]);
				vbn.back() = vb[j];
				x0 = vb[j].second;
			}
			vb.swap(vbn);
			
			s[p[i].second] = pii(vb_k.first + r, vb_k.second + r);
		}
		printf("Case #%d: ", t);
		for (int i = 0; i < n; i++) {
			//printf("%d %d ", s[i].first, s[i].second);
			printf("%d %d ", s[i].second, s[i].first);
		}
		printf("\n");
	}
	return 0;
}
