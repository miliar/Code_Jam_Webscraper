#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int len(int n)
{
	int ans = 0;
	while (n > 0)
	{
		++ans;
		n /= 10;
	}
	return ans;
}

int main () {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; ++i)
	{
		int a, b, ans = 0;
		scanf("%d%d", &a, &b);
		int l = len(a);
		int maxx = 1;
		vector <int> tmp;
		for (int j = 0; j < l; ++j)
			maxx *=10;		
		for (int j = a; j <= b; ++j)
		{
			tmp.clear();
			int po = 10;
			for (int k = 1; k < l; ++k)
			{
				if (j % po < po / 10 )
				{
					po *= 10;
					continue;
				}
				int ne = j % po * (maxx/po) + j / po;
				po *= 10;
				if (ne > j && ne >= a && ne <= b)
				{
					tmp.push_back(ne);
				}
			}
			sort(tmp.begin(), tmp.end());
			tmp.resize(unique(tmp.begin(),tmp.end()) - tmp.begin());
			ans += tmp.size();
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}
