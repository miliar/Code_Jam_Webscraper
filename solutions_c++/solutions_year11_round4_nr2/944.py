#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<map>
using namespace std;
char s[505][505];
#define eps 1e-2
int max(int x,int y)
{
	if (x>y)return x;
	else return y;
}
int min(int x,int y)
{
	if (x<y)return x;
	else return y;
}
bool is_zero(double x)
{
	if ((x<=eps)&&(x>=-eps)) return true;
	else return false;
}
int main()
{
   freopen("B_small.in","r",stdin);
   freopen("B_small.out","w",stdout);
    int tcase,cas,k,r,c,i,j,d,ans,kk,lk,ii,jj;
	scanf("%d",&tcase);
	for(cas=1;cas<=tcase;cas++)
	{
		scanf("%d%d%d",&r,&c,&d);
		for(i=1;i<=r;i++)
			scanf("%s",s[i]+1);
		ans=0;
        for(kk=3;kk<=min(r,c);kk++)
		{
			lk=kk/2;
			if (kk%2==1)
			{
				for(i=lk+1;i<=r-lk;i++)
					for(j=lk+1;j<=c-lk;j++)
					{
					  
						int x=0,y=0;
						for(ii=i-lk;ii<=i+lk;ii++)
							for(jj=j-lk;jj<=j+lk;jj++)
								if (abs(i-ii)+abs(j-jj)!=2*lk)
							{
								x+=(j-jj)*(s[ii][jj]-'0');
								y+=(i-ii)*(s[ii][jj]-'0');
							}
								if ((x==0)&&(y==0)&&(kk>ans))
									ans=kk;
					}
			}
			else
			{
               for(i=lk+1;i<=r-lk+1;i++)
					for(j=lk+1;j<=c-lk+1;j++)
					{
						double midi,x=0,y=0,midj;
						midi=i-0.5;midj=j-0.5;
                      for(ii=i-lk;ii<=i+lk-1;ii++)
							for(jj=j-lk;jj<=j+lk-1;jj++)
								if (!
									(
									 ((ii==i-lk)&&((jj==j-lk)||(jj==j+lk-1)))
									 ||((ii==i+lk-1)&&((jj==j-lk)||(jj==j+lk-1)))
									)
								   )
								{
									x=x+(midi-ii)*(s[ii][jj]-'0');
									y=y+(midj-jj)*(s[ii][jj]-'0');
								}
						if ((is_zero(x)&&is_zero(y))&&(kk>ans))
							ans=kk;
					}
			}
		}
		if (ans==0) printf("Case #%d: IMPOSSIBLE\n",cas);
		else printf("Case #%d: %d\n",cas,ans);
	}
}
/* int l=0,r=0,d=0,u=0;
						for(ii=i-1;ii>=i-lk;ii--)
							for(jj=j-lk;jj<=j+lk;jj++)
								if (abs(i-ii)+abs(j-jj)!=2*lk)
								l+=(i-ii)*(s[i][j]-'0');
					     for(ii=i+1;ii<=i+lk;ii++)
						   for(jj=j-lk;jj<=j+lk;jj++)
								if (abs(i-ii)+abs(j-jj)!=2*lk)
								r+=(i-ii)*(s[i][j]-'0');
						for(jj=j-1;jj>=j-lk;jj--)
							for(ii=i-lk;ii<=i+lk;ii++)
								if (abs(i-ii)+abs(j-jj)!=2*lk)
								d+=abs(j-jj)*(s[i][j]-'0');
					     for(ii=i+1;ii<=i+lk;ii++)
						   for(jj=j-lk;jj<=j+lk;jj++)
								if (abs(i-ii)+abs(j-jj)!=2*lk)
								r+=abs(j-jj)*(s[i][j]-'0');*/