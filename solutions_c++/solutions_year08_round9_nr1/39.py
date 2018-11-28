#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int test;
int usea[10010];
struct Titem
{
	int a, b, c;
}item[10010];

bool cmpb(const Titem &a, const Titem &b)
{
	return a.b < b.b;
}

void work()
{
	int n;
	scanf("%d", &n);
	memset(usea, 0, sizeof(usea));
	for (int i = 0; i < n; ++i)
	{
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);
		usea[a] = 1;
		item[i].a = a;
		item[i].b = b;
		item[i].c = c;
	}
	sort(item, item + n, cmpb);
	int ans = 0;
	for (int va = 0; va <= 10000; ++va)
	{
		if (!usea[va])
			continue;
		vector<int> lis;
		for (int i = 0; i < n; ++i)
		{
			if (item[i].a > va)
				continue;
			lis.push_back(item[i].c);
			push_heap(lis.begin(), lis.end());
			while (!lis.empty() && lis[0] > 10000 - va - item[i].b)
			{
				pop_heap(lis.begin(), lis.end());
				lis.pop_back();
			}
			if ((int)lis.size() > ans)
				ans = lis.size();
		}
	}
	printf("Case #%d: %d\n", ++test, ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
