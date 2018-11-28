#include <stdio.h>
#include <algorithm>
using namespace std;
char temp1[2000],temp[2000];
int se[15],list[15];
int MIN1 ,i , k ,T,len;
void dfs()
{
	int i,j;
	if(len == k)
	{
		int ans ;
		int l = strlen(temp1);
		int t = 0 ;
		for(i = 0 ; i < l ;)
		{
			for(j = 0 ; j < len ; j ++)
			{
				temp[i++] = temp1[list[j]-1+t];
			}
			t += k ;
		}
		ans = 0 ;
		for(i = 0 ; i < l ;)
		{
			j = i ;
			while(j+1 < l && temp[j] == temp[j+1])
			{
				j ++ ;
			}
			j ++ ;
			i = j ;
			ans ++ ;
		}
		if(MIN1 == -1 || ans < MIN1)
			MIN1 = ans ;
			return ;
	}
	for(i = 1 ; i <= k ; i ++)
	{
		if(se[i])
			continue ;
		se[i] = 1 ;
		list[len ++] = i ;
		dfs();
		len -- ;
		se[i] = 0 ;
	}
}
int main()
{
	int i;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&T);
	for(i = 1 ; i <= T ; i ++)
	{
		scanf("%d",&k);
		scanf("%s",temp1);
		memset(se,0,sizeof(se));
		len = 0 ;
		MIN1 = -1 ;
		dfs();
		printf("Case #%d: %d\n",i,MIN1);
	}
	return 0;
}