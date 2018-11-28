#include<cstdio>
#include<algorithm>

using namespace std;

const int MAXN = 1100;
const int INF = 2000000;

int candies[MAXN];
int n;

int maximum() {
	int res = 0, mini = INF, sum = 0;
	for (int i = 0; i < n; i++) {
		res = res ^ candies[i];
		mini = min(mini, candies[i]);
		sum += candies[i];
	}

	if (res != 0) return -1;
	else return (sum - mini);
}

int main() {
	int T = 0;
	scanf("%d", &T);

	for (int caseNum = 1; caseNum <= T; caseNum++) {
		n = 0;
		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			int c = 0;
			scanf("%d", &c);
			candies[i] = c;
		}

		int res = maximum();

		printf("Case #%d: ", caseNum);
		if (res > 0)
			printf("%d\n", res);
		else
			printf("NO\n");
	}

	return 0;
}
