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

char pMatrix[2][105][105];
int m,n,last,now;

int IsWest(int x,int y) 
{
	if (y==0) 
	{
		return 0;
	}
	return pMatrix[last][x][y-1]!='0';
}

int IsNorth(int x,int y)
{
	if (x==0) 
	{
		return 0;
	}
	return pMatrix[last][x-1][y]!='0';
}

int main()
{
	int iNum;
	int iIndex;
	int x1,y1,x2,y2,ans,num,t,i,j;
	freopen("in.txt","r",stdin);
	freopen("result.txt","w",stdout);

	for (scanf("%d",&iNum),iIndex=1;iIndex<=iNum;++iIndex)
	{
		printf("Case #%d: ",iIndex);
		m=n=num=0;
		memset(pMatrix,'0',sizeof(pMatrix));
		for (scanf("%d",&t);t;--t) 
		{
			scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
			--x1;
			--x2;
			--y1;
			--y2;

			if (x2>m) 
			{
				m=x2;
			}
			if (y2>n)
			{
				n=y2;
			}
			for (i=x1;i<=x2;++i) 
			{
				for (j=y1;j<=y2;++j) 
				{
					pMatrix[0][i][j]='1';
					++num;
				}
			}
		}
		for (i=0;i<=m;++i)
		{
			pMatrix[0][i][n+1]='0';
		}
		for (ans=last=0;num;++ans) 
		{
			memcpy(pMatrix[now=1-last],pMatrix[last],sizeof(pMatrix[0]));
			for (i=num=0;i<=m;++i)
			{
				for (j=0;j<=n;++j) 
				{
					if ((pMatrix[last][i][j]=='1') && (!IsNorth(i,j)) && (!IsWest(i,j)))
					{
						pMatrix[now][i][j]='0';
					}
					if ((pMatrix[last][i][j]=='0') && (IsNorth(i,j)) && (IsWest(i,j)))
					{
						pMatrix[now][i][j]='1';

					}
					if (pMatrix[now][i][j]=='1')
					{
						++num;
					}
				}
			}
			last=now;
		}
		printf("%d\n",ans);




	}
	return 0;
}