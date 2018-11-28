#include "stdio.h"
#include <vector>
#include <set>
#include <strstream>
#include <string>
#include <algorithm>
#include <hash_map>
#include <hash_set>
#include <queue>
using namespace std;
using namespace stdext;

#include <memory.h> 
#define null 0 
const int size = 110; 
//size must be bigger than n and m. 
//n小于m时效率高 
int maxmatch( int n, int m, bool w[][size], int *p) 
{ 
 int p_n[size]; 
 int p_m[size]; 
 bool sign[size]; 
 int q[size],from[size],s,t; 
 int i,j,link,now,h; 
 memset( p_n, -1, sizeof(int)*n ); 
 memset( p_m, -1, sizeof(int)*m ); 
 for(i=0;i<n;i++) 
 if(p_n[i]==-1) 
 { 
  memset( sign, 0, sizeof(bool)*m ); 
  s=1;link=-1; 
  from[0]=-1; 
  q[0]=size-1; 
  p_m[size-1]=i; 
  for(t=0;t<s;t++) 
  { 
     now=q[t]; 
     for(j=0;j<m;j++) 
     { 
      if( w[p_m[now]][j] != null && sign[j]==0 ) 
      { 
     sign[j]=1; 
     q[s]=j; 
     from[s++]=t; 
     if(p_m[j]==-1) 
     { 
      link=s-1; 
      break; 
     } 
      } 
     } 
     if(j<m)break; 
  } 
  if(t<s) 
  { 
    while(from[link]!=-1) 
    { 
     h=from[link]; 
     p_m[q[link]]=p_m[q[h]]; 
     p_n[p_m[q[h]]]=q[link]; 
     link=h; 
    } 
  } 
  //无完备匹配 
  //else return 0; 
 } 
 int an; 
 for(i=0,an=0;i<n;i++) 
 { 
  if(p)p[i]=p_n[i]; 
  if(p_n[i]>=0)an++; 
 } 
 return an; 
} 

int a[1000][200];
bool w[110][110];
int main()
{
	freopen( "test.in", "r", stdin );
	freopen( "test.out", "w", stdout );

	int tn, m, n;
	scanf( "%d", &tn );
	for( int cn = 1; cn <= tn; ++cn )
	{
		scanf( "%d%d", &n, &m );
		
		for( int i=0; i<n; ++i )
		{
			for( int j=0; j<m; ++j )
			{
				scanf( "%d", &a[i][j] );
			}
		}

		for( int i=0; i<n; ++i )
		{
			for( int j=0; j<n; ++j )
			{
				bool ok = true;
				for( int k=0; k<m; ++k )
				{
					if( a[i][k] <= a[j][k] )
					{
						ok = false;
						break;
					}
				}

				w[i][j] = ok;
			}
		}

		int ans = n - maxmatch( n, n, w, NULL );


		printf( "Case #%d: %d\n", cn, ans );
	}
	return 0;

}