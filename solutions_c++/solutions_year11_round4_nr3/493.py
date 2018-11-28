#include <stdio.h>
#include <assert.h>
#include <string.h>

int v_p (int n, int p, int cur) {
    if (cur > n)
	return 0;
    return v_p(n, p, cur*p) + 1;
}

int main (void) {
    int T;
    int scanned = scanf("%d", &T);
    bool is_prime[100];
    int pr[100];
    memset(is_prime, true, 100 * sizeof(bool));
    int np = 0;
    for (int i = 2; i < 100; ++i) {
	if (is_prime[i]) {
	    for (int j = i*i; j < 100; j += i)
		is_prime[j] = false;
	    pr[np] = i;
	    ++np;
	}
    }
    
    for (int currentcase = 1; currentcase <= T; ++currentcase) {
	int n;
	scanf("%d", &n);
	int nump = 0, max = 0;
	for (int i = 0; i < np; ++i) {
	    int p = pr[i];
	    int vp = v_p(n, p, p);
	    if (vp != 0)
		++nump;
	    max += vp;
	}
	printf("Case #%d: %d\n", currentcase, (nump == 0) ? 0 : (max - nump + 1));
    }
    return 0;
}
