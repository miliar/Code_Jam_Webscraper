#include<stdio.h>
#include<iostream>
#include<math.h>
using namespace std;
struct node
{
	char temp[3];
	int n;
}a[105];
int o[105],b[105];
int main()
{
	int cas,i,n,l1,l2,p1,p2,t1,t2;
	//freopen("2.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++)
	{
		scanf("%d",&n);
		l1=l2=0;
		for(i=0;i<n;i++)
		{
			scanf("%s%d",a[i].temp,&a[i].n);
			if(a[i].temp[0]=='O')
				o[l1++]=a[i].n;
			else
				b[l2++]=a[i].n;
		}
		p1=p2=1;t1=t2=0;
		for(i=0;i<n;i++)
		{
			if(a[i].temp[0]=='O')
			{
				t1+=abs(a[i].n-p1);
				if(i>0&&a[i-1].temp[0]=='B')
					t1=max(t1,t2);
				t1++;
				p1=a[i].n;
			}
			else
			{
				t2+=abs(a[i].n-p2);
				if(i>0&&a[i-1].temp[0]=='O')
					t2=max(t1,t2);
				t2++;
				p2=a[i].n;
			}
		}
		printf("Case #%d: %d\n",ii,max(t1,t2));
	}
	return 0;
}