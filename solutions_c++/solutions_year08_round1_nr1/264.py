#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vx;
vector<int> vy;

void solve(int id)
{
	sort(vx.begin(), vx.end());
	sort(vy.begin(), vy.end());
	reverse(vy.begin(), vy.end());

	int ans = 0;
	for (size_t i = 0;i < vx.size();++i)
		ans += vx[i] * vy[i];

	printf("Case #%d: %d\n", id, ans);
}

int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.txt", "w", stdout);

	/*freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);*/

	int N, n, temp;
	scanf("%d", &N);
	for (int i = 0;i < N;++i)
	{
		vx.clear();
		vy.clear();

		scanf("%d", &n);
		for (int j = 0;j < n;++j)
		{
			scanf("%d", &temp);
			vx.push_back(temp);
		}
		for (int j = 0;j < n;++j)
		{
			scanf("%d", &temp);
			vy.push_back(temp);
		}

		solve(i + 1);
	}
	return 0;
}