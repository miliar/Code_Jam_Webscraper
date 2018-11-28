#include<iostream>
#include<cstdio>

using namespace std;

__int64 kase=1,i,R,K,N,sum,res,cnt,a[1001],T,c;

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%I64d",&T);
	while(T--)
	{
		scanf("%I64d%I64d%I64d",&R,&K,&N);
		for(i=0;i<N;i++)
			scanf("%I64d",&a[i]);
		res=cnt=sum=c=0;
			
		for(i=0;i<N;i++)
		{
			if(sum+a[i]<=K)
			{
				sum+=a[i];
				c++;
				if(c==N)	{cnt++;res+=sum;sum=c=0;}
			}
			else
			{
				res+=sum;
				sum=c=0;
				i--;
				cnt++;
			}
			if(cnt==R)	break;
			if(i==N-1)	i=-1;
		}
		printf("Case #%I64d: %I64d\n",kase++,res);
	}
	return 0;
}