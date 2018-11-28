//============================================================================
// Name        : gcj.cpp
// Author      : yb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
struct node
{
	int x;
	int flag;
}a[200];
int abs(int a)
{
	return a>0?a:a*-1;
}
int b[200],c[200];
int main()
{
	freopen("1.out","w",stdout);
	int txt,n,l,l1,l2,cas=1;
	scanf("%d",&txt);
	while(txt--)
	{
		l=l1=l2=0;
		char f;
		scanf("%d",&n);
		while(n--)
		{
			scanf(" %c %d",&f,&a[l].x);
			if(f=='O'){a[l].flag=0;b[l1++]=a[l].x;}
			if(f=='B'){a[l].flag=1;c[l2++]=a[l].x;}
			l++;
		}
		/*for(int i=0;i<l1;i++)
			printf("%d ",a[i]);
		puts(" ");
		for(int i=0;i<l2;i++)
			printf("%d ",b[i]);
		puts(" ");*/
		int t1=1,t2=1,k1=0,k2=0;
		int ans=0,tmp;
		for(int i=0;i<l;i++)
		{
			if(!a[i].flag)
			{
				tmp=abs(a[i].x-t1)+1;
				ans+=tmp;
				t1=a[i].x;
				k1++;
				if(k2<l2)
				{
					if(tmp>abs(c[k2]-t2))t2=c[k2];
					else
					{
						if(c[k2]>t2)t2+=tmp;
						else t2-=tmp;
					}
				}
			}
			else
			{
				tmp=abs(a[i].x-t2)+1;
				ans+=tmp;
				t2=a[i].x;
				k2++;
				if(k1<l1)
				{
					if(tmp>abs(b[k1]-t1))t1=b[k1];
					else
					{
						if(b[k1]>t1)t1+=tmp;
						else t1-=tmp;
					}
				}
			}
		}
		printf("Case #%d: ",cas++);
		printf("%d\n",ans);
	}
	return 0;
}
