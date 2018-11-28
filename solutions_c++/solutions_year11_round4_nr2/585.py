#include <string.h>
#include <assert.h>
#include <math.h>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <iostream>
#include <stdio.h>
#include <algorithm>
#define sf scanf
#define pf printf
#define fr(i,a,b) for(int i=a;i<b;++i)
using namespace std;
#define ll long long
const double eps = 1e-8;

int g[520][520];
double sump[520][520];
double sum[520][520];
int str[530];
int r,c,d;
double multi( int c, double x, double y )
{
	return x*c + y * c;
}
void getsump()
{
	memset( sump, 0 ,sizeof( sump ) );
	memset( sum, 0 ,sizeof( sum ) );
	fr(i,1,r+1)
	{
		fr(j,1,c+1)
		{
			sump[i][j] = sump[i-1][j] + sump[i][j-1] - sump[i-1][j-1] +  multi( ( g[i][j] + d ) ,i , j )  ;
			sump[i][j] = sump[i][j];
			sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i - 1][j - 1] + g[i][j] + d;
		}
	}
}

double ft1(int x, int y, int k)
{
	double ret = multi(g[x][y] +d ,x,y) + multi( g[x-k+1][y] + d, x-k+1,y ) + multi( g[x-k+1][y-k+1] + d, x-k+1, y-k+1 ) + multi( g[x][y-k+1] + d, x, y-k+1 );	
	return ret;
}

double ft2( int x, int y, int k )
{
	double ret = g[x][y] + d + g[x-k+1][y] + d + g[x-k+1][y-k+1] + d + g[x][y-k+1] + d ;	
	return ret;
}

double getsump( int x1, int y1,  int k )
{
	assert( x1-k >= 0 );
	assert( y1 - k >= 0 );

	return sump[x1][y1] - sump[x1-k][y1] - sump[x1][y1-k] + sump[x1-k][y1-k]  - ft1( x1, y1, k );
}

double getsum( int x1, int y1,  int k )
{
	assert( x1-k >= 0 );
	assert( y1 - k >= 0 );

	return sum[x1][y1] - sum[x1-k][y1] - sum[x1][y1-k] + sum[x1-k][y1-k] - ft2( x1, y1, k );
}

void getcenter( int x, int y, int k, double &cx, double &cy )
{
	cx = x-k/2.0;
	cy = y-k/2.0;	
}

int getsum(int x,int y, int k, double cx, double cy )
{
	double p = getsump( x, y, k );
	double mp =  getsum( x, y, k );
	double tot = multi( mp, cx, cy );
	return fabs( p - tot ) < eps;
}

int sol()
{
	for(int k=max(r,c);k>2;--k)
	{
		fr(i,1,r+1)
		{
			fr(j,1,c+1)
			{
				if( i - k < 0 || j - k < 0 )
					continue;

				double cx, cy;
				getcenter( i, j, k, cx, cy );
				int ret = getsum(i,j, k, cx, cy );
				if( ret == 1 )
				{
					return k;
				}

			}
		}
	}
	return -1;
}


int main()
{
	int T;
	sf("%d",&T);
	int ca=0;
	while(T--)
	{
		sf("%d%d%d",&r,&c,&d);
		fr(i,1,r+1)
		{
			sf("%s",str+1);
			fr(j,1,c+1)
			{
				g[i][j]=str[j]-'0';
			}
		}
		getsump();
		int ans = sol();
		if( ans == -1 )
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n",ans);
		}
	}
	
}


