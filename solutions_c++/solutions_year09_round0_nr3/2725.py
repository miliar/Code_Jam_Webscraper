#include <stdio.h>
#include <string.h>
char str[]={"welcome to code jam"};
char word[502];
int map[50][50];

int solve(int len)
{	
	memset(map,0,sizeof(map));
	map[0][0] = 1;
	int res = 0;
	int i,j;
	for(i=0;i<len;i++)
	{
		for(j=0;j<=18;j++)
		{
			map[i][j]  %=10000;
			map[i+1][j]=map[i+1][j] + map[i][j];
			if(str[j]==word[i])
				map[i+1][j+1]= map[i+1][j+1] + map[i][j];
		}
		res  =	res +map[i][19];
		res= res % 10000;
	}
	return (res + map[len][19])%10000;
}
int main()
{	
	int n;
	int i,j,k;
	int len,count,sum;
	int flag;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	while(scanf("%d",&n)!=EOF)
	{
		
		getchar();
		for(k=1;k<=n;k++)
		{
		
			gets(word);
			len  = strlen(word);
			printf("Case #%d: ",k);
			count = solve(len);

			sum = count;
			i = 1;
			count = count/10;
			while(count>0)
			{	
				i ++;
				count=count/10;
			}
			for(j=1;j<=4-i;j++)
				printf("0");
			printf("%d\n",sum);

		}
	}
	return 0;
}
