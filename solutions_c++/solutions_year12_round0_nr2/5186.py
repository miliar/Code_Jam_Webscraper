#include <iostream>
#include <cstdio>

using namespace std;

const int MXN = 37;

int n, s, p;
int a[MXN], b[MXN];
int t[MXN];

int main()
{
	for (int i = 2; i <= 30; ++i) {
		a[i] = (i - 1) / 3 + 1;
		b[i] = (i - 2) / 3 + 2;
	}
	int T;
	scanf("%d", &T);
	for (int numCase = 1; numCase <= T; ++numCase) {
		int ans = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (int i = 0; i < n; ++i) {
			scanf("%d", t + i);
			if (a[t[i]] >= p) {
				++ans;
			} else if (b[t[i]] >= p) {
				if (s > 0) {
					++ans;
					--s;
				}
			}
		}
		printf("Case #%d: %d\n", numCase, ans);
	}
}
