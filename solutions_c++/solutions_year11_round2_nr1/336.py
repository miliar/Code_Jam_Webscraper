#include<stdio.h>
int n;
char s[101][101];
int W[100],S[100];
double wp[101],owp[101],oowp[101];
int main()
{
	int test,i,j,T=1;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	for(;test>0;test--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%s",s[i]);
		}
		for(i=0;i<n;i++)
		{
			int w,ss;
			w=ss=0;
			for(j=0;j<n;j++)
			{
				if(s[i][j]!='.')
				{
					ss++;
					if(s[i][j]=='1')w++;
				}
			}
			W[i]=w;
			S[i]=ss;
			wp[i]=(double)w/ss;
		}
		for(i=0;i<n;i++)
		{
			int c=0;
			owp[i]=0;
			for(j=0;j<n;j++)
			{
				if(s[i][j]=='1')
				{
					if(S[i]>0)
					{
						owp[i]+=(double)W[j]/(S[j]-1);
					}
					c++;
				}
				else if(s[i][j]=='0')
				{
					if(S[i]>0)
					{
						owp[i]+=(double)(W[j]-1)/(S[j]-1);
					}
					c++;
				}
			}
			owp[i]/=c;
		}
		for(i=0;i<n;i++)
		{
			int c=0;
			oowp[i]=0;
			for(j=0;j<n;j++)
			{
				if(s[i][j]!='.')
				{
					oowp[i]+=owp[j];
					c++;
				}
			}
			oowp[i]/=c;
		}
		printf("Case #%d:\n",T++);
		for(i=0;i<n;i++)
		{
			printf("%.6lf\n",wp[i]/4+owp[i]/2+oowp[i]/4);
		}
	}
	return 0;
}