#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<string>
#include<algorithm>
#include<functional>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<cassert>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;
int gcd( int a, int b ) {  if( !b ) return a;  return gcd( b, a % b ); }



int main()
{
	int t;
	scanf("%d",&t);
	int k = 1;
	while(t--)
	{
		int mat[1010][1010] ;
		int i,j,u,v,r;
		for(i = 0 ; i < 1010 ; i++)
		{
			for(j=0; j < 1010;  j++)
			{
				mat[i][j] = 0;
			}
		}
		scanf("%d%d",&u,&v);
		int count = 0;
		int x;
		for(x= u  ; x <= v; x++)
		{
			int m = x;
			char s[100];
			sprintf(s,"%d",m);
			int l = strlen(s);
			for(int i2 = 1; i2 <= l-1; i2++)
			{
				
				char g = s[0];
				for(i = 0; i <= l-2; i++)
				{
					s[i] = s[i+1];
				}
				s[l-1] = g;
				sscanf(s,"%d",&r);
				//printf("r =%d %d %d\n",r,u,v);
				int yy;
				//scanf("%d",&yy);
				if(r < u || r > v)
				{
					m = r;
					continue;
				}
				
				if(mat[x][r] == 0 && x != r)
				{
					mat[x][r] = 1;
					mat[r][x] = 1;
					count++;
					//printf("%d %d     count = %d\n",x,r,count);
				}
				m = r;
			}
		}
		printf("Case #%d: %d\n",k,count);
		k++;
		
	}    
	return 0;
}   
 
 
