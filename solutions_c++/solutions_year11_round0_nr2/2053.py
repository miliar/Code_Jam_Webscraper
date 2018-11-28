#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int ind(char a, char b)
{
	return a*256 + b;
}

void solve()
{
	int c, d, n;
	int cnt[256] = {};
	char ra[256*256] = {};
	int da[28];
	char buf[102];

	scanf("%d", &c);
	for (int i = 0; i < c; i++)
	{
		char q,w,e;
		scanf(" %c%c%c", &q, &w, &e);
		ra[ind(q,w)] = e;
		ra[ind(w,q)] = e;
	}

	scanf("%d", &d);
	for (int i = 0; i < d; i++)
	{
		char q,w;
		scanf(" %c%c", &q, &w);
		da[i] = ind(q,w);
	}

	vector<char> ans;
	scanf("%d %s", &n, buf);
	for (int i = 0; i < n; i++)
	{
		cnt[buf[i]]++;
		ans.push_back(buf[i]);

		if (ans.size() > 1)
		{
			int a = ans[ans.size() - 1], b = ans[ans.size() - 2];
			int c = ra[ind(a, b)];
			if (c > 0)
			{
				ans.pop_back();
				ans.pop_back();
				ans.push_back(c);
				cnt[a]--;
				cnt[b]--;
				cnt[c]++;
			}
		}
		
		for (int j = 0; j < d; j++)
		{
			int a = da[j] % 256, b = da[j] / 256;
			if (cnt[a] > 0 && cnt[b] > 0)
			{
				ans.clear();
				fill(cnt + 0, cnt + 256, 0);
				break;
			}
		}
	}

	putchar('[');
	for (int i = 0; i < ans.size(); i++)
	{
		printf(i == 0 ? "%c" : ", %c", ans[i]);
	}
	putchar(']');
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i+1);
		solve();
		printf("\n");
	}
	return 0;
}