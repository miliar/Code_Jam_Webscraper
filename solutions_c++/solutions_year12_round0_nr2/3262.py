#include<iostream>
using namespace std;
int main()
{
	freopen("22.in","r",stdin);
	freopen("22.out","w",stdout);
	int t,j;
	int s,n,p,i,a;
	int ans;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		ans=0;
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a);
			if(a%3==0&&(a/3)>=p) ans++;
			else if((a+1)%3==0&&((a+1)/3)>=p) ans++;
			else if((a+2)%3==0&&((a+2)/3)>=p) ans++;
			else if(s>0&&a>=3&&a%3==0&&((a/3)+1)>=p)
			{
				s--; ans++;
			}
			else if(s>0&&a>=2&&(a+4)%3==0&&(a+4)/3>=p)
			{
				s--; ans++;
			}
			else if(s>0&&a>=4&&(a+2)%3==0&&(a+2)/3>=p)
			{
				s--; ans++;
			}
		}
		printf("Case #%d: %d\n",j,ans);
	}	
	return 0;
}
