#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

struct node
{
	vector<int> v;
	bool operator<(const node t) const {
		return v[0] < t.v[0];
	}
};

int a[100][100];
int flag[100], pre[100];
int n;

bool dfs(int now)
{
	int i,temp;
	for(i = 0; i < n; ++i)
	{
		if(a[now][i] && !flag[i])
		{
			flag[i] = true;
			temp = pre[i];
			pre[i] = now;
			if(temp == -1 || dfs(temp))
				return true;
			pre[i] = temp;
		}
	}
	return false;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w",stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int k;
		scanf("%d %d", &n, &k);
		vector<node> chart(n);
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < k; ++j) {
				int tmp;
				scanf("%d", &tmp);
				chart[i].v.push_back(tmp);
			}
		sort(chart.begin(), chart.end());
		for (int i = 0; i < n; ++i) {
			for (int j = i + 1; j < n; ++j) {
				int big = 0;
				for (int l = 0; l < k; ++l) {
					big += chart[j].v[l] > chart[i].v[l];
				}
				a[i][j] = big == k;
			}
		}
		memset(pre, 0xff, sizeof(pre));
		for (int i = 0; i < n; ++i) {
			memset(flag, 0, sizeof(flag));
			dfs(i);
		}
		int res = n;
		for (int i = 0; i < n; ++i)
			if (pre[i] != -1)
				--res;
		printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}