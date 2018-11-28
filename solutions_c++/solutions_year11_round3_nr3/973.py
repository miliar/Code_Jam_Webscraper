#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int cmp(const void *a, const void *b)
{
	return *(int*) a < *(int*) b ? -1 : 1;
}

int GCD(int a, int b) {
	int r;
	while (b > 0) { r = a % b; a = b; b = r; }
	return a;
}

#define MAX 105

int num[MAX];

int main()
{
	int kase, serial=1,
		n, low, high,
		soln;

	scanf("%d", &kase);
	while (kase--) {
		// begin test case
		scanf("%d %d %d", &n, &low, &high);

		for (int i=0; i<n; ++i) {
			scanf("%d", num+i);
		}

		soln = -1;
		for (int s = low; s <= high; ++s) {

			bool ok = true;
			for (int i=0; i<n; ++i) {
				if (! (s % num[i] == 0 || num[i] % s == 0)) {
					ok = false;
					break;
				}
			}

			if (ok) {
				soln = s;
				break;
			}
		}

		printf("Case #%d: ", serial++);
		if (soln > 0) printf("%d\n", soln);
		else puts("NO");

		// end test case
	}
	return 0;
}
