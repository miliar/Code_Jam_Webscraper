#include<iostream>
#include<stdio.h>
using namespace std;
int absi(int x)
{
	return (x>=0?x:-x);
}
int main()
{
	int t,i,j,n,cur;
	char type;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		scanf("%d",&n);
		int p1=1,t1=0,p2=1,t2=0;
		for(i=0;i<n;i++)
		{
			scanf(" %c %d",&type,&cur);
			if(type=='O')
			{
				t1=max(t1+absi(p1-cur),t2)+1;
				p1=cur;
			}
			else
			{
				t2=max(t2+absi(p2-cur),t1)+1;
				p2=cur;
			}
		}
		printf("Case #%d: %d\n",j,max(t1,t2));
	}
	return 0;
}
/*
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1
*/
