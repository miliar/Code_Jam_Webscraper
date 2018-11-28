#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <fstream>

using namespace std;

int t,n,s,p;
int num[101];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int cas = 1,ans,i,a,b,c;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",cas++);
		scanf("%d%d%d",&n,&s,&p);
		for(i=0; i<n; i++)
			scanf("%d",&num[i]);
		sort(num,num+n);
		ans = 0;
		for(i=0; i<n; i++)
		{
			if(num[i]<p)
				continue;
			/*a = b = num[i]/3;
			c = num[i]-a-b;
			if(a>=p || c>p)
				ans++;
			else if(c==p)
			{
				ans++;
				if(c-b==2)
					s--;
			}
			else if(a==p-1 && c==p-1)
			{
				if(s>0)
				{
					s--;
					ans++;
				}
			}*/
			a = num[i]/3;
			if(num[i]%3>=1)
				c = a+1;
			else
				c = a;
			if(num[i]%3==2)
				b = c;
			else
				b = a;
			if(c>=p)
				ans++;
			else if(s>0 && c==p-1 && (a || b) && a!=b)
			{
				ans++;
				s--;
			}
			else if(s>0 && c==p-1 && (a || b) && a==p-1)
			{
				ans++;
				s--;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
