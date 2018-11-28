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

int t,r,c;
char a[55][55];
int mov[3][2]={0,1,1,0,1,1};

int lbb(int x,int y)
{
	int ans=0;
	for(int i=0;i<3;i++)
		if(a[x+mov[i][0]][y+mov[i][1]]=='#')
			ans++;
	return ans;
}
void ice(int x,int y)
{
	a[x][y]='/';
	a[x][y+1]='\\';
	a[x+1][y]='\\';
	a[x+1][y+1]='/';
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	forn(tcase,t)
	{
		scanf("%d%d",&r,&c);
		forn(i,r)
			cin>>a[i-1];
		int judge=0;
		forn(i,r)
		{
			forn(j,c)
			{
				if(a[i-1][j-1]=='#') 
				{
					judge=1;
					if(lbb(i-1,j-1)==3)
						ice(i-1,j-1);
					else
					{
						judge=2;
						break;
					}
				}
			}
			if(judge==2)
				break;
		}
		printf("Case #%d:\n",tcase);
		if(judge==1 || judge==0)
		{
			forn(i,r)
				cout<<a[i-1]<<endl;
		}
		else
			printf("Impossible\n");
	}
	return 0;
}