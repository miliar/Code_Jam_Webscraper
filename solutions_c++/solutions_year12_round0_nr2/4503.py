#include<iostream>
#include<cstdio>
#include<string.h>
#include<algorithm>

using namespace std;

int a[110];
int main()
{
	int C;
	int n,s,p;
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&C);
	int c=0;
	while(1)
	{
		c++;
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++)
			scanf("%d",a+i);
		sort(a,a+n);
		int res=0;
		if(p<=10)
		for(int i=n-1;i>=0;i--)
		{
			if(p==0){res=n;break;}
			if(a[i]==0)break;
			
			if(a[i]/3>=p)res++;
			else 
			{
				if(a[i]%3==0&&a[i]/3+1==p&&s)
				{
					s--;res++;
				}
				else if(a[i]%3>=1&&a[i]/3+1==p)
					res++;
				else if(a[i]%3==2&&a[i]/3+2==p&&s)
				{
					s--;res++;
				}
			}
		}
		printf("Case #%d: %d\n",c,res);
		if(c==C)break;
	}
	return 0;
}
				
				
				
				
				
				
				
				
				
				
				
				
		
