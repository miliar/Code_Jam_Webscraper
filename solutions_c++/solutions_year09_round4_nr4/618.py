#include <stdio.h>
#include <math.h>
#include <iostream>
using namespace std;

#define m0 100

double X[m0], Y[m0], R[m0];
int n;

double sqr(double x){
	return(x * x);
}

void init(){
	cin >> n;
	for (int i = 0;i < n; i++)
		cin >> X[i] >> Y[i] >> R[i];
}

double calc(){
	int i, j, k;

	if (n == 1) return(R[0]);
	if (n == 2) return(R[0] > R[1] ? R[0] : R[1]);

	double ans = 99999999999999.0;

	for (i = 0; i < n; i++){
		for (j = 0; j < n; j++){
			if (i == j) continue;

			for (k = 0; k < n; k++)
				if (k != i && k != j) break;

			double x1, y1, x2, y2, r1, r2;
			if (R[i] > R[j]){
				x1 = X[i]; y1 = Y[i]; r1 = R[i];
				x2 = X[j]; y2 = Y[j]; r2 = R[j];
			}
			else {
				x1 = X[j]; y1 = Y[j]; r1 = R[j];
				x2 = X[i]; y2 = Y[i]; r2 = R[i];	
			}
			double dis = sqrt(sqr(x1 - x2) + sqr(y1 - y2));
			if (dis + r2 <= r1){
				if (r1 >= R[k]){
					if (r1 < ans) ans = r1;
				}
			}
			else {
				double rr = (dis + r1 + r2) / 2.0;
				if (rr >= R[k]){
					if (rr < ans) ans = rr;
				}
			}
		}
	}
	return(ans);
}


int main(){
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; cin >> T;
	for (int i = 1; i <= T; i++){
		init();
		printf("Case #%d: %.6lf\n", i, calc());
	}
	return 0;
}