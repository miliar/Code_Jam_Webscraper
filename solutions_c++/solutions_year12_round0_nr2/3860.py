#include<iostream>
#include<cstdio>
#include<map>
#define db(a) \
cout << #a << " = " << a << endl
#define db2(a, b) \
cout << #a << " = " << a << " " << #b << " = " << b << endl
#define inf (1<<30)
#define foreach(it, m) \
for (typeof(m.begin()) it = m.begin(); it != m.end(); it++)
using namespace std;
int main() {
	freopen("in.in", "r", stdin);
	freopen("ou.out", "w", stdout);
	int t, n, s, p, val, res;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		scanf("%d", &s);
		scanf("%d", &p);
		res = 0;
		int least = 3 * p - 2;
		int or_least = 3 * p - 4;
		if (p == 1) or_least = least;
		for (int j = 0; j < n; j++) {
			scanf("%d", &val);
			if (val >= least) res++;
			else if (val >= or_least && s) res++, s--;
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}
