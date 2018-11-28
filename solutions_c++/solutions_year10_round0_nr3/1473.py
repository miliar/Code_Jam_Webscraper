#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define llt long long 

int r,k,n;
int g[1011];
int a[1011];
int time[1011];

int solve()
{
	int s,t,now,tnow;
	int circle;
	int rmod,rt,rflag,rstart,rend,ra,rwhere;
	int i;
	llt ans;
	llt ar;
	
	memset(a,0,sizeof(a));
	memset(time,0,sizeof(time));
	now=-1;
	tnow=1;
	s=0;
	circle=0;
	while(1)
	{
		now=(now+1)%n;
		t=s+g[now];
		circle++;
		if (circle>n)
			t=s;
		if (t>k||circle>n)
		{
			if (time[(now+n-1)%n]==0)
			{
				a[(now+n-1)%n]=s;
				time[(now+n-1)%n]=tnow++;
				t=g[now];
				circle=1;
			}
			else
			{
				rwhere=(now+n-1)%n;
				ra=s;
				rflag=tnow;
				break;
			}
		}
		s=t;
	}
	
	ans=0;
	ar=0;
	
	/*
	tnow--;
	rmod=r%tnow;
	for(i=0;i<n;i++)
	{
		if (time[i]!=0)
			ar+=a[i];
		if (time[i]<=rmod)
			ans+=a[i];
	}
			
	ans+=ar*(r/tnow);
	*/
	if (r<tnow)
	{
		for(i=0;i<n;i++)
			if (time[i]<=r)
				ans+=a[i];
	}
	else
	{
		circle=rflag-time[rwhere];
		rstart=rflag-circle+1;
		rend=rflag;
		for(i=0;i<n;i++)
			if (time[i]<rstart)
				ans+=a[i];
		a[rwhere]=ra;
		time[rwhere]=rflag;
		for(i=0;i<n;i++)
			if (time[i]<=rend&&time[i]>=rstart)
				ar+=a[i];
		rmod=(r-rstart+1)%circle;
		rt=(r-rstart+1)/circle;
		for(i=0;i<n;i++)
			if (time[i]<=rstart+rmod-1&&time[i]>=rstart)
				ans+=a[i];
		ans+=ar*rt;
	}
	
	printf("%I64d\n",ans);
	
	/*
	printf("%d %d %d %d %d %d\n",circle,rstart,rend,rflag,rwhere,rt);	
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
	printf("\n");	
	for(i=0;i<n;i++)
		printf("%d ",time[i]);
	printf("\n");
	*/

	return 0;
}

int main()
{
	int casen,i,j;
	freopen("t3.in","r",stdin);
	freopen("t3.out","w",stdout);
	
	scanf("%d",&casen);
	for(i=1;i<=casen;i++)
	{
		scanf("%d %d %d",&r,&k,&n);
		for(j=0;j<n;j++)
			scanf("%d",&g[j]);
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
