#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

int t, len, pow_10, A, B;
set<pair<int, int> > res;

int length_of(int x) {
	int res = 0;
	while (x) {
		res++;
		x /= 10;
	}
	return res;
}

int main () {
	scanf("%d", &t);
	for (int tt=1; tt<=t; tt++) {
		scanf("%d %d", &A, &B);
		len = length_of(A);
		pow_10 = pow10(len-1);
		for (int n=A; n<=B; n++) {
			int x = n;
			for (int i=0; i<len; i++) {
				x = (x*10 + x/pow_10) % (pow_10*10);
				if (x > n && x <= B) {
					res.insert(make_pair(n, x));
				}
			}
		}
		printf("Case #%d: %d\n", tt, res.size());

		res.clear();
	}
}
