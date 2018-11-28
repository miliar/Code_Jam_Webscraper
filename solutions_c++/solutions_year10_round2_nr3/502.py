#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstring>

#define MOD 100003

using namespace std;

typedef long long ll;

ll binom(int a, int b) {
	ll res=1;
	int i;
	if (a == b) return 1;
	if (a < b)
		return 0;
	for(i = a-b+1; i<=a; ++i) {
		res = (res * i);
	}
	for(i = 1; i<=b; ++i) {
		res /= i;
	}
	return res % MOD;
}

ll dyn[32][32];

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	ll T, NT, n, i, j, k, l, cur, curS;
	cin>>NT;
	memset(dyn, 0, sizeof(dyn));
	for(i = 2; i <= 25; ++i) {
		curS = 1;
		dyn[i][1] = 1;
		for(j = 2; j < i; ++j) {
			cur = 0;
			for(k = 1; k < j; ++k) {
				cur += dyn[j][k] * binom(i-j-1, j-k-1);
			}
			dyn[i][j] = cur;
			curS = (curS + cur) % MOD;
		}
		dyn[i][0] = curS;
	}
	for(T = 1; T <= NT; ++T) {
		cin>>n;
		cout<<"Case #"<<T<<": "<<dyn[n][0]<<endl;
	}
	return 0;
}