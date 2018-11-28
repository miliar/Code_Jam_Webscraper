#include <iostream>
using namespace std;

double p[100010];
double ep[100010];

int main() {

	int t;
	scanf("%d", &t);

	for (int k = 0; k < t; k++) {
		int a, b;
		scanf("%d%d", &a, &b);
		for (int i = 0; i < a; i++) {
			scanf("%lf", &p[i]);
		}

		double t = 1;
		double acc = 1;
		for (int i = 0; i <= a; i++) {
			ep[i] = 0;
		}

		for (int i = 0; i < a; i++) {
			t = (1 - p[i]) * acc;
			int j;
			for (j = 0; j <= i; j++) {
				ep[(a - j)] += t * ((a - j) + (b - j) + 1);
			}
			for (; j <= a; j++) {
				ep[(a - j)] += t * ((a - j) + (b - j) + 1 + b + 1);
			}
			acc *= p[i];
		}

		for (int j = 0; j <= a; j++) {
			ep[a-j] += acc * ((a - j) + (b - j) + 1);
			//printf("t %d\n");
		}


		double ans = b + 1 + 1;



		for (int i = 0; i <= a; i++) {
			if (ep[i] < ans) ans = ep[i];
		}

		printf("Case #%d: %.6f", k+1, ans);

		if (k < t - 1) printf("\n");
	}
}

// int main() {

// 	int t;
// 	scanf("%d", &t);

// 	for (int k = 0; k < n; k++) {
		

// 		if (k < n - 1) printf("\n");
// 	}
// }