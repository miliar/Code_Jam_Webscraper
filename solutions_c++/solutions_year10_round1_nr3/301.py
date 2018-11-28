#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

bool run(int a, int b) {
	int flag = -1;
	int cnt = 0;
	if (a > b) {
		swap(a, b);
	}
	while (a != 0) {
		int t = b / a;
		if (t == 1) {
			cnt++;
		} else if (flag == -1) {
			flag = cnt;
		}
		t = b % a;
		b = a;
		a = t;
	}
	if (flag != -1){
		return flag % 2 == 0;
	} else {
		return cnt % 2 == 0;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		int A1, A2, B1, B2;
		scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
		int res = 0;
		for (int i = A1; i <= A2; i++) {
			for (int j = B1; j <= B2; j++) {
				if (run(i, j)) {
					res++;
				}
			}
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}
