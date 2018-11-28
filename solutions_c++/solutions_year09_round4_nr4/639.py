#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAX = 105;
const int MAX_K = 30;

struct P{
	double x, y, r;
}p[10];

double fmin(double x, double y){
	return x < y ? x : y;
}

double fmax(double x, double y){
	return x > y ? x : y;
}

double dis(P a, P b)
{
	return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}


int main()
{
	int T;
	int cnt = 0;
	freopen("f://D-small-attempt0.in", "r", stdin);
	freopen("f://D-small-attempt0.out", "w", stdout);
	scanf("%d", &T);
	while(T--){
		int n;
		cnt++;
		scanf("%d", &n);
		int i, j;
		for(i = 0; i < n; i++){
			scanf("%lf%lf%lf", &p[i].x, &p[i].y, &p[i].r);
		}
		printf("Case #%d: ", cnt);
		if(n == 1)  printf("%.6lf\n", p[0].r);
		else if(n == 2){
			printf("%.6lf\n", fmax(p[0].r, p[1].r));
		}
		else if(n == 3){
			double ans1 = fmax((dis(p[0], p[1]) + p[0].r + p[1].r) / 2, p[2].r);
			double ans2 = fmax((dis(p[1], p[2]) + p[1].r + p[2].r) / 2, p[0].r);
			double ans3 = fmax((dis(p[2], p[0]) + p[2].r + p[0].r) / 2, p[1].r);
			printf("%.6lf\n", fmin(ans1, fmin(ans2, ans3)));
		}
	}
}