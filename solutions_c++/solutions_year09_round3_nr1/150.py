#include<stdio.h>
#include<string.h>

int n,num[100];
char string[100];
__int64 ans;

void process()
{
	ans=0; n=strlen(string);
	int i,j,p=0,digit[100];
	for(i=0;i<n;i++){ num[i]=-1; digit[i]=i; }
	digit[0]=1; digit[1]=0;
	for(i=0;i<n;i++)
	{
		if(num[i]!=-1) continue;
		num[i]=digit[p];
		for(j=i+1;j<n;j++)
		{
			if(string[j]==string[i])
			{
				num[j]=digit[p];
			}
		}
		p++;
	}
	if(p==1) p++;
	__int64 x=1;
	for(i=n-1;i>-1;i--)
	{
		ans+=x*__int64(num[i]);
		x*=__int64(p);
	}
}

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%s",string);
		process();
		printf("Case #%d: %I64d\n",i,ans);
	}
	return 0;
}