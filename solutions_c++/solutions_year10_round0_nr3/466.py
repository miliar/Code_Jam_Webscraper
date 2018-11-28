#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    for (int line = 1; line <= t; line++) {
	int r, k, n, g[1000];
	scanf("%d %d %d", &r, &k, &n);
	for (int i = 0; i < n; i++) scanf("%d", &g[i]);

	long long total_riders = 0;
	for (int i = 0; i < n; i++) total_riders += g[i];

	long long result = 0;
	if (total_riders <= k) {
	    result = r * total_riders;
	} else {
	    int new_rider[1000], newly_boarded[1000];
	    for (int i = 0; i < n; i++) {
		int rider = i;
		int boarded = 0;
		while (boarded + g[rider] <= k) {
		    boarded += g[rider++];
		    if (rider == n) rider = 0;
		}

		new_rider[i] = rider;
		newly_boarded[i] = boarded;
	    }

	    int rider = 0;
	    for (int i = 0; i < r; i++) {
		result += newly_boarded[rider];
		rider = new_rider[rider];
	    }
	}

	printf("Case #%d: %lld\n", line, result);
    }
}
