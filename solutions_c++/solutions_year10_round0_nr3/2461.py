#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <list>
#include <ctype.h>
#include <string.h>
using namespace std;

const int NMAX = 30;

list <int> q;

int main()
{
	int t, r, k, n;
	freopen("test.in", "a+", stdin);
	freopen("test.out", "w", stdout);
	scanf("%d", &t);


	for (int l = 0; l < t; ++l)
	{
		printf("Case #%d: ", l+1);
		scanf("%d%d%d", &r, &k, &n);
		int g;
		q.clear();
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &g);
			if (g > k)
				continue;
			q.push_back(g);
		}
		int cnt = 0, ans = 0;
		int step = 0;
		for (list <int>::iterator it = q.begin(); step < r; ++step)
		{
			int schet = 0;
			while ((cnt + *it) <= k)
			{
				cnt += *it;
				q.push_back(*it);
				++it;
				list <int>::iterator temp = it;
				++temp;
				++schet;
				if (schet >= n)
				{
					q.pop_front();
					break;
				}
				q.pop_front();
			}
			ans += cnt;
			cnt = 0;
		}
		printf("%d\n", ans);
	}
	return 0;
}