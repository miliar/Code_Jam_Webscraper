#include <cstdio>
#include <algorithm>
using namespace std;

int N;
int A[1111];

int brute() {
    int ans = -1;
    for(int k = 1; k + 1 < 1 << N; ++k) {
	int sum1 = 0, sum2 = 0, xorsum1 = 0, xorsum2 = 0;
	for(int i = 0; i < N; ++i) {
	    if(k & (1 << i)) {
		sum1 += A[i];
		xorsum1 ^= A[i];
	    }
	    else {
		sum2 += A[i];
		xorsum2 ^= A[i];
	    }
	}
	if(xorsum1 == xorsum2) {
	    ans = max(ans, max(sum1, sum2));
	}
    }
    return ans;
}

void solve(int test) {
    printf("Case #%d: ", test);
    scanf("%d", &N);
    int sumxor = 0;
    int ans = 1 << 30;
    int sum = 0;
    for(int i = 0; i < N; ++i) {
	int x;
	scanf("%d", &x);
	A[i] = x;
	sumxor ^= x;
	sum += x;
	ans = min(ans, x);
    }
    if(sumxor) {
	puts("NO");
    }
    else {
	printf("%d\n", sum - ans);
	//printf("%d\n", brute());
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
	solve(i);
    }
    return 0;
}
