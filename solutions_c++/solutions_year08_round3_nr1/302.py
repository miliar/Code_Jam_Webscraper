#include<stdio.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("hi.txt","w",stdout);
	__int64 N,P,K,L;
	__int64 k=1,i;
	__int64 num[10000];
	int flag=0;
	scanf("%I64d",&N);
	while(k<=N)
	{
		scanf("%I64d%I64d%I64d",&P,&K,&L);
		for(i=0;i<L;i++)
		{
			scanf("%I64d",&num[i]);
			if(num[i]>1000000)
				flag=1;
		}
		if(P*K<L||flag==1)
		{
			printf("Case #%I64d: Impossible\n",k);
			k++;
			break;
		}
		__int64 j;
		for(i=0;i<L;i++)
		{
			for(j=i+1;j<L;j++)
			{
				if(num[i]<num[j])
				{
					__int64 t=num[i];num[i]=num[j];num[j]=t;
				}
			}
		}
		i=0;
		__int64 s=0;
		__int64 jj;
		while(i<L)
		{
			for(j=1;j<=P;j++)
			{
				for(jj=0;jj<K;jj++)
				{
					if(i>=L)
						break;
					s+=num[i]*j;
					i++;
				}
				if(i>=L)
					break;
			}
		}
		printf("Case #%I64d: %I64d\n",k,s);
		k++;
	}
}
