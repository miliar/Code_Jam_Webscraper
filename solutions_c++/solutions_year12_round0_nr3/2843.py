#include<stdio.h>

int pow(int x,int k)
{
	int sum=1;
	for(int i=1;i<=k;i++) sum*=x;
	return sum;
}

int main()
{
	freopen("E:\\TDDOWNLOAD\\C-small-attempt0.in","r",stdin);
	freopen("E:\\TDDOWNLOAD\\C-small-attempt0.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for(int cse=1;cse<=T;cse++)
	{
		int A,B;
		scanf("%d%d",&A,&B);
		
		int ans=0;
		for(int k=A;k<=B;k++)
		{
			int dig=1;
			int pre=-1;
			while(k/pow(10,dig)!=0) dig++;
			for(int i=1;i<dig;i++)
			{
				int tmp=k/pow(10,i)+(k%pow(10,i))*pow(10,dig-i);
				if(tmp!=pre&&tmp<k&&tmp>=A)
				{
					ans++;
					pre=tmp;
				}
			}
		}
		printf("Case #%d: %d\n",cse,ans);
	}
	return 0;
}
