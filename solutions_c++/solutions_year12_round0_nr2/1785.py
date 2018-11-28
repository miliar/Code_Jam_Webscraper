#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 100 + 2;

int T;
int n, s, p, now, i, ans;
int a[N];

int main() {
	freopen("input.txt", "r", stdin);	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; ans = 0, i <= T; i++) {
        scanf("%d%d%d", &n, &s, &p);
        for (int j = 1; j <= n; ++j)
			scanf("%d", &a[j]);
        sort(a + 1, a + n + 1);
        for (int j = n; j >= 1; j--)
			if (a[j] + 2 >= p * 3)
				ans++;
            else if (s && a[j] >= 2 && a[j] <= 28 && (a[j] - p) / 2 >= p - 2) {
                ans++;
                s--;
            }
        printf("Case #%d: %d\n", i, ans);
    }
	fclose(stdin);	fclose(stdout);
	return 0;
}
