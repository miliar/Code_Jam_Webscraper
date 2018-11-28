// include file
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <ctime>

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <list>
#include <functional>

using namespace std;

// typedef
typedef __int64 ll;

// 
#define read freopen("A-small-attempt1.in","r",stdin)
#define write freopen("out.txt","w",stdout)

const double eps = 1e-6;
const double INFf = 1e100;
const int INFi = 1000000000;
const double Pi = acos(-1.0);

template<class T> inline T sqr(T a){return a*a;}
template<class T> inline T TMAX(T x,T y)
{
	if(x>y) return x;
	return y;
}
template<class T> inline T TMIN(T x,T y)
{
	if(x<y) return x;
	return y;
}
template<class T> inline T MMAX(T x,T y,T z)
{
	return TMAX(TMAX(x,y),z);
}
template<class T> inline T MMIN(T x,T y,T z)
{
	return TMIN(TMIN(x,y),z);
}
template<class T> inline void SWAP(T &x,T &y)
{
	T t = x;
	x = y;
	y = t;
}


// code begin
int T;
char mp[55][55];
int M,N;

bool Isin(int r,int c)
{
	if( r<0 || r>=M || c<0 || c>=N ) return false;
	return true;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	
	scanf("%d",&T);
	int cas = 1;
	while(T--)
	{
		scanf("%d %d",&M,&N);
		for(int i=0;i<M;i++)
		{
			scanf("%s",mp[i]);
		}
		
		bool f = true;
		for(int i=0;i<M;i++)
		{
			for(int j=0;j<N;j++)
			{
				if(mp[i][j]=='#')
				{
					if( Isin(i+1,j) && mp[i+1][j]=='#' && Isin(i,j+1) && mp[i][j+1]=='#' && Isin(i+1,j+1) && mp[i+1][j+1]=='#' )
					{
						mp[i][j] = '/';
						mp[i][j+1]= '\\';
					    mp[i+1][j] = '\\';
						mp[i+1][j+1]='/';
					}
					else
					{
						f = false;
						break;
					}
				}
			}
			if(!f) break;
		}
		printf("Case #%d:\n",cas++);

		if(f)
		{
			for(int i=0;i<M;i++)
			{
				printf("%s\n",mp[i]);
			}
		}
		else
		{
			printf("Impossible\n");
		}
	}
	return 0;
}