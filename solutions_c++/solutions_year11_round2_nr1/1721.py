#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

#define forn(i,n) for(int i=1;i<=n;i++)
#define Min(a,b) ((a)>(b)?(b):(a))
const double pi=acos(-1.0);
const double eps=1e-11;

int n,t;
char a[105][105];
double wp[105],owp[105],oowp[105];
double fz[105],fm[105];
int main()
{
	freopen("A-large (1).in","r",stdin);
	freopen("A-large (1).out","w",stdout);
	scanf("%d",&t);
	forn(tcase,t)
	{
		scanf("%d",&n);
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
		memset(fz,0,sizeof(fz));
		memset(fm,0,sizeof(fm));
		forn(i,n)
		{
			cin>>a[i-1];
			forn(j,n)
			{
				if(a[i-1][j-1]!='.')
				{
					fm[i-1]++;
					if(a[i-1][j-1]=='1')
						fz[i-1]++;
				}
			}
			wp[i-1]=fz[i-1]/fm[i-1];
		}
		forn(i,n)
		{
			forn(j,n)
			{
				if(j==i)
					continue;
				if(a[j-1][i-1]=='.')
					continue;
				if(a[j-1][i-1]=='0')
					owp[i-1]+=fz[j-1]*1.0/(fm[j-1]-1);
				else
					owp[i-1]+=(fz[j-1]-1)*1.0/(fm[j-1]-1);
			}
			owp[i-1]=owp[i-1]/fm[i-1];
		}
		forn(i,n)
		{
			forn(j,n)
			{
				if(j==i)
					continue;
				if(a[j-1][i-1]=='.')
					continue;
				oowp[i-1]+=owp[j-1];
			}
			oowp[i-1]=oowp[i-1]/fm[i-1];
		}
		printf("Case #%d:\n",tcase);
		forn(i,n)
		{
			printf("%.12lf\n",0.25*wp[i-1]+0.5*owp[i-1]+0.25*oowp[i-1]);
		}
	}
	return 0;
}