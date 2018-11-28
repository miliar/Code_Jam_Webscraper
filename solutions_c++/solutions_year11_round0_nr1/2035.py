#include<stdio.h>
#include<cmath>
#include<iostream>
using namespace std;

struct node
{
	char ch;
	int pos;
}a[150];
int ans[150];
int main()
{
	int n,t,i,j,time,pos;
	char ch;
	int cas=1,posb,poso;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			cin>>ch>>pos;
			a[i].ch=ch;
			a[i].pos=pos;
		}
		posb=poso=1;
		time=0;
		ans[0]=a[0].pos;
		ch=a[0].ch;
		if(ch=='O')
			poso=a[0].pos;
		else
			posb=a[0].pos;
		time+=ans[0];
		for(j=1;j<n;j++)
			if(a[j].ch==ch)
			{
				if(a[j].ch=='O')
					pos=poso;
				else
					pos=posb;
				ans[j]+=ans[j-1]+abs(a[j].pos-pos)+1;
				pos=a[j].pos;
				time+=ans[j]-ans[j-1];
				if(a[j].ch=='O')
					poso=pos;
				else
					posb=pos;
			}
			else
			{
				if(a[j].ch=='O')
					pos=poso;
				else
					pos=posb;
				if(abs(a[j].pos-pos)>time)
					ans[j]=ans[j-1]+abs(a[j].pos-pos)-time+1;
				else
					ans[j]=ans[j-1]+1;
				pos=a[j].pos;
				ch=a[j].ch;
				time=ans[j]-ans[j-1];
				if(a[j].ch=='O')
					poso=pos;
				else
					posb=pos;
			}
		int Max=-1;
	    for(i=0;i<n;i++)
			if(Max<ans[i])
				Max=ans[i];
		memset(ans,0,sizeof(ans));
		printf("Case #%d: %d\n",cas++,Max);	    
	}
	return 0;
}

