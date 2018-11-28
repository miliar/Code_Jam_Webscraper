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

int n, k;
int T, I;

void input() {
	scanf("%d %d", &n, &k);
}

void solve() {
	k %= (1 << n);
}

void output() {
	printf("Case #%d: ", I + 1);
	if (k == (1 << n) - 1)
		printf("ON\n");
	else
		printf("OFF\n");
}

int main() {
	scanf("%d", &T);
	for (I = 0; I < T; ++I) {
		input();
		solve();
		output();
	}
	return 0;
}

