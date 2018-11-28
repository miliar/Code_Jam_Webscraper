#include <stdio.h>
#include <math.h>
const double PI = acos(-1.0);
double x[4], y[4], r[4];
double dis(int i, int j){
	return sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]));
}
double solve(int i, int j, int k){
	double t = (dis(i, j) + r[i] + r[j]) / 2;
	if(t > r[k]) return t;
	return r[k];
}
int main(){
	freopen("D:\\D-small-attempt0.in", "r", stdin);
	freopen("D:\\outD.txt", "w", stdout);
	int cases;
	scanf("%d", &cases);
	for(int case_t = 1; case_t <= cases; ++case_t){
		int n;
		double res = 1e100;
		scanf("%d", &n);
		for(int i = 1; i <= n; ++i) scanf("%lf%lf%lf", x + i, y + i, r + i);
		if(n == 1) res = r[1];
		else if(n == 2){
			if(r[1] > r[2]) res = r[1];
			else res = r[2];
		}
		else{
			if(solve(1, 2, 3) < res) res = solve(1, 2, 3);
			if(solve(1, 3, 2) < res) res = solve(1, 3, 2);
			if(solve(2, 3, 1) < res) res = solve(2, 3, 1);
		}
		printf("Case #%d: %lf\n", case_t, res);
	}
	return 0;
}