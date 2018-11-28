#include <iostream>
#include <cmath>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

ll n, pd, pg;

bool solve() {
	ll b = 100 / gcd(100, pd);
	if (b > n) return 0;
	if (pd == pg) return true;

	if (pd != pg && (pg == 0 || pg == 100)) return false;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);

    for (int tc = 1; tc <= tk; ++tc) {
    	printf("Case #%d: ", tc);


    	cin >> n >> pd >> pg;

    	if (solve()) cout << "Possible" << endl;
    	else cout << "Broken" << endl;
    }
	
	return 0;
}