#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int main(int argc, char *argv[])
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t, cn, n, k, i;
	bool on;
	scanf("%d", &t);
	for (cn=1; cn<=t; ++cn)
	{
	    scanf("%d%d", &n, &k);
	    on = true;
	    for (i=0; i<n; ++i) {
            if (!(k & 1)) {
                on = false;
                break;
            }
            k >>= 1;
	    }
	    printf("Case #%d: %s\n", cn, on ? "ON": "OFF");
	}

	return 0;
}
