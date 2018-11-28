#include<stdio.h>
#include<string.h>
char s[105][105];
int g[105][105],a[105],b[105];
double w[105],op[105],oop[105],r[105];
int main()
{
	int t,ca=1,cnt,i,j,n;
	double k;
	//freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d:\n",ca++);
		scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%s",s[i]);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
			{
				if(s[i][j]=='1')g[i][j]=1;
				else if(s[i][j]=='.')g[i][j]=-1;
				else g[i][j]=0;
			}
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=0;i<n;i++)
		{
			cnt=0;
			k=0;
			for(j=0;j<n;j++)
			{
				if(g[i][j]!=-1)cnt++;
				if(g[i][j]==1)
				{
					k=k+1;
					a[i]++;
				}
			}
			b[i]=cnt;
			w[i]=k/cnt;
		}
		for(i=0;i<n;i++)
		{
			k=0;
			cnt=0;
			for(j=0;j<n;j++)
				if(g[i][j]!=-1)
			{
				cnt++;
				if(g[i][j]==1)
				{
					k+=(double)(a[j])/(b[j]-1);
				}
				else
				{
					k+=(double)(a[j]-1)/(b[j]-1);
				}
			}
			op[i]=k/cnt;
		}
		for(i=0;i<n;i++)
		{
			k=0;
			cnt=0;
			for(j=0;j<n;j++)
				if(g[i][j]!=-1)
			{
				cnt++;
				k+=op[j];
			}
			oop[i]=k/cnt;
		}
		for(i=0;i<n;i++)
			r[i]=0.25*w[i]+0.5*op[i]+0.25*oop[i];
		for(i=0;i<n;i++)
			printf("%.9lf\n",r[i]);
	}
}
