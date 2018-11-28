#include<iostream>
using namespace std;
int b[2048][2048],b2[2048][2048];
int main()
{
	int a,s,d,n,t,m,mxx,mxy,x1,y1,x2,y2,c,brk;
	n=2048;
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
//	for(a=0;a<n;a++) for(s=0;s<n;s++){ b[a][s]=0; b2[a][s]=0; }
	scanf("%d",&m);
	mxx=0; mxy=0;
	for(a=0;a<m;a++)
	{
		scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
		for(s=x1;s<=x2;s++)
		{
			for(d=y1;d<=y2;d++)
			{
				b[s][d]=1;
			}
		}
		if( x2>mxx ) mxx=x2;
		if( y2>mxy ) mxy=y2;
	}
	c=0;
	while( 1 )
	{
		for(a=1;a<=mxx;a++)
		{
			for(s=1;s<=mxy;s++)
			{
				if( b[a][s-1]==1 && b[a-1][s]==1 ) b2[a][s]=1;
				else if( b[a][s]==1 && ( b[a][s-1]==1 || b[a-1][s]==1 ) ) b2[a][s]=1;
				else b2[a][s]=0;
			}
		}
		brk=1;
		for(a=1;a<=mxx;a++)
		{
			for(s=1;s<=mxy;s++)
			{
				b[a][s]=b2[a][s];
				if( b[a][s]==1 ) brk=0;
			}
		}
		c++;
		if( brk==1 ) break;
	}
	printf("Case #%d: %d\n",_,c);
}
	return 0;
}
