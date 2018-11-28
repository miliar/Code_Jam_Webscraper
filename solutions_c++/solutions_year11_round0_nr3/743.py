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
typedef __int64 LL;

// 
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)

#define Z(a,b) ((a)<<(b))
#define Y(a,b) ((a)>>(b))

const double eps = 1e-6;
const double INFf = 1e100;
const int INFi = 1000000000;
const LL INFll = (LL)1<<62;
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
// 所有数的和不大于10^6
#define MAXN (1<<20)
int DP[MAXN][2];
int T,N,data[1010];
int main()
{
	freopen("C-large.in","r",stdin);
	write;
	int cas = 1,f;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&N);
		f = 0;
		for(int i=0;i<N;i++)
		{
			scanf("%d",data+i);
			f^=data[i];
		}
		printf("Case #%d: ",cas++);
		if(f)
		{
			printf("NO\n");
		}
		else
		{
			memset(DP,-1,sizeof(DP));
			DP[0][1] = 0;
			for(int i=0;i<N;i++)
			{
				for(int j=0;j<MAXN;j++)
				{
					DP[j][i&1] = DP[j][(i+1)&1];
				}
				for(int j=0;j<MAXN;j++)
				{
					if(DP[j][(i+1)&1]!=-1)
					{
						DP[j^data[i]][i&1] = TMAX(DP[j^data[i]][i&1],DP[j][(i+1)&1]+data[i]);
					}
				}
			}
			int ans = 0;
			for(int i=1;i<MAXN;i++)
			{
				if(DP[i][(N-1)&1]!=-1)
				{
					if( i^i==f )
					{
						if(DP[i][(N-1)&1]>ans)
							ans=DP[i][(N-1)&1];
					}
				}
			}
			printf("%d\n",ans);
		}
	}

	return 0;
}