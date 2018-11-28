#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
int cases,g,h,w;
char grid[60][60];
bool put(int y,int x)
{
	if(y+1>=h || x+1>=w)return false;
	int i,j;
	for(i=0;i<2;i++)
		for(j=0;j<2;j++)
			if(grid[y+i][x+j]!='#')
				return false;
	grid[y][x]='/';
	grid[y][x+1]='\\';
	grid[y+1][x]='\\';
	grid[y+1][x+1]='/';
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
////////////////////////////////////////////
	int i,j,k;
	scanf("%d",&cases);
	for(g=0;g<cases;g++)
	{
		printf("Case #%d:\n",g+1);
		scanf("%d%d",&h,&w);
		for(i=0;i<h;i++)
		{
			scanf("%s",&grid[i]);
		}
		for(i=0;i<h;++i)
		{
			for(j=0;j<w;j++)
			{
				if(grid[i][j]=='#')
				{
					bool tmp=put(i,j);
					if(tmp==false)
					{
						printf("Impossible\n");
						goto bara;
					}
				}
			}
		}
		for(i=0;i<h;i++)
		{
			printf("%s\n",grid[i]);
		}
bara:
		k=1;
	}

	return 0;
}