#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>

using namespace std;

#define Size(a) ((int)a.size())
int a[100];
char s[100];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ntests;
	scanf("%d", &ntests);
	for (int itest = 1; itest <= ntests; itest++) {
		printf("Case #%d: ", itest);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s", s);
			a[i] = 0;
			for (int j = 0; j < n; j++) {
				if (s[j] - '0') a[i] = j;
			}
		}
		int res = 0;
		for (int i = 0; i < n; i++) {
			int j;
			for (j = i; j < n; j++) {
				if (a[j] <= i) break;
			}
			for (int k = j - 1; k >= i; k--, res++) {
				swap(a[k], a[k + 1]);
			}
		}
		printf("%d\n", res);
	}
	return 0;
}