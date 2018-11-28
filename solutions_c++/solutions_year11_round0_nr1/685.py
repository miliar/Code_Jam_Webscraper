#include"iostream"
#include"stdio.h"
#include"algorithm"
#include"queue"
#include"string.h"
#include"vector"
#include"stack"
#include"set"
#define N 105
using namespace std;
struct node {

	char name[5];
	int cordinate;
} a[N];
int preB;
int preO;
int stepB;
int stepO;
void init() {
	preB = 1;
	preO = 1;
	stepB = 0;
	stepO = 0;
}
int solve(int n) {
	for (int i = 0; i < n; ++i) {
		if (a[i].name[0] == 'O') {
			if (abs(a[i].cordinate - preO) + stepO < stepB) {
				stepO = stepB + 1;
				preO = a[i].cordinate;
			} else {
				stepO += abs(a[i].cordinate - preO) + 1;
				preO = a[i].cordinate;
			}
		} else {
			if (abs(a[i].cordinate - preB) + stepB < stepO) {
				stepB = stepO + 1;
				preB = a[i].cordinate;
			} else {
				stepB += abs(a[i].cordinate - preB) + 1;
				preB = a[i].cordinate;
			}
		}
	}

	return max(stepB,stepO);
}
int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; ++i) {
		init();
		int n;
		scanf("%d", &n);
		for (int j = 0; j < n; ++j) {
			scanf("%s%d", a[j].name, &a[j].cordinate);
		}
		printf("Case #%d: %d\n", i + 1, solve(n));
	}
	return 0;
}
