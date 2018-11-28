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
int nextA[102];
int nextB[102];
int topA;
int topB;
typedef struct node
{
	char cmd[3];
	int loc;
};
node Data[102];
int T,N;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	while(scanf("%d",&T)!=-1)
	{
		cas = 1;
		while(T--)
		{
			scanf("%d",&N);
			topA = topB = 0;
			for(int i=0;i<N;i++)
			{
				scanf("%s %d",&Data[i].cmd,&Data[i].loc);
				if(Data[i].cmd[0]=='O')
				{
					nextA[topA++] = Data[i].loc;
				}
				else
				{
					nextB[topB++] = Data[i].loc;
				}
			}
			int ans = 0,pAloc = 1,pBloc = 1, onet;
			for(int i=0,j=0,k=0;k<N;k++)
			{
				if(Data[k].cmd[0]=='O')
				{
					onet = abs(Data[k].loc-pAloc)+1;
					ans += onet;
					pAloc = Data[k].loc;

					i++;
					if(j<topB)
					{
						if( nextB[j]>=pBloc)
						{
							pBloc += onet;
							if(pBloc>nextB[j])
							{
								pBloc = nextB[j];
							}
						}
						else
						{
							pBloc -=  onet;
							if(pBloc<nextB[j])
							{
								pBloc = nextB[j];
							}
						}
					}
				}
				else
				{
					onet = abs(Data[k].loc-pBloc)+1;
					ans += onet;
					pBloc = Data[k].loc;

					j++;
					if(i<topA)
					{
						if( nextA[i]>pAloc)
						{
							pAloc += onet;
							if(pAloc>nextA[i])
								pAloc = nextA[i];
						}
						else
						{
							pAloc -= onet;
							if( pAloc<nextA[i])
								pAloc = nextA[i];
						}
					}
				}
			}

			printf("Case #%d: %d\n",cas++,ans);
		}
	}
	return 0;
}