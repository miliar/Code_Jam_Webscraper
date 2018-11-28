#include<iostream>
using namespace std;
int a[1005];
int main()
{
	int fi,re,n,len,f,k,r,l=1;
	int t;
	__int64 x,sum;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		for(re=0;re<n;re++)
			scanf("%d",&a[re]);
		fi=0;
		sum=0;
		while(r--)
		{
			x=k;
			len=0;
			f=a[fi];
			while(len<n&&x>=f)
			{
				x-=f;
				sum+=f;
				fi=(fi+1)%(n+1);
				a[re]=f;
				re=(re+1)%(n+1);
				f=a[fi];
				len++;
			}
		}
		printf("Case #%d: %I64d\n",l++,sum);
	}
	return 0;
}


 