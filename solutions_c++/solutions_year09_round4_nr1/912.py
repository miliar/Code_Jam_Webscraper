#include <iostream>
using namespace std;
int main()
{
	freopen("C.txt","r",stdin);
	freopen("ttt.txt","w",stdout);
	int n,T,map[50][50],i,j;
	char str[50];
	scanf("%d",&T);
	for (int p=1;p<=T;p++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%s",&str);
			for (j=0;j<n;j++)
				map[i][j] = str[j]-'0';
		}
		int result=0;
		for (int q=1;q<=n;q++)
		{
			for (i=q-1;i<n;i++)
			{
				for (j=q;j<n;j++)
				{
					if (map[i][j]) break;
				}
				if (j==n) break;
			}
			result += i-q+1;
			for (;i>q-1;i--)
			{
				for (j=0;j<n;j++)
				{
					int temp = map[i][j];
					map[i][j] = map[i-1][j];
					map[i-1][j] = temp;
				}
			}
		}
		printf("Case #%d: %d\n",p,result);
	}
	return 0;
}