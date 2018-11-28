#include<stdio.h>
#include<string.h>

int cost[12];
char str[25];
char ans[25];
int n,m;

int solve()
{
	int i,j,k,t;
	int flag=0;
	n=strlen(str);
	m=0;
	for(i=n-1;i>=0;i--)
	{
		k=str[i]-'0';
		cost[k]++;	
		if(m>k)
		{
			flag=1;
			break;
		}
		if(m<k)
			m=k;
	}
	
	if(flag)
	{
		k=0;
		for(j=0;j<i;j++)
			ans[k++]=str[j];
		for(j=1;j<=9;j++)
		{
			if((cost[j])&&(j>str[i]-'0'))
			{
				cost[j]--;
				ans[k++]=j+'0';
				break;
			}
		}
		t=0;
		for(j=i+1;j<n;j++)
		{
			while(cost[t]==0)
				t++;
			cost[t]--;
			ans[k++]=t+'0';
		}
		ans[k]='\0';
	}
	else
	{
		t=1;
		while(cost[t]==0)
			t++;
		ans[0]=t+'0';
		ans[1]='0';
		cost[t]--;
		k=2;
		t=0;
		for(j=1;j<n;j++)
		{
			while(cost[t]==0)
				t++;
			ans[k++]=t+'0';
			cost[t]--;
		}
		ans[k]='\0';
	}
	return 0;
}

int main()
{
	int t,T;
	scanf("%d",&T);

	for(t=1;t<=T;t++)
	{
		scanf("%s",str);
		solve();
		printf("Case #%d: %s\n",t,ans);
	}
	return 0;
}