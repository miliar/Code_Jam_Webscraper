#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <queue>
using namespace std;

int ans,a[2048],p[2048],dp[65537][22];

int maxi(int x,int y) 
{
	return (x>y)?x:y;
}

void IsBetter(int &x,int y) 
{
	if ((x<0) || (x>y)) {
		x=y;
	}
}

int main()
{
	int iNum;
	int iIndex;
	int x,y,i,j,k,n,m,num;
	freopen("in.txt","r",stdin);
	freopen("result.txt","w",stdout);

	for (scanf("%d",&iNum),iIndex=1;iIndex<=iNum;++iIndex) {
		printf("Case #%d: ",iIndex);
		scanf("%d",&n);
		m=1<<n;
		for (i=0;i<m;++i) 
		{
			scanf("%d",&a[i]);
			a[i]=n-a[i];
		}
		num=m>>1;
		memset(dp,0xff,sizeof(dp));
		for (i=n-1;i>=0;--i)
		{
			for (j=(1<<i),k=0;k<num;++k) 
			{
				scanf("%d",&p[k+j]);
			}
			num>>=1;
		}
		for (j=m,k=0;k<m;++k)
		{
			dp[j+k][a[k]]=0;
		}
		for (i=m-1;i;--i) 
		{
			x=(i<<1);
			y=(i<<1)|1;
			for (j=0;j<=n;++j)
			{
				if (dp[x][j]<0)
				{
					continue;
				}
				for (k=0;k<=n;++k)
				{
					if (dp[y][k]<0)
					{
						continue;
					}
					IsBetter(dp[i][maxi(j,k)],dp[x][j]+dp[y][k]);
					if (j+k) 
					{
						IsBetter(dp[i][maxi(j,k)-1],dp[x][j]+dp[y][k]+p[i]);
					}
				}
			}
		}
		printf("%d\n",dp[1][0]);
	}
	return 0;
}