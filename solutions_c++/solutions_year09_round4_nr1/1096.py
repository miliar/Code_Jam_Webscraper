#include<iostream>

using namespace std;

int a[100];
char str[100];
int n;

int main()
{
	int T;
	scanf("%d",&T);
	for (int t = 1; t <= T; t++)
	{
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		getchar();
		for (int i = 0; i < n; i++)
		{
			scanf("%s",str);
			for (int j = n - 1; j >= 0; j--)
				if (str[j] - 48 == 1)
				{
					 a[i] = j;
					 break;
				}
		}
		int ans = 0;	
		for (int i = 0; i < n; i ++)
		{
			for (int j = i; j < n; j++)
				if (a[j] <= i)
				{
					int tmp = a[j];
					for (int p = j; p > i; p --)
					{
						a[p] = a[p - 1];
						ans ++;
					}
					a[i] = tmp;
					break;
				}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	//system("pause");
	return 0;
}
