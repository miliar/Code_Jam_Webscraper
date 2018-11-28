#include <math.h>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define max(myplants,b) (((myplants)>(b))?(myplants):(b))

struct node {
	double x, y, r;
}myplants[100];

int n;
double mydis(int i) {
	return (sqrt((myplants[i].x -myplants[(i+1)%n].x)*(myplants[i].x - myplants[(i+1)%n].x) + (myplants[i].y - myplants[(i+1)%n].y)*(myplants[i].y - myplants[(i+1)%n].y)) + myplants[i].r + myplants[(i+1)%n].r) / 2;
}
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int i, t;
	double ans;
	int cas, CAS;
	scanf("%d", &CAS);
	for (cas = 1; cas <= CAS; cas ++) {
		scanf("%d", &n);
		for (i = 0;i < n;i++)
			scanf("%lf%lf%lf", &myplants[i].x, &myplants[i].y, &myplants[i].r);
		if (n == 1) {
			printf("Case #%d: ", cas);
			printf("%lf\n", myplants[0].r);
			continue;
		}
		if (n == 2) {
			printf("Case #%d: ", cas);
			printf("%lf\n", max(myplants[0].r, myplants[1].r));
			continue;
		}
		ans = 1000000000;
		for (i = 0;i < n;i++) {
			if (ans > max(mydis(i), myplants[(i+2)%n].r))
				ans = max(mydis(i), myplants[(i+2)%n].r);
		}
		printf("Case #%d: ", cas);
		printf("%lf\n", ans);
	}
	return 0;
}
