


/*
	Prob: (Google code jam 2011 - Round 1A - A)
	Author: peanut
	Time: 21/05/11 09:12
	Description: >_<
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

long long N, T;

long long gcd(long long x, long long y) {
	return y == 0 ? x : gcd(y, x % y);
}

bool check() {
	long long Pd, Pg;
	cin >> N >> Pd >> Pg;
	if (Pg == 100 && Pd < 100) return false;
	if (Pg ==   0 && Pd >   0) return false;
	long long Pc = 100 / gcd(Pd, 100);
	if (N >= Pc) return true;
	else return false;
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	cin >> T;
	for (int cs = 1; cs <= T; ++ cs) {
		printf("Case #%d: ", cs);
		if (check()) puts("Possible");
		else puts("Broken");
	}
	
	return 0;
}
