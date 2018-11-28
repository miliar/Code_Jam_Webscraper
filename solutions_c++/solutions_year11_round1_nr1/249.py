#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#define out(v) cout << #v << ": " << (v) << endl
using namespace std;
typedef long long LL;

int T;
LL N, PD, PG;
LL gcd(LL m, LL n) { return n ? gcd(n, m % n) : m; }

bool judge() {
	if (PD == 0) {
		if (PG == 100) return false;
		return true;
	}
	LL Dp = 100 / gcd(100, PD);
	//LL WD = PD * Dp / 100, LD = Dp - WD;
	if (PG == 0) return false;
	LL Gp = 100 / gcd(100, PG);
	if (Dp <= N && (PG < 100 || PG == 100 && PD == 100)) return true;
	return false;
}

int main() {
	cin >> T;
	for (int id = 1; id <= T; ++id) {
		cin >> N >> PD >> PG;
		string ans = judge() ? "Possible" : "Broken";
		cout << "Case #" << id << ": " << ans << endl;
	}
	return 0;
}
