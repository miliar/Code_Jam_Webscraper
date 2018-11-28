#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

const int MAXN = 10100;
int and_gate[MAXN], changeable[MAXN], n, v, opt[MAXN][2], value[MAXN];

int left(int i) { return 2*i+1; }
int right(int i) { return 2*i+2; }

void process() {
	scanf("%d %d", &n, &v);
	for (int i = 0; i < n; i++)
		opt[i][0] = opt[i][1] = -1;
	for (int i = 0; i < (n-1)/2; i++)
		scanf("%d %d", &and_gate[i], &changeable[i]);
	for (int i = (n-1)/2; i < n; i++) {
		scanf("%d", &value[i]);
		// printf("value %d: %d\n", i, value[i]);
	}
	for (int i = (n-1)/2 - 1; i >= 0; i--) {
		if (and_gate[i])
			value[i] = (value[left(i)]&&value[right(i)]);
		else
			value[i] = (value[left(i)]||value[right(i)]);
		// printf("value %d: %d\n", i, value[i]);
	}

	for (int i = 0; i < n; i++)
		opt[i][value[i]] = 0;
	for (int i = (n-1)/2 - 1; i >= 0; i--) {
		if (changeable[i]) {
			int s = !value[i];
			for (int tl = 0; tl <= 1; tl++)
				for (int tr = 0; tr <= 1; tr++) {
					int t = (and_gate[i]?(tl||tr):(tl&&tr));
					if (t == s && opt[left(i)][tl]>=0 && opt[right(i)][tr]>=0 && (opt[left(i)][tl] + opt[right(i)][tr] + 1 < opt[i][s] || opt[i][s] < 0))
						opt[i][s] = opt[left(i)][tl]+opt[right(i)][tr]+1;
				}
		}
		for (int s = 0; s <= 1; s++) {
			for (int tl = 0; tl <= 1; tl++)
				for (int tr = 0; tr <= 1; tr++) {
					int t = (and_gate[i]?(tl&&tr):(tl||tr));
					if (t == s && opt[left(i)][tl]>=0 && opt[right(i)][tr]>=0 && (opt[left(i)][tl] + opt[right(i)][tr] < opt[i][s] || opt[i][s] < 0))
						opt[i][s] = opt[left(i)][tl]+opt[right(i)][tr];
				}
			// printf("opt %d, %d: %d\n", i, s, opt[i][s]);
		}
	}

	if (opt[0][v]<0)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", opt[0][v]);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		process();
	}
}
