#include<iostream>
#include<vector>
using namespace std;

typedef long long ll;

int D, K, T, L;
ll data[16];

vector<ll> primes;
vector<bool> isp; //is this optimized??
void genprime(ll M) { //generates prime up until number (M+1)
	isp.assign(M + 1, true);
	for(ll i = 2; i <= M; i++) {
		if(isp[i]) {
			for(ll j = i * i; j < M; j += i) isp[j] = 0;
			primes.push_back(i);
		}
	}
}

inline ll mod(const ll& x, const ll& m) {
	return ((x % m) + m) % m;
}

ll egcd(ll a, ll b, ll& x, ll &y) {
	if (!b) { x = 1; y = 0; return a; }
	ll result = egcd(b, a%b, y, x);
	y -= x * (a/b);
	return result;
}

ll modinv(const ll& a, const ll& m) {
	if(a == 0) return 0;
	// ax + ym = 1
	ll x, y;
	ll g = egcd(a, m, x, y);
	if(g != 1) cerr << " egcd ERROR a=" << a << " m=" << m << " g=" << g << endl;
	return mod(x, m);
}

vector<ll> lim;
const string dun = "I don't know.";

int main() {
	ll p = 1;
	for(int d = 0; d <= 6; ++d) {
		lim.push_back(p);
		p *= 10;
	}
	genprime(2000000);
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> D >> K;
		ll maxima = 0;
		for(int k = 0; k < K; ++k) {
			cin >> data[k];
			maxima = max(maxima, data[k]);
		}
		ll ans = -1;
		if(K > 2) {
			L = lim[D];
			// cout << " L=" << L << " max=" << maxima << endl;
			for(int p = 0; primes[p] <= L; ++p) {
				if(primes[p] <= maxima) continue;
				// try p
				const ll m = primes[p];
				const ll s01 = mod(data[0] - data[1], m);
				const ll s12 = mod(data[1] - data[2], m);
				const ll is01 = modinv(s01, m);
				const ll A = (s12 * is01) % m;
				const ll B = mod(data[1] - A * data[0], m);
				bool okay = true;
				for(int i = 1; i < K; ++i) {
					ll t = (A * data[i-1] + B) % m;
					if(t != data[i]) {
						okay = false;
						break;
					}
				}
				// cout << " m=" << m << " A=" << A << " B=" << B << " " << okay << endl;
				if(okay) {
					// what's next??
					ll next = (A * data[K-1] + B) % m;
					if (ans == -1 || ans == next) {
						ans = next;
					} else {
						ans = -1;
						goto here;
					}
				}
			}
		} else if (K == 2) {
			for(int p = 0; primes[p] <= L; ++p) {
				if(primes[p] <= maxima) continue;
				if(data[0] == data[1]) {
					ans = data[0];
					break;
				}
			}
		}
here:
		if (ans == -1) {
			cout << "Case #" << tt << ": " << dun << endl;
		} else {
			cout << "Case #" << tt << ": " << ans << endl;
		}
	}
	return 0;
}

