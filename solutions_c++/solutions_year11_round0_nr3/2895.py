#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
	int i, j, k, batas, cnt, counter, T, ans, sean, patrick, dum, pile[1005], n, temp;
	bool cek;
//	freopen("3-1.in", "r", stdin);
//	freopen("3-1.out", "w", stdout);
	scanf("%d", &T);
	for (i = 1; i <= T; ++i)
	{
		ans = 0;
		scanf("%d", &n);
		for (j = 0; j < n; ++j)
		    scanf("%d", &pile[j]);
		batas = 1 << n;
		--batas;
		for (k = 1; k < batas; ++k)
		{
			temp = 0;
			counter = 0;
			sean = 0;
			patrick = 0;
			for (j = 0; j < n; ++j)
			{
				dum = pile[j];
				if (k & (1<<j))
				{
					temp += pile[j];
					sean = sean ^ dum;
				}
				else
				{
					patrick = patrick ^ dum;
				}
			}
			if (sean == patrick)
				ans = max(temp, ans);
		}
		if (ans == 0)
			printf("Case #%d: NO\n", i);
		else
			printf("Case #%d: %d\n", i, ans);
	}
//	fclose(stdin); fclose(stdout);
	return 0;
}
