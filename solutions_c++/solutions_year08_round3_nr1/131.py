#include<iostream>
#include<algorithm>
using namespace std;
__int64 al[1000];
int main()
{
	__int64 n,p,k,l,i,j,x,sum,flag=1;
	scanf("%I64d",&n);
	while(n--)
	{
		scanf("%I64d%I64d%I64d",&p,&k,&l);
		for(i=0;i<l;i++)
		{
			scanf("%I64d",&al[i]);
		}
		sort(al,al+l);
		sum=0;
		j=0;
		for(i=l-1,x=0;i>=0;i--,x++)
		{
			if(x%k==0)j++;
			sum+=al[i]*j;
		}
		printf("Case #%I64d: ",flag++);
		printf("%I64d\n",sum);
	}
	return 0;
}