#include <stdio.h>

#define MAX_L 15
#define MAX_D 5005
#define MAX_N 505
#define MAX_S 1000

char word[MAX_D+2][MAX_L+2];
char str[MAX_S];
int L,D,N;

int solve()
{
	int ret=0;
	int i,j,k,flag;
	for (i=0;i<D;i++)
	{
		k=0;
		for (j=0;j<L;j++)
		{
			if(str[k] != '(') 
			{
				if(word[i][j] == str[k]) 
				{
					k++;
					flag = 1;
					continue;
				}
				else break;
			}
			else
			{
				k++;
				flag = 0;
				while (str[k] != ')')
				{
					if(word[i][j] == str[k] ) flag = 1;
					k++;
				}
				if (flag) k++;
				else break;
			}
		}
		if (j==L && flag) ret++;
	}
	return ret;
}
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A_Large.txt","w",stdout);
	int i,ans;
	scanf("%d%d%d",&L,&D,&N);
	for (i=0;i<D;i++)
	{
		scanf("%s",word[i]);
		
	}
	getchar();
	for (i=1;i<=N;i++)
	{
		gets(str);
		ans = solve();
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}