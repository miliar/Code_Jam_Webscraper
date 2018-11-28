#include<iostream>
#include<algorithm>
#define MAX 2000

using namespace std;
__int64 a[MAX];

int main(void)
{
	__int64 t,n,L,i,p,k,res,flag,m,count,j;
	
	
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%I64d",&t);
	
	for(i=1;i<=t;i++)
	{
		scanf("%I64d %I64d %I64d",&p,&k,&L);
		for(j=0;j<L;j++)
		{
			scanf("%I64d",&a[j]);
		}
		sort(a,a+L);
		res = 0;
		m = 1;
		count = 0;
		flag = 0;
		for(j=L-1;j>=0;j--)
		{
			if(m>p)	flag = 1;
			res += m*a[j];
			count++;
			if(count == k)
			{
				count = 0;
				m++;
			}
		}
		if(flag==0)
		{
			printf("Case #%I64d: %I64d\n",i,res);
		}
		
	}
	return 0;
}