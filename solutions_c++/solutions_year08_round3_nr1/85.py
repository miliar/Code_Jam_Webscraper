#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>

using namespace std;

int T, p, k, l;
int f[2000];

int main() {
	freopen("alarge.in", "r", stdin);
	freopen("alarge.out", "w", stdout);
	scanf("%d", &T);
	for (int e = 0; e < T; e++) {
		scanf("%d %d %d", &p, &k, &l);
		for (int i = 0; i < l; i++) 
			scanf("%d" , &f[i]);
		sort(f, f + l);
		int kel = 1;
		long long suma = 0;
		for (int r = l - 1; r >= 0; r--) {
			int e = l - r;
			int w = e / k;
			if (e % k != 0) w++;
			suma += w * f[r];
		}
		printf("Case #%d: %lld\n", e + 1, suma);
	}
	return 0;
}