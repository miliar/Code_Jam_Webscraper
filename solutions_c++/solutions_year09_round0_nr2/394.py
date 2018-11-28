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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int n,m;

bool isin(int x,int y)
{
	return (x>=0 && x<n && y>=0 && y<m);
}
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int tb[110][110];
char ret[110][110];

char flow(int x,int y,char mark)
{
//	ret[x][y]=mark;
	int i=0;
	int mim = tb[x][y];
	int marx=x,mary=y;
	for(i=0;i<4;i++)
	{
		int tx=x+dx[i],ty=y+dy[i];
		if(isin(tx,ty) && tb[tx][ty]<mim)
		{
			mim=tb[tx][ty];
			marx=tx,mary=ty;
		}
	}
	if(mim == tb[x][y])
	{
		if(ret[x][y]=='A')
			return ret[x][y]=mark;
		else
			return ret[x][y];
	}else
	{
		return ret[x][y]=flow(marx,mary,mark);
	}
}
int main()
{
	freopen("bin.txt","r",stdin);
	freopen("bout.txt","w",stdout);
	int T;
	scanf("%d",&T);
	int count=0;
	while(T--)
	{
		count++;
		memset(tb,-1,sizeof(tb));
		scanf("%d %d",&n,&m);
		int i,j;

		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				scanf("%d",&tb[i][j]);
				ret[i][j]='A';
			}
		char mark='a';
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
			{
				if(ret[i][j]!='A')
					continue;
				char ans='A';
				ans = flow(i,j,mark);
				if(ans==mark)
					mark++;
			}
		printf("Case #%d:\n",count);
		for(i=0;i<n;i++)
		{
			for(j=0;j<m;j++)
			{
				putchar(ret[i][j]);
				if(j!=m-1)
					putchar(' ');
			}
			putchar('\n');
		}
	}
}