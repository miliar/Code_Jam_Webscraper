


/*
	Prob: (Google code jam 2011 - Round 2 - B)
	Author: peanut
	Time: 04/06/11 22:10
	Description: Greedy
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MaxN = 1111111;

long long T, N, ans, k;
bool v[MaxN];

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	memset(v, 1, sizeof(v));
	v[1] = 0;
	for (int i = 2; i < MaxN; ++ i)
		if (v[i]) {
			for (int j = i + i; j < MaxN; j += i)
				v[j] = false;
		}
	cin >> T;
	for (int cs = 1; cs <= T; ++ cs) {
		cin >> N;
		ans = 0;
		for (k = 2; k * k <= N; ++ k)
			if (v[k]) {
				long long tmp = N;
				while (tmp >= k) {++ ans; tmp /= k;}
				-- ans;
			}
		printf("Case #%d: %d\n", cs, ans + (N != 1));
	}
	
	return 0;
}
