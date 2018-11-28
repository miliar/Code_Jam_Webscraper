#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
using namespace std;

char flag[2000001];

long long getCount(int n, int a, int b, int m) {
	int x, y;
	vector< int > V;
	do {
		V.push_back(n);
		x = n / m;
		y = n % m;
		n = y * 10 + x;
	} while(V[0] != n);
	for(y = x = 0; x < V.size(); x++) {
		if(V[x] / m > 0 && V[x] >= a && V[x] <= b) {
			y++;
			flag[V[x]] = 1;
		}
	}
	return y * (y - 1) / 2;
}

int main() {
	int test, cs, a, b, m, i;
	long long ans;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf("%d", &test);
	for(cs = 1; cs <= test; cs++) {
		scanf("%d %d", &a, &b);
		memset(flag, 0, sizeof flag);
		m = (int)pow(10.0, floor(log10((double)a)));
		ans = 0;
		for(i = a; i <= b; i++) {
			if(!flag[i]) ans += getCount(i, a, b, m);
		}
		printf("Case #%d: %lld\n", cs, ans);
	}
	return 0;
}