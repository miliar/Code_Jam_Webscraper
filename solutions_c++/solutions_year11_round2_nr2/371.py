
#include "cstdio"
#include "cstring"
#include "cmath"
#include "iostream"
//#include "vector"
//#include "map"
//#include "string"

using namespace std;

typedef long long ll;

struct point {
	int pos;
	int count;
};


bool ispossible(ll step, int c, int d, point* pts) {

	ll at;

	at = -10000000000000;
	for (int i = 0; i < c; i++) {
		// for d=4
		// X----X----X----X----
		ll length = ((ll)pts[i].count) * ((ll) (d));
		ll pos = pts[i].pos;
		pos -= step;
		if (at < pos) at = pos;
		ll end = at + length;
		if ((end-(ll)d) > ((ll) pts[i].pos) + step) return false;
		//fprintf(stderr, "begin:%lld end:%lld\n", at, end);
		at = end;
	}
	return true;
}


int algo() {
	int tn;
	scanf("%d", &tn);

	for (int ti = 1; ti <= tn; ti++) {

		int c, d;
		scanf("%d %d", &c, &d);
		d *= 2;

		point pts[500];
		for (int i = 0; i < c; i++) {
			scanf("%d %d", &pts[i].pos, &pts[i].count);
			pts[i].pos *= 2;
		}

		ll min = 0;
		ll max = 10000000000000;
		while (min < max) {
			ll b = ((max-min) / 2) + min;
			//fprintf(stderr, "%lld %lld %lld\n", min, max, b);
			if (ispossible(b, c, d, pts)) {
				max = b;
			} else {
				min = b+1;
			}
		}


		//fprintf(stderr, "--- %lld\n", min);
		ispossible(min, c, d, pts);

		double w = min;
		w/=2.0;
		printf("Case #%d: %f\n", ti, w);
	}

	return 0;
}








//STANDARD COMMON CODE BELOW

int main(int argc, char *argv[]) {
	char str[80];
	strcpy(str, argv[1]);
	strcat(str, ".in");
  freopen(str, "r", stdin);
	strcpy(str, argv[1]);
	strcat(str, ".out");
	freopen(str, "w", stdout);

	int rv = algo();

	fclose(stdout);

	return rv;
}





