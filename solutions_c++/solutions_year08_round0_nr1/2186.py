// A.cpp : 定义控制台应用程序的入口点。
//

#include "cstdio"
#include "cstring"

int solve()
{
	int i,j,k,ii,ans;
	int s,q;
	char engine[100][101];
	char temp[101];
	int seq[1000] = {0};
	int a[2][100] = {0};

	scanf("%d",&s);
	getchar();
	for (i = 0; i < s; i++)
	{
		gets(engine[i]);
	}

	scanf("%d",&q);
	getchar();
	for (i = 0; i < q; i++)
	{
		gets(temp);
		for (j = 0; j < s; j++)
		{
			if (strcmp(engine[j],temp) == 0)
				seq[i] = j;
		}
	}

	ans = 10000;
	a[1][seq[0]] = 10000;
	for (i = 1,ii = 0; i < q; i++,ii = 1-ii)
		for (j = 0; j < s; j++)
		{
			if (seq[i] == j)
			{
				a[ii][j] = 10000;
				continue;
			}
			a[ii][j] = a[1-ii][j];
			for (k = 0; k < s; k++)
			{
				a[ii][j] = a[ii][j] < a[1-ii][k]+1 ? a[ii][j] : a[1-ii][k]+1; 				
			}
			if (i == q-1) 
				ans = ans < a[ii][j] ? ans : a[ii][j];
		}
	if (ans == 10000) ans = 0;
	return ans;
}

int main()
{
	freopen("s.txt","r",stdin);
	int n;

	scanf("%d",&n);
	for (int i = 0; i < n; i++)
	{
		printf("Case #%d: %d\n",i+1,solve());
	}

	return 0;
}

