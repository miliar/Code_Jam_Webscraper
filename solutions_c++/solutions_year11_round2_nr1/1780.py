#include <cstdio>
#include <cstring>
#include <iostream>
#define ll __int64
using namespace std;
/*
freopen("1.txt","w",stdout);
*/
char a[105][205];
int cnt[105],win[105],lose[105];
double tmp1[105],tmp2[105];
double ans[105];
const double eps=1e-13;
int main()
{
	freopen("1.txt","w",stdout);
	int n,cas=1,t,i,j;
	scanf("%d",&t);
	while(t--)
	{
		memset(lose,0,sizeof(lose));
		memset(cnt,0,sizeof(cnt));
		memset(win,0,sizeof(win));
		memset(tmp2,0,sizeof(tmp2));
		memset(a,0,sizeof(a));
		memset(ans,0,sizeof(ans));
		printf("Case #%d:\n",cas++);
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{	
			scanf("%s",a[i]);
			//puts(a[i]);
			for(j=0;j<n;j++)
			{
				
				if(a[i][j]!='.')
				{
					cnt[i]++;
					if(a[i][j]=='1')win[i]++;
					tmp1[i]=win[i]*1.0/cnt[i];
				}
			}
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++ )
			{
				if(a[i][j]!='.')
				{
					if(a[i][j]=='1')
						tmp2[i]+=win[j]*1.0/(cnt[j]-1);
					else
						tmp2[i]+=(win[j]-1)*1.0/(cnt[j]-1);
				}
			}tmp2[i]=tmp2[i]*1.0/cnt[i];
		}
		for(i=0;i<n;i++)
		{
			ans[i]=0.25*tmp1[i]+0.5*tmp2[i];
			tmp1[i]=0;
			for(j=0;j<n;j++)
			{
				if(a[i][j]!='.')
					tmp1[i]+=tmp2[j];
			}
			ans[i]+=0.25*(tmp1[i]/cnt[i]);
			int tmp=10;
			int flag=0;
			for(j=0;j<=7&&!flag;j++)
			{
				int temp=ans[i]*tmp;
				if(ans[i]*tmp-temp<eps)
				{
					if(j==0)        printf("%.1lf",ans[i]);
					else if(j==1)	printf("%.2lf",ans[i]);
					else if(j==2)	printf("%.3lf",ans[i]);
					else if(j==3)   printf("%.4lf",ans[i]);
					else if(j==4)	printf("%.5lf",ans[i]);
					else if(j==5)	printf("%.6lf",ans[i]);
					else if(j==6)	printf("%.7lf",ans[i]);
					flag=1;
				}
				tmp*=10;
			}
			if(!flag)
				printf("%.12lf",ans[i]);
			puts("");
		}
	}
	
	return 0;
}