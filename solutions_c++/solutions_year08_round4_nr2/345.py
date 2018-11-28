#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

typedef long long LL;
LL xabs(LL a) { if(a < 0) return -a; else return a; }
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 1; z <= t; ++z)
	{
		int n, m, aa;
		LL a;
		scanf("%d%d%d", &n, &m, &aa);
		//cin >> n >> m >> a;
		a = aa;
		bool fl = false;
		int xx1, xy1, xx2, xy2;
		for(int x = 0; x <= n; ++x)
		for(int y = 0; y <= m; ++y)
		for(int x1 = 0; x1 <= n; ++x1)
		for(int y1 = 0; y1 <= m; ++y1)
			{
				LL s = LL(x) * y1 - LL(x1) * y;
				s = xabs(s);
				if(s == a)
				{
					fl = true;
					xx1 = x, xy1 = y;
					xx2 = x1, xy2 = y1;
				}
			}
answer: int answer = fl;
		printf("Case #%d: ", z);
		if(fl)
		{
			printf("%d %d %d %d %d %d\n", 0, 0, xx1, xy1, xx2, xy2);
		} else
		{
			printf("IMPOSSIBLE\n");
		}

	}

	return 0;
}