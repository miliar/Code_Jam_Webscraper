#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

typedef long long ll;

ll A1, A2, B1, B2;

int canwin(ll A, ll B) { // A - k * B
	if(A == B) return false;
	if(B > A) return canwin(B, A);
	if(A >= 2 * B) return true;
	for(ll k = 1; B * k <= A; ++k) {
		if(!canwin(A - k * B, B)) return 1;
	}
	return 0;
}

int main() {
	int T; cin >> T;
	for(int tt = 1; tt <= T; ++tt) {
		cin >> A1 >> A2 >> B1 >> B2;
		ll ans = 0;
		for(ll a = A1; a <= A2; ++a) {
			// if(B1 <= a / 2) ans += (min(B2, a / 2) - B1 + 1);
			// if(B2 >= a * 2) ans += (B2 - max(B1, a * 2) + 1);
			// cout << " a=" << a << " ans=" << ans << endl;
			for(ll b = B1; b <= B2; ++b) {
				if(canwin(a, b)) ans++;
			}
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}

