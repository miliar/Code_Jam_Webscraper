#include <stdio.h>

long long w[510][510];
long long s[510][510];
long long sx[510][510];
long long sy[510][510];
char str[510][510];

int main()
{
	long long T, r, c, d, i, j, x0, y0, x1, y1, k, cas, ans, x, y, xy;
	freopen("b2.in", "r", stdin);
	freopen("b2.out", "w", stdout);
	scanf("%I64d", &T);
	for (cas=1; cas<=T; cas++)
	{
		scanf("%I64d%I64d%I64d", &r, &c, &d);
		for (i=0; i<r; i++)
		  scanf("%s", str[i]);
		for (i=1; i<=r; i++)
		 for (j=1; j<=c; j++)
		   w[i][j]=str[i-1][j-1]-'0';
		ans=0;   
		long long rx, ry;
		
		for (i=0; i<=r; i++)
		{
			rx=0;
		 for (j=0; j<=c; j++)
		 {
		 	if (i==0 || j==0) s[i][j]=0;
			else 
			{
				rx+=w[i][j];
				s[i][j]=s[i-1][j]+rx;
			}
		 }
		}
		
		
		for (i=0; i<=r; i++)
		{
			rx=0;
		 for (j=0; j<=c; j++)
		 {
		 	if (i==0 || j==0) sx[i][j]=0;
			else 
			{
				rx+=w[i][j]*i;
				sx[i][j]=sx[i-1][j]+rx;
			}
		 }
		}
		
		for (j=0; j<=c; j++)
		{
			ry=0;
		 for (i=0; i<=r; i++)
		 {
		 	if (i==0 || j==0) sy[i][j]=0;
			else 
			{
				ry+=w[i][j]*j;
				sy[i][j]=sy[i][j-1]+ry;
			}
		 }
		}
		
		
		
		long long tot;
		for (k=3; k<=r&&k<=c; k++)
		{
			for (x1=k; x1<=r; x1++)
			 for (y1=k; y1<=c; y1++)
			{
				x0=x1-k;
				y0=y1-k;
				
				x=sx[x1][y1]-sx[x0][y1]-sx[x1][y0]+sx[x0][y0];
				y=sy[x1][y1]-sy[x0][y1]-sy[x1][y0]+sy[x0][y0];
				xy=s[x1][y1]-s[x0][y1]-s[x1][y0]+s[x0][y0];
			
				tot=k*k-4;				
				x0++;
				y0++;
				x-=w[x0][y0]*x0+w[x0][y1]*x0+w[x1][y0]*x1+w[x1][y1]*x1;				
				y-=w[x0][y0]*y0+w[x0][y1]*y1+w[x1][y0]*y0+w[x1][y1]*y1;	
				xy-=w[x0][y0]+w[x0][y1]+w[x1][y0]+w[x1][y1];	
				
				if (x*2==(x0+x1)*xy && y*2==(y0+y1)*xy)
		   	   		if (k>ans) ans=k;				
			}
		}
	   if (ans==0) printf("Case #%I64d: IMPOSSIBLE\n", cas);
	   else printf("Case #%I64d: %I64d\n", cas, ans);		
	}
	return 0;
}
/*
10
3 3 2
111
111
111


3 3 2
222
222
222



*/