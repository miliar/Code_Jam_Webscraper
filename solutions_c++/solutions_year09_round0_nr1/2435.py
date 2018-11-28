#include<stdio.h>
#include<string.h>

int cost[20][30];
char in[505];
char str[5005][20];
int n,d,l;
int change()
{
	int i=0,j=0;
	memset(cost,0,sizeof(cost));
	for(i=0;i<l;i++)
	{
		if(in[j]=='(')
		{
			j++;
			while(in[j]!=')')
			{
				cost[i][in[j]-'a']=1;
				j++;
			}
			j++;
		}
		else
		{
			cost[i][in[j++]-'a']=1;
		}
	}
	return 0;
}

int judge(char str[])
{
	int i;
	for(i=0;i<l;i++)
	{
		if(!cost[i][str[i]-'a'])
			return 0;
	}
	return 1;
}

int main()
{
	int i,j;
	int ans;
	scanf("%d%d%d",&l,&d,&n);
	for(i=0;i<d;i++)
		scanf("%s",str[i]);
	for(i=1;i<=n;i++)
	{
		ans=0;
		scanf("%s",in);
		change();
		for(j=0;j<d;j++)
			ans+=judge(str[j]);
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}