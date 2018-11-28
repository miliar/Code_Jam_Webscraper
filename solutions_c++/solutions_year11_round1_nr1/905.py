
#include "cstdio"
#include "cstring"
#include "cmath"
//#include "vector"
//#include "map"
//#include "string"

using namespace std;

int solve(unsigned long long n,unsigned long long pd,unsigned long long pg) {

	//printf("%llu %llu %llu\n", n, pd, pg);

	if (pg == 100) {
		if (pd < 100) {
			return 0;
		} else {
			return 1;
		}
	}
	if (pg == 0) {
		if (pd > 0) {
			return 0;
		} else {
			return 1;
		}
	}

	if (pd == 0) return 1;

	unsigned long long a = pd;
	unsigned long long b = 100;
	if (a % 2 == 0) { a/=2; b/=2; };
	if (a % 2 == 0) { a/=2; b/=2; };
	if (a % 5 == 0) { a/=5; b/=5; };
	if (a % 5 == 0) { a/=5; b/=5; };

	if (n >= b) return 1;
	return 0;
}

int algo() {
	int tn;
	scanf("%d", &tn);

	for (int ti = 1; ti <= tn; ti++) {

		unsigned long long n, pd, pg;
		scanf("%llu %llu %llu", &n, &pd, &pg);
		

		int sol = solve(n, pd, pg);
		printf("Case #%d: ", ti);
		if (sol) {
			printf("Possible");
		} else {
			printf("Broken");
		}
		printf("\n");

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





