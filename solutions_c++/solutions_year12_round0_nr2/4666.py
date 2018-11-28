#include<cstdio>
#include<algorithm>
using namespace std;
int arr[101];
int main()
{
	int t,i,j,s,p,x,n,tmp;
	int a,b,c,count;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		scanf("%d %d %d",&n,&s,&p);
		for(i=0;i<n;i++)scanf("%d",&arr[i]);
		count = 0;
		sort(arr,arr+n);
		for(i=n-1;i>=0;i--)
		{
			tmp = arr[i]/3;
			if(tmp>=p)count++;
			else
			{
				a=p;
				tmp = arr[i]-a;
				if(tmp>=0&&tmp>=(p-1)*2)
					count++;
				else if(tmp>=0&&s>0&&tmp>=(p-2)*2)
				{
					s--;
					count++;
				}
			}
		}
		printf("Case #%d: %d\n",j,count);
	}
	return 0;
}
