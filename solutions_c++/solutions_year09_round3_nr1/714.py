#include<stdio.h>
#include<string.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	__int64 CS,cs=1,l,mem[200],cnt,k,sum,i;
	char a[200];

	scanf("%I64d",&CS);
	
	while(CS--)
	{
		scanf("%s",a);
		memset(mem,-1,sizeof(mem));
		l=strlen(a);
		mem[a[0]]=1;
		cnt=2;
		k=0;
		for(i=1;i<l;i++)
			if(mem[a[i]]==-1)
			{
				if(k!=0)
					cnt++;
				mem[a[i]]=k++;
				if(k==1)
					k++;
			}
		sum=0;
		for(i=0;i<l;i++)
			sum=sum*cnt+mem[a[i]];

		printf("Case #%I64d: %I64d\n",cs++,sum);

	}
	return 0;
}