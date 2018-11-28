#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int input[1000];
int n = 0;


int gcd(int a, int b) {
	if (a < b) {
		int temp = a;
		a = b;
		b = a;
	}
	if (b == 0) {
		return a;
	}
	int r = a % b;
	while (r) {
		a = b;
		b = r;
		r = a % b;
	}
	return b;
}

long long f() {
	int best = abs(input[1] - input[0]);
	for (int i = 2; i < n; i++) {
		int diff = abs(input[i] - input[i-1]);
		best = gcd(best, diff);
	}
	if (input[0] % best == 0) {
		return 0;
	} else {
		return best - (input[0] % best);
	}
}

int main () {
	freopen("E:/algo/B_in.txt","r",stdin);
//	freopen("E:/algo/B_out_small.txt","w",stdout);

	int testNum = 0;
	scanf("%d", &testNum);
	for (int testIndex = 1; testIndex <= testNum; testIndex++) {
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &input[i]);
		}
		int result = f();
		printf ("Case #%d: %d\n", testIndex, result);
	}
	fflush(stdout);
	return 0;
}
