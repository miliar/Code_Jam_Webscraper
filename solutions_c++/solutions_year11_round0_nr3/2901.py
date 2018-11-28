#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;

int w[1100];
int main()
{
	freopen("Clager.txt","w",stdout);
	int t,n,i,j,a,s,ss,k,max,ju;
	scanf("%d",&t);
	k=t;
	while(t--)
	{
		ju=1;
		s=0;
		ss=0;
		max=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&w[i]);
			s^=w[i];
			ss+=w[i];
		}
		for(i=0;i<n;i++)
		{
			a=s^w[i];
			if(a==w[i])
				if(max<ss-w[i])
				{
					max=ss-w[i];
					ju=0;
				}
		}
		if(ju==0)printf("Case #%d: %d\n",k-t,max);
		else printf("Case #%d: NO\n",k-t);
	}
	return 0;
}
