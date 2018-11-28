#include <cstdio>
#include <cstdlib>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int t, n, num[1024], pos[1024];
double ans[1024], C[1024][1024], bad[1024];

void solve();

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	//ans[0] = 1.0;
	//ans[2] = 2.0;
	//bad[0] = 1.0;
	//bad[1] = 0.0;
	//bad[2] = 1.0;
	//for (int i = 0; i <= 1000; ++i) {
		//C[i][0] = C[i][i] = 1;
		//for (int j = 1; j < i; ++j)
			//C[i][j] = C[i - 1][j] + C[i - 1][j - 1];
	//}
	//double fact = 2.0;
	//for (int i = 3; i <= 1000; ++i) {
		//fact *= i;
		//bad[i] = (i - 1) * (bad[i - 2] + bad[i - 1]);
		//ans[i] = 0;
		//for (int j = 1; j <= i; ++j) {
			//ans[i] += (C[i][j] * bad[i - j] / fact) * (ans[i - j] + 1);
		//}
		//double tmp = bad[i] / fact;
		//ans[i] = (ans[i] + tmp) / (1.0 - tmp);
	//}
    //for (int i = 2; i < 10; ++i)
        //printf("%lf\n", ans[i]);
    //printf("%lf\n", ans[100]);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i)
		solve();
	return 0;
}

void solve() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &num[i]);
		--num[i];
		pos[num[i]] = i;
	}
	sort(num, num + n);
	double sum = 0;
	for (int i = 0; i < n; ++i) {
		int k = 0;
		while (pos[num[i]] != i) {
			//ans += num[pos[num[i]]];
			++k;
			swap(pos[num[i]], pos[num[pos[num[i]]]]);
		}
        if (k != 0)
		    sum += k + 1;
	}
	printf("Case #%d: %.8lf\n", ++t, sum);
}
