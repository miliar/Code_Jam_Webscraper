#include<iostream>
using namespace std;
int main()
{
	char tc;
	int a,n,i,b1,b2,p1,p2,c,t;
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
	scanf("%d",&n);
	c=0;
	p1=1; p2=1; b1=0; b2=0;
	for(a=0;a<n;a++)
	{
		scanf(" %c%d",&tc,&i);
		if( tc=='O' )
		{
			if( i<=p1 ) t=p1-i; else t=i-p1;
			if( t>b1 ) t-=b1; else t=0;
			b1=0;
			t++;
			c+=t;
			b2+=t;
			p1=i;
		}
		else
		{
			if( i<=p2 ) t=p2-i; else t=i-p2;
			if( t>b2 ) t-=b2; else t=0;
			b2=0;
			t++;
			c+=t;
			b1+=t;
			p2=i;
		}
//printf("%d %d %d\n",p1,p2,t);
	}
	printf("Case #%d: %d\n",_,c);
}
	return 0;
}
