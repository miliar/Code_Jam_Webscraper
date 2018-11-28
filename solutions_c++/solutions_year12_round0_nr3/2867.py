//#include <stdafx.h>

#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <set>
using namespace std;

int f(int a, int b) {
	int k1 = 1;
	int k2 = 1;
	while (k1 < a) k1 *= 10;
	k2 *= 10;
	k1 /= 10;
	int ans = 0;
	set<int> s;
	while (k2 < a) {
		int next = (a % k2) * k1 + a / k2;
		if (next > a && next <= b && s.insert(next).second) ans++;
		k2 *= 10;
		k1 /= 10;
	}
	return ans;
}

int main() {
	//freopen("D:\\a.in", "r", stdin);
	//freopen("D:\\a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; I++) {
		int a, b;
		scanf("%d%d", &a, &b);
		int ans = 0;
		for (int i = a; i <= b; i++) {
			ans += f(i, b);
		}
		printf("Case #%d: %d\n", I + 1, ans);
	}
}