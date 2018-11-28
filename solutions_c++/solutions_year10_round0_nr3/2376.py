#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int t,n,k,g[11],r;
int money,head;

int getmoney();

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("test.out","w",stdout);
	
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		money=0;
		memset(g,0,sizeof(g));
		printf("Case #%d: ",i);
		scanf("%d %d %d",&r,&k,&n);
		for(int j=0;j<n;j++)
			scanf("%d",&g[j]);
		head=0;
		while(r-- >0)
		{
			money+=getmoney();
			
		}
		printf("%d\n",money);
	}
	return 0;
}

int getmoney()
{
	int mon=0;
	int temp=head;
	while((k-mon)>=g[temp])
	{
		mon+=g[temp];
		temp++;
		temp=temp%n;
		if(temp==head)
			break;
	}
	head=temp;
	return mon;
}