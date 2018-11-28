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
#define torad(a) (a*pi/180.0)
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
int cases,z;
FILE *in=fopen("C-small-attempt0.in","r");
FILE *out=fopen("c-small-attempt0.out","w");
char grid[100][100];
int h,w;
char best[11][11][1<<10][1<<10];
inline bool busy(int m,int i)
{
	if(i>=0 && i<w)return (m & 1<<i);
		return 0;
}
char solve(int y,int x,int cm,int om)
{
	if(y==h)return 0;
	if(x==w)
		return solve(y+1,0,0,cm);
	char & ret=best[y][x][cm][om];
	if(ret!=-1)return ret;
	ret=0;

	//use disk
	if(grid[y][x]!='x' && !busy(cm,x-1) && !busy(om,x-1) && !busy(om,x+1))
		ret=max(ret,(char)(1+solve(y,x+1,cm | 1<<x,om)));
	//don't use
	ret=max(ret,solve(y,x+1,cm,om));
	return ret;
}
int main()
{
	int i,j,k;
	fscanf(in,"%d",&cases);
	for(z=0;z<cases;z++)
	{
		CLS(best,-1);
		fscanf(in,"%d%d",&h,&w);
		for(i=0;i<h;i++)
			fscanf(in,"%s",&grid[i]);
		k=solve(0,0,0,0);
		fprintf(out,"Case #%d: %d\n",z+1,k);
	}
	return 0;
}