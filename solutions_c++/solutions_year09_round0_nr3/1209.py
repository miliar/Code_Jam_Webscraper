#include <stdio.h>
#include <string.h>

char wel[20] = "welcome to code jam";

int n, len;
char str[600];
int save[19][600];

int solve(int w, int s)
{
	//printf("%d\n",s);
	if (w >= 19) 
		return 1;
	if (s >= len) 
		return 0;
	if (save[w][s] >= 0) return save[w][s];

	int res = 0;
	for (int i = s; i < len; i++)
		if (str[i] == wel[w])
		{
			res+= solve(w+1, i+1);
			if (res > 10000) 
			{
				res%=10000;
			}
		}
	return save[w][s] = res;
}

main()
{
	freopen("C-large.in","r",stdin);
	freopen("tmp.out","w",stdout);

	scanf("%d\n",&n);
	
	for (int nn = 0 ; nn < n; ++nn)
	{
		gets(str);

		len = strlen(str);
		memset(save, 0xff, sizeof(save));	
		int ans = solve(0,0) %10000;
		printf("Case #%d: %04d\n", nn+1, ans);
	}

	return 0;
}
