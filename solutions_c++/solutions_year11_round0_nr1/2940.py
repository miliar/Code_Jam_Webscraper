#include<iostream>
#include<stdio.h>
#define N 1000
using namespace std;
int a[N][2];
int timer[N];
int FindNext(int st,int dest,int type)
{
	if(type) type=1;
	else type=0;
	for(int i=st;i<dest;i++)
		if(a[i][0]==type)
			return i;
	return -1;
}
int Solve(int st,int dest,int blue,int orange)
{
	int pos,ans=0;
	if(a[st][0]==0) pos=blue;
	else pos=orange;
	for(int i=st;i<dest;i++)
	{
		if(timer[i]==-1) 
		{
			int dist=pos-a[i][1];
			if(dist<0) dist=-dist;
			ans+=(dist+1);
		}
		else ans+=(timer[i]+1);
		pos=a[i][1];
	}
	return ans;
}
int main()
{
	int i,j,k,tc,t,ans;
	int reqd,orange,blue,m,n,curr,next;
	char ch;
	scanf("%d",&tc);
	for(t=0;t<tc;t++)
	{
		scanf("%d ",&n);
		for(i=0;i<n;i++)
		{
			timer[i]=-1;
			scanf(" %c %d ",&ch,&m);
			a[i][1]=m;
			if(ch=='O')
				a[i][0]=1;
			else
				a[i][0]=0;
		}
		ans = 0;
		orange=blue=1;
		for(i=0;i<n;i++)
		{
			j=FindNext(i+1,n,!a[i][0]);
			if(a[i][0]==0)  {
				curr=blue;
				next=orange;
			}
			else {
				curr=orange;
				next=blue;
			}
			int diff,dist=curr-a[i][1];
			if(dist<0) dist=-dist;
			dist++;
			ans+=dist;
			if(j!=-1 && next!=a[j][1])
			{
				diff=(next-a[j][1]);
				if(diff<0) diff=-diff;
				if(dist>=diff)
				{
					if(a[j][0]==0) blue=a[j][1];
					else orange=a[j][1];
				}
				else 
				{
					switch ( a[j][0] )
					{
						case 0:
							if(blue<a[j][1]) blue+=dist;
							else blue-=dist;
							break;
						default:
							if(orange<a[j][1]) orange+=dist;
							else orange-=dist;
							break;
					}
				}
			}
			switch (a[i][0])
			{
				case 0:
					blue=a[i][1];
					break;
				default:
					orange=a[i][1];
					break;
			}
		}
		printf("Case #%d: %d\n",(t+1),ans);
	}
	return 0;				
}
