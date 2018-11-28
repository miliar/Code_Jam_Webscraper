#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
	int T,cs;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for(cs=1;cs<=T;cs++)
	{
		printf("Case #%d: ",cs);
		
		int n,i,s,sum;
		int t[10005];
		scanf("%d",&n);
		s=0;
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&t[i]);
			s^=t[i];
			sum+=t[i];
		}
		if(s!=0)
		{
			printf("NO\n");
			continue;
		}
		sort(t,t+n);
		printf("%d\n",sum-t[0]);
	}
}