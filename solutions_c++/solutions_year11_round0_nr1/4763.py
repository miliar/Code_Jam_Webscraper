#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

int main()
{
	int t, cas, n, i, o, ot, b, bt, ans, x;
	char c;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for (cas = 1; cas <= t; cas++)
	{
		scanf("%d", &n);
		o = 1; b = 1; ot = 0; bt = 0; ans = 0;
		for (i = 0; i < n; i++)
		{
			scanf(" %c%d", &c, &x);
			if (c == 'O')
			{
				ans = max(ans, ot+abs(x-o))+1;
				o = x;
				ot = ans;
			}
			else
			{
				ans = max(ans, bt+abs(x-b))+1;
				b = x;
				bt = ans;
			}
		}
		printf("Case #%d: %d\n", cas, ans); 
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}