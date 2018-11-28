#include <iostream>
using namespace std;
int mm[1005];
int len[1005];
int Min(int aa,int bb)
{
	return aa<bb?aa:bb;
}
int main ()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int T,temp,left,xxx=0;
	int ans,i,j,k,l,t,n,c,cnt,sum;
	scanf("%d",&T);
	while(T--)
	{
		xxx++;
		printf("Case #%d: ",xxx);
		scanf("%d%d%d%d",&l,&t,&n,&c);
		for(i=0;i<c;i++)
		{
			scanf("%d",&mm[i]);
		}
		cnt=0;
		for(i=0;i<n;i++)
		{
			len[i]=mm[cnt++];
			if(cnt==c)cnt=0;
		}
		if(l==0)
		{
			sum=0;
			for(i=0;i<n;i++)sum+=len[i];
			printf("%d\n",sum*2);
			continue;
		}
		temp=999999999;
		if(l==1)
		{
			for(i=0;i<n;i++)
			{
				ans=0;
				for(k=0;k<n;k++)
				{
					if(k==i)
					{
						if(ans>=t)
						{
							ans+=len[k];
						}
						else
						{
							if(ans+len[k]*2<=t)
							{
								ans+=len[k]*2;
							}
							else
							{
								left=t-ans;
								ans=t;
								ans+=(len[k]-left*0.5);
							}
						}
					}
					else
					{
						ans+=len[k]*2;
					}
				}
				temp=Min(ans,temp);
			}
			printf("%d\n",temp);
			continue;
		}
		if(l==2)
		{
			for(i=0;i<n;i++)
			{
				for(j=i+1;j<n;j++)
				{
					ans=0;
					for(k=0;k<n;k++)
					{
						if(k==i||k==j)
						{
							if(ans>=t)
							{
								ans+=len[k];
							}
							else
							{
								if(ans+len[k]*2<=t)
								{
									ans+=len[k]*2;
								}
								else
								{
									left=t-ans;
									ans=t;
									ans+=(len[k]-left*0.5);
								}
							}
						}
						else ans+=len[k]*2;
					}
					temp=Min(temp,ans);
				}
			}
		}
		printf("%d\n",temp);
	}
}