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
typedef long long ll;

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
int N;
int L,H;

int data[10010];

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&T);
	int cas = 1;
	while(T--)
	{
		scanf("%d %d %d",&N,&L,&H);
		for(int i=0;i<N;i++)
			scanf("%d",data+i);
		int ans = -1;
		for(int i=L;i<=H;i++)
		{
			bool f=true;
			for(int j=0;j<N;j++)
			{
				if( i%data[j]==0 || data[j]%i==0 )
				{
					;
				}
				else
				{
					f=false;
				}
			}
			if(f)
			{
				ans = i;
				break;
			}
		}
		printf("Case #%d: ",cas++);
		if(ans==-1)
			printf("NO\n");
		else
			printf("%d\n",ans);
	}

	return 0;
}