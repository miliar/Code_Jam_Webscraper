#include <cstdio>

using namespace std;

int main () {
	int tt;
	scanf ("%d", &tt);
	for (int it = 1; it <= tt; it++) {
		int n, k;
		scanf ("%d%d", &n, &k);	
		k %= (1 << n);
		if (k + 1 == (1 << n)) printf ("Case #%d: ON\n", it); else printf ("Case #%d: OFF\n", it);
	}
}