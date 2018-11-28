#include<iostream>
using namespace std;
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,k,x,a,count,next,ar[100],check;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d %d %d",&x,&k,&n);
		for(int j=0;j<n;j++)
		scanf("%d",&ar[j]);
		next=0;
		count=0;
		while(x--)
		{
			check=1;
			a=0;
			while(a+ar[next]<=k && check<=n)
			{
				count+=ar[next];
				a+=ar[next];
				if(next==n-1)
				next=0;
				else
				++next;
				check++;
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}
