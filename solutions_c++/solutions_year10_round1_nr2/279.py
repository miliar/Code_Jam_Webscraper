#include<iostream>
using namespace std;
int r[256],r2[256],b[100];
int main()
{
	int a,s,d,t,mn,D,I,m,n;
int _,T;
scanf("%d",&T);
for(_=1;_<=T;_++)
{
	scanf("%d%d%d%d",&D,&I,&m,&n);
	for(a=0;a<n;a++) scanf("%d",&b[a]);
	for(a=0;a<256;a++) r[a]=0;
	for(a=0;a<n;a++)
	{
		// Insert
		if( m>0 )
		{
			for(d=0;d<256;d++)
			{
				r2[d]=r[d];
				for(s=0;s<256;s++)
				{
					t=r[s]+((abs(s-d)-1)/m+1)*I;
					if( t<r2[d] ) r2[d]=t;
				}
			}
			for(d=0;d<256;d++)
			{
				r[d]=r2[d];
			}
		}
		// Delete
		for(d=0;d<256;d++) r2[d]=r[d]+D;
		// Alter
		for(d=0;d<256;d++)
		{
			for(s=0;s<256;s++)
			{
				if( abs(s-d)>m ) continue;
				t=r[s]+abs(d-b[a]);
				if( t<r2[d] ) r2[d]=t;
			}
		}
		for(s=0;s<256;s++) r[s]=r2[s];
//for(s=0;s<256;s++) printf("%d ",r[s]);
//printf("\n");
	}
	mn=r[0];
	for(a=1;a<256;a++) if( r[a]<mn ) mn=r[a];
	printf("Case #%d: %d\n",_,mn);
}
	return 0;
}
