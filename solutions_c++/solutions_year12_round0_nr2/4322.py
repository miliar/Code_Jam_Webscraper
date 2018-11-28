#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main()
{
	freopen("/1/1.in", "r", stdin);
	freopen("/1/1.out", "w", stdout);
	int T;
	scanf("%d\n", &T);
	for (int T1 = 1; T1 <= T; ++T1) {
		printf("Case #%d: ", T1);
		int n, s, p, a, ans = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a);
			int x = a/3; a -= x;
			int y = a/2; a -= y;
			int z = a;
			if (z >= p) ++ans;
			else if (s) {
				if (y==z && y>=1) {
					if (z+1 >= p) {
						++ans;
						--s;
					}
				}
			}
		}
		printf("%d\n", ans);
	}
}
