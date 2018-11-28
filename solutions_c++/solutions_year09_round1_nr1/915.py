#include<stdio.h>
#include <stdlib.h>
#include<string.h>

char save[11][1000000];
char flag[1000000];

int ishappy(int n,int base)
{
	int len,i,sum;
	char s2[100];     //存base进制 
	
	memset(flag,0,sizeof(flag));
	
	itoa(n,s2,base);  //将n转为base进制 
	len = strlen(s2);
	
	if(save[base][n] == 'y')
		return 1;
	if(save[base][n] == 'n')
		return 0;
	
	while(1)
	{
		sum = 0;
		for(i = 0;i < len;i++)
		{
			sum += (s2[i]-'0') * (s2[i]-'0');
		}
		if(sum == 1)
		{
			save[base][n] = 'y';
			return 1;
		}
		if(flag[sum] == '1')
		{
			save[base][n] = 'n';
			return 0;
		}
		else
			flag[sum] = '1';
		itoa(sum,s2,base);  //将sum转为base进制 
		len = strlen(s2);
	}
}
int main()
{
	//	进制转换
	int T,i,ans,j;
	int num[10],t;
	char c;
	freopen("data.txt","w",stdout);
	freopen("A-small-attempt2.in","r",stdin);
	
	scanf("%d",&T);
	getchar();
	for(i = 1;i <= T;i++)
	{
		t = 0;
		//		memset(num,0,sizeof(num[0]));
		for(j = 0;j < 10;j++)
			num[j] = 0;
		while((c = getchar()) != '\n')
		{
			if(c == ' ')
				continue;
			if(c >= '2' && c <= '9')
				num[t++] = c-'0';
			if(c == '1')
			{
				c = getchar();
				num[t++] = 10;
			}
		}
		
		for(ans = 2;;ans++)
		{			
			j = 0;
			while(num[j] != 0)
			{
				if(!ishappy(ans,num[j]))
					break;
				j++;
			}
			if(num[j] == 0)  // 找到最小结果
				break;
		}
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}