#include<stdio.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n,k,i,x,cs=0,temp,j,flag,a[40];
	scanf("%d",&x);
	while(x--)
	{
		cs++;
		flag=0;
		scanf("%d %d",&n,&k);
		temp=k;
		for(i=0;i<n;i++)
			a[i]=0;
		for(i=0;k>0;i++)
		{
			a[i]=k%2;
			k/=2;
		}
		for(j=0;j<n;j++)
		{
			if(a[j]==0 || temp==0)
			{
				printf("Case #%d: OFF\n",cs);
				flag=1;
				break;
			}
		}
		if(!flag)
			printf("Case #%d: ON\n",cs);
	}
	return 0;
}