#include<iostream>
#include<stdio.h>
#include<math.h>
#define N 110
long double wp[N],owp[N],oowp[N];
char a[N][N];
int win[N],loss[N];

int main() 
{
	int tc,n;
	scanf("%d",&tc);
	for(int t=0;t<tc;t++)
	{
		scanf(" %d ",&n);
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				scanf(" %c ",&a[i][j]);
		for(int i=0;i<n;i++) 
		{
			win[i]=0,loss[i]=0;
			wp[i]=owp[i]=oowp[i]=0;
			for(int j=0;j<n;j++) 
			{ 
				if(a[i][j]=='1') win[i]++;
				else if(a[i][j]=='0') loss[i]++;
			}
			if(win[i]+loss[i])
				wp[i]=((double)win[i])/(win[i]+loss[i]);
		}
		for(int i=0;i<n;i++)
		{
			int j,count=0;
			for(j=0;j<n;j++)
			{
				if(i==j) continue;
				if(a[i][j]=='1')
				{
					if(win[j]+loss[j]>1)
						owp[i]+=((double)win[j])/(win[j]+loss[j]-1);
					count++;
				}
				else if(a[i][j]=='0')
				{
					if(win[j]+loss[j]>1)
						owp[i]+=((double)win[j]-1)/(win[j]+loss[j]-1);
					count++;
				}
			}
			if(count)
				owp[i]=owp[i]/count;
		}
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				if(a[i][j]!='.')
					oowp[i]+=owp[j];
			}
			if(win[i]+loss[i])
				oowp[i]=oowp[i]/(win[i]+loss[i]);
		}
		printf("Case #%d:\n",t+1);
		for(int i=0;i<n;i++)
			printf("%Lf\n",(wp[i]*0.25000000+owp[i]*0.500000000+oowp[i]*0.25000000));
	}
	return 0;
}


