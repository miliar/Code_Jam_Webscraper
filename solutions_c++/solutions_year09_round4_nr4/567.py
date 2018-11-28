#include <iostream>
#include <algorithm>
#include <bitset>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;


#define MAXN 1700001
unsigned int BKDRHash(char* str)
{
    unsigned int seed = 131 ; 
    unsigned int hash = 0 ;
    while (*str)
    {
        hash = hash*seed + (*str ++ );
    }
    return (hash & 0x7FFFFFFF );
}

int hash[MAXN];
inline bool hashit(char *str)
{
    int k,t;
    //while( *str == '0' )    str++;
    k = BKDRHash(str);
    t = k % MAXN;
    while( hash[t] != k && hash[t] != -1 )
        t = ( t + 10 ) % MAXN;
    if( hash[t] == -1 ) {
		hash[t] = k;
		return 0;
	}
	else return 1;
}
int n;
struct point
{
	int x,y,r;
}p[1000];
int main()
{
	int i, j, k,t, cas = 0;
	freopen("D-small-attempt0.in","r", stdin);
	freopen("D-out.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d", &n);
		for(i = 0 ; i < n; i ++)
			scanf("%d %d %d", &p[i].x, &p[i].y, &p[i].r);
		int dis = -1;
		double res ;
		if( n == 1)
		{
			res = p[0].r;
		}
		else if( n == 2)
		{
			if ( p[0].r > p[1].r )
				res = p[0].r;
			else res = p[1].r;
		}
		else if( n == 3)
		{
			double dis23, dis12, dis13;
			dis23 = sqrt(0.0 + (p[1].x - p[2].x) * (p[1].x - p[2].x) + (p[1].y - p[2].y) * (p[1].y - p[2].y));
			if( dis23 + p[1].r <= p[2].r )
			{
				dis23 = p[2].r;
			}
			else if( dis23 + p[2].r <= p[1].r)
				dis23 = p[1].r;
			else dis23 = (dis23 + p[1].r + p[2].r )/2;

			if( dis23 < p[0].r ) 
				dis23 = p[0].r;


			dis12 = sqrt(0.0 + (p[0].x - p[1].x) * (p[0].x - p[1].x) + (p[0].y - p[1].y) * (p[0].y - p[1].y));
			if(dis12 + p[0].r <= p[1].r)
				dis12 = p[1].r;
			else if( dis12 + p[1].r <= p[0].r)
				dis12 = p[0].r;
			else dis12 = (dis12 + p[1].r + p[0].r )/2;
			if( dis12 < p[2].r ) 
				dis12 = p[2].r;



			dis13 = sqrt(0.0 + (p[0].x - p[2].x) * (p[0].x - p[2].x) + (p[0].y - p[2].y) * (p[0].y - p[2].y));
			if(dis13 + p[0].r <= p[2].r)
				dis13 = p[2].r;
			else if( dis13 + p[2].r <= p[0].r)
				dis13 = p[0].r;
			else dis13 = (dis13 + p[2].r + p[0].r )/2;
			if( dis13 < p[1].r ) 
				dis13 = p[1].r;

			res = dis12;
			if(res > dis13)  res = dis13;
			if( res > dis23) res = dis23;
		}
		printf("Case #%d: %.6lf\n", ++cas, res);
	}
	
}