#include <stdio.h>
#include <iostream>

using namespace std;

int t, mx, n, test;
int a[100], s[100];

void write();

void read() {

	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d ", &t);

}


int check() {

	int sum1 = 0, sum2 = 0, sum3 = 0, sum4 = 0;

	for (int i=0; i<n; ++i) {

		if (s[i] == 0) {
			sum1 = sum1 ^ a[i];
			sum3 += a[i];
		} else {
			sum2 = sum2 ^ a[i];
			sum4 += a[i];
		}
		//printf("%d ", s[i]);
	}

	//printf("\n");

	if (sum1 == sum2 && sum1 != 0) {
		return (sum3 > sum4 ? sum3 : sum4);
	} else {
		return 0;
	}

	return 0;
}


void back(int p) {

	if (p > n) {

		int tmp = check();

		if (mx < tmp) {
			mx = tmp;
		}

	} else {

		for (int k=0; k<2; ++k) {
			s[p] = k;
			back(p+1);
		}

	}

}


void solve() {

	for (test = 1; test <= t; ++test) {

		mx = 0;

		scanf("%d ", &n);

		for (int i=0; i<n; ++i) {
			scanf("%d ", &a[i]);
		}

		back(0);

		write();
	}

}


void write() {

	printf("Case #%d: ", test);
	if (mx > 0) {
		printf("%d\n", mx);
	} else {
		printf("NO\n");
	}

}



int main() {

	read();
	solve();

	fclose(stdin);
	fclose(stdout);

	return 0;
}


