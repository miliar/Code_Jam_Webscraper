#include <stdio.h>

int re;
int chk[16];
int n,num[16];

void goback(int x)
{
	int i,r1,r2,sum1,sum2;

	if(x==n)
	{
		sum1=sum2=0;
		for(i=0;i<n;i++)
		{
			if(chk[i]==0)
			{
				r1^=num[i];
				sum1+=num[i];
			}
			else
			{
				r2^=num[i];
				sum2+=num[i];
			}
		}
		if(r1==r2 && sum1!=0 && sum2!=0)
		{
			if(sum2>sum1)
				sum1=sum2;
			if(re<sum1)
				re=sum1;
		}
	}
	else
	{
		chk[x]=1;
		goback(x+1);
		chk[x]=0;
		goback(x+1);
	}
}

int main()
{
	int t,tcase,i;

	FILE *out;
	out=stdout;//fopen("C.out","w");

	scanf("%d",&tcase);

	for(t=0;t<tcase;t++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d",&num[i]);
		re=-1;
		goback(0);
		if(re==-1)
			fprintf(out,"Case #%d: NO\n",t+1);
		else
			fprintf(out,"Case #%d: %d\n",t+1,re);
	}

	return 0;
}