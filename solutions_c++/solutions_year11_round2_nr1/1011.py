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
char mp[110][110];
double ans[110];
double wp[110];
double owp[110];
double oowp[110];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		{
			scanf("%s",mp[i]);
		}
		
		for(int i=0;i<N;i++)
		{
			int all = 0,z = 0;
			for(int j=0;j<N;j++)
			{
				if( mp[i][j]!='.' )
				{
					z += mp[i][j]-'0';
					all++;
				}
			}
			wp[i] = (z+0.0)/(all+0.0);
		}

		for(int i=0;i<N;i++)
		{
			double ave = 0.0;
			int cnt = 0;
			for(int j=0;j<N;j++)
			{
				if( mp[i][j]!='.')
				{
					cnt++;
					// jµÄWP
					int all = 0,z = 0;
					for(int k=0;k<N;k++)
					{
						if( mp[j][k]!='.' && k!=i)
						{
							all++;
							z += mp[j][k]-'0';
						}
					}
					if(all!=0) ave += (z+0.0)/(all+0.0);
				}
			}

			owp[i] = ave/cnt;
		}

		for(int i=0;i<N;i++)
		{
			double ave = 0.0;
			int cnt = 0;
			for(int j=0;j<N;j++)
			{
				if(mp[i][j]!='.')
				{
					ave += owp[j];
					cnt++;
				}
			}
			oowp[i] = ave/cnt;
		}
		printf("Case #%d:\n",cas++);
		for(int i=0;i<N;i++)
		{
			ans[i] = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
			printf("%f\n",ans[i]);
		}
	}

	return 0;
}