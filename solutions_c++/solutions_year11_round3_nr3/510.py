
#include <stdio.h>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>

#define D if(1)

using namespace std;

int n, l, h, g, a[10001];

int gcd(int a, int b) {
	return b ? gcd(b, a % b) : a;
}

int main(int argc, char const* argv[])
{
	int case_count;
	scanf("%d", &case_count);
	for (int case_index = 0; case_index < case_count; case_index++) {
		printf("Case #%d: ", case_index + 1);
		scanf("%d%d%d", &n, &l, &h);

		for (int i = 0; i < n; i++) {
			scanf("%d", a + i);
		//	if (i == 0) g = a[0]; else g = gcd(g, a[i]);
		}
		// find x in [l,h], subset of g's primers
		int res = -1;
		for (int i = l; i <= h; i++) {
			// test i
			bool ok = true;
			for (int j = 0; j < n; j++) {
				if (i % a[j] != 0 && a[j] % i != 0) {
					ok = false;
					break;
				}
			}
			if (ok) {
				res = i;
				break;
			}
		}
		if (res == -1) puts("NO");
		else printf("%d\n", res);


	}
	
	return 0;
}
