#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int x[100],v[100];
bool d[100];
void solve()
{
	int n,k,b,t,i,j,s;
	scanf("%d %d %d %d",&n,&k,&b,&t);
	for (i=n-1;i>=0;i--)
		scanf("%d",x+i);
	for (i=n-1;i>=0;i--)
	{
		scanf("%d",v+i);
		if (b-x[i]<=t*v[i])
			d[i]=1;
		else
			d[i]=0;
	}
	j=0;
	for (i=0;i<n&&j<k;i++)
	{
		if (d[i]==1)
			j++;
	}
	if (j<k)
		printf("IMPOSSIBLE\n");
	else
	{
		s=0;
		j=0;
		for (i=0;i<n&&j<k;i++)
		{
			if (d[i]==1)
			{
				s+=i-j;
				j++;
			}
		}
		printf("%d\n",s);
	}
	return;
}
int main()
{
	int t,tt;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		printf("Case #%d: ",tt);
		solve();
	}
	return 0;
}