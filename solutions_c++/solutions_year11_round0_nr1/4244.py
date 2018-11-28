/*


*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int Abs(int x)
{
	if (x < 0) return -x;
	return x;
}

int main()
{
	int T;
	int casen = 1;

	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	scanf("%d", &T);
	while (T--)
	{
		int n, ans;
		char str[3];
		int p, o_p=1, b_p=1;
		int o_T=0, b_T=0;
		int i, temp;

		scanf("%d", &n);
		for (i=0; i<n; i++)
		{
			scanf("%s%d", str, &p);
			if ('O' == str[0])
			{
				temp = Abs(o_p - p) + o_T;
				if (temp < b_T) temp = b_T;
				o_p = p;
				o_T = temp + 1;
			}
			else
			{
				temp = Abs(b_p - p) + b_T;
				if (temp < o_T) temp = o_T;
				b_p = p;
				b_T = temp + 1;
			}
		}

		ans = o_T > b_T ? o_T : b_T;
		printf("Case #%d: %d\n", casen++, ans);
	}

	return 0;
}

/*
Input:

3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

*/