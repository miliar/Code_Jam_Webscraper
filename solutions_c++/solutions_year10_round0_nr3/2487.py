#include <iostream>
using namespace std;
int main ()
{
	freopen("c-small.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int T,sum,t,r,k,n,p,temp,i,count;
	int a[15];
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		sum=0;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)scanf("%d",&a[i]);
		p=0;
		for(i=0;i<r;i++)
		{
			count=0;
			temp=0;
			while(temp+a[p]<=k)
			{
				count++;
				temp+=a[p];
				p++;
				if(p==n)p=0;
				if(count==n)break;
			}
			sum+=temp;
		}
		printf("Case #%d: %d\n",t,sum);
	}
}