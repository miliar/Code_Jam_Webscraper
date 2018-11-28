#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
typedef long long ll;

ll N, PD, PG;

int solve() {
	scanf("%lld%lld%lld", &N, &PD, &PG);
	int b = 100 / __gcd(100LL, PD);
	if (N < b) return 0;
	if (PG == 100) return PD == 100;
	if (PG == 0) return PD == 0;
	return 1;
}

int main() {
	int case_n; scanf("%d", &case_n);
	for (int case_x = 1; case_x <= case_n; case_x++)
	  printf("Case #%d: %s\n", case_x, solve() ? "Possible" : "Broken");
	return 0;
}
