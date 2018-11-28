#include <stdio.h>
#include <assert.h>

double min (double a, double b) {
    return (a < b) ? a : b;
}

int main (void) {
    int T;
    int scanned = scanf("%d", &T);
    for (int currentcase = 1; currentcase <= T; ++currentcase) {
	int n, d;
	scanf("%d %d", &n, &d);
	int place, number;
	scanf("%d %d", &place, &number);
	double last = place;
	double time = 0;
	--number;
	for (int i = 1; i < n || number != 0;) {
	    if (number == 0) {
		++i;
		scanf("%d %d", &place, &number);
	    }
	    if (place - last < d) {
		double newt = last - place + d;
		if (newt < time) {
		    last = place + newt;
		}
		else {
		    newt -= time;
		    last = place + time + (newt / 2.0);
		    time += (newt / 2.0);
		}
	    }
	    else {
		double gain = min(time, place - last - d);
		last = place - gain;
	    }
	    --number;
	}
	printf("Case #%d: %.8lf\n", currentcase, time);
    }
    return 0;
}
