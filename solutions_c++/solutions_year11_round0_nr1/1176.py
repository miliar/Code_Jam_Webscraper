#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
#define maxn 3000

int main()
{    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d",&T);

	int k,n,a1,a2,b1,b2,t,x,i;
	char ch;
	for(k=1; k<=T; k++)
	{
		a1=b1=1;a2=b2=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%c%c%d",&ch,&ch,&x);
			if(ch == 'O')
			{
				t=x;
				x-=a1;
				a1=t;
				if(x<0) x=-x;
				a2+=x+1;
				if(a2 <= b2)a2=b2+1;
			}
			else
			{
				t=x;
				x-=b1;
				b1=t;
				if(x<0) x=-x;
				b2+=x+1;
				if(b2 <= a2)b2=a2+1;
			}
			
		}
			if(a2<b2)a2=b2;
			printf("Case #%d: %d\n",k,a2);
	}
}