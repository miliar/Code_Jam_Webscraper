#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int a[1000];
int b[1000];

int main()
{
	int t;
	int i, j, k;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		int n;
		int ans = 0;
		scanf("%d", &n);
		for (j = 0; j < n; j++) {
			scanf("%d %d", &a[j], &b[j]);
			for (k = 0; k < j; k++) {
				ans+=(a[j] < a[k] && b[j] > b[k]) || (a[j] > a[k] && b[j] < b[k]);
			}
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
}