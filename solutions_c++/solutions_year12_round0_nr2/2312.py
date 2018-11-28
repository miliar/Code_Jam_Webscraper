#include <iostream>
#include <string>
#include <sstream>

using namespace std;
int main () {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 0; i< t; ++i)
	{
		int n, s, p, ans = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (int j = 0; j < n; ++j)
		{
			int q;
			scanf("%d", &q);
			
			if (q/3 + (q % 3 == 0 ? 0 : 1) >= p) 
				++ans;
			else 
			{
				if (q > 0 && q / 3 + 1 >= p && q % 3 == 0 && s > 0)
				{
					++ans;
					--s;
				}
				if (q > 1 && q / 3 + 2 >= p && q % 3 == 2 && s > 0)
				{
					++ans;
					--s;
				}
			}
		}
		printf("Case #%d: %d\n", i+1, ans);
	}
	return 0;
}
