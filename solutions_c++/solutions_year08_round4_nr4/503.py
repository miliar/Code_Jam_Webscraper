#include <algorithm>
#include <cstdio>
using namespace std;

const int MaxL = 1000 + 100;

int totCase, caseNum;
char s[MaxL];
char t[MaxL];
int n;
int len, ans;
bool v[20];
int a[20];

void work();
void dfs(int k);
int cptNum();

int main() {
	scanf("%d", &totCase);
	for (caseNum = 1; caseNum <= totCase; ++caseNum) {
		scanf("%d", &n);
		scanf("%s", s);
		printf("Case #%d: ", caseNum);
		work();
	}
	return 0;
}

void work() {
	len = strlen(s);
	ans = len;
	fill(v, v + n, false);
	dfs(0);
	printf("%d\n", ans);
}

void dfs(int k) {
	if (k == n) {
		ans = min(ans, cptNum());
	} else {
		for (int i = 0; i < n; ++i)
			if (!v[i]) {
				a[k] = i;
				v[i] = true;
				dfs(k + 1);
				v[i] = false;
			}
	}
}

int cptNum() {
	for (int i = 0; i < len; i += n) {
		for (int j = 0; j < n; ++j) {
			t[i + a[j]] = s[i + j];			
		}
	}
	int tot = 0;
	for (int i = 0; i < len; ++i) {
		if (i == 0 || t[i] != t[i - 1])
			++tot;
	}
	return tot;
}
