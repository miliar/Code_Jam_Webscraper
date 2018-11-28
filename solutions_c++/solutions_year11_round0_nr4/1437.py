#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<map>
#include<algorithm>
using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large-output.txt","w",stdout);
	int T,n,i,k=0,ans,a;
	scanf("%d",&T);
	while(T--)
	{
		k++;
		ans=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a);
			if(i!=a)
				ans++;
		}
		printf("Case #%d: %.6lf\n",k,double(ans));
	}
	return 0;
}