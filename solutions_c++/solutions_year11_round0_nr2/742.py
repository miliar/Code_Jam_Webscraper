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
int C,D,N,T;
int combine[27][27];
int oppos[27][27];
char in[104],out[104];
int main()
{
	freopen("B-large.in","r",stdin);
	write;
	int cas = 1;
	scanf("%d",&T);
	while(T--)
	{

		for(int i=0;i<27;i++) for(int j=0;j<27;j++) 
		{
			combine[i][j] = -1;
			oppos[i][j] = -1;
		}

		scanf("%d",&C);
		for(int i=0;i<C;i++)
		{
			scanf("%s",in);
			combine[in[0]-'A'][in[1]-'A'] = in[2]-'A';
			combine[in[1]-'A'][in[0]-'A'] = in[2]-'A';
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++)
		{
			scanf("%s",in);
			oppos[in[0]-'A'][in[1]-'A'] = 1;
			oppos[in[1]-'A'][in[0]-'A'] = 1;
		}
		scanf("%d",&N);
		scanf("%s",in);
		int top = 0, tmp;
		for(int i=0;i<N;i++)
		{
			out[top++] = in[i];
			if(top>1)
			{
				if( combine[out[top-2]-'A'][out[top-1]-'A']!=-1)
				{
					tmp = top-2;
					out[tmp++] = combine[out[top-2]-'A'][out[top-1]-'A']+'A';
					top = tmp;
				}
				else if( combine[out[top-1]-'A'][out[top-2]-'A']!=-1)
				{
					tmp = top-2;
					out[top++] = combine[out[top-1]-'A'][out[top-2]-'A']+'A';
					top = tmp;
				}
				else
				{
					bool f=true;
					for(int j=0;j<top-1;j++)
					{
						if( oppos[out[j]-'A'][out[top-1]-'A']==1 ||
							oppos[out[top-1]-'A'][out[j]-'A']==1 )
						{
							f=false;
							break;
						}
					}
					if(!f)
					{
						top=0;
					}
				}
			}
		}
		printf("Case #%d: [",cas++);
		if(top)
		{
			printf("%c",out[0]);
			for(int i=1;i<top;i++)
			{
				printf(", %c",out[i]);
			}
		}
		printf("]\n");
	}
	return 0;
}