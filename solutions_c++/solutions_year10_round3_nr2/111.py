#include <cstdlib>
#include <iostream>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

int T;
int L, P;
long long C;

int solve(long long a, long long b)
{
	if (b <= a * C) return 0;
	
	int ret = INT_MAX;
	double da = a;
	double db = b;
	double la = log(a) / log(C);
	double lb = log(b) / log(C);
	int x = pow(C, (la + lb) / 2);
	
	//printf("%I64d, %I64d -> la = %f, lb = %f, x = %d\n", a, b, la, lb, x);
	if (x != a) ret = min(ret, max(solve(a, x), solve(x, b) ) + 1);
	if (x + 1 != b) ret = min(ret, max(solve(a, x + 1), solve(x + 1, b) ) + 1);
	
	return ret;
}

int main(int argc, char *argv[])
{
	cin >> T;
	
	int ans;
	
	for (int i = 0; i < T; ++i) {
		cin >> L >> P >> C;
		ans = solve(L, P);
		printf("Case #%d: %d\n", i + 1, ans);
	}
	
    return EXIT_SUCCESS;
}
