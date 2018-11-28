#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
	int t,k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		int n,s,p,x,count=0,countp=0;
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&x);
			if(((x/3)+((x%3)!=0))>=p)
				count++;
			else if(x%3==0&&((x/3)+min(x/3,1))>=p)
				countp++;
			else if(x%3==2&&((x/3)+2)>=p)
				countp++;
		}
		printf("Case #%d: %d\n",k,count+min(s,countp));
	}
    return 0;
}