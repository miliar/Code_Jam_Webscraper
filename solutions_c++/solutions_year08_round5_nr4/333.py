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
int h,w,r;
int rx[10];
int ry[10];
const int mod=10007;
int best[109][109];
int dx[]={1,2};
int dy[]={2,1};
int solve(int y,int x)
{
	if(y==h && x==w)
		return 1;
	if(y>=h || x>=w)return 0;
	int &ret=best[y][x];
	if(ret!=-1)return ret;
	ret=0;
	int i,j,y2,x2;
	for(i=0;i<2;i++)
	{
		y2=y+dy[i];
		x2=x+dx[i];
		for(j=0;j<r;j++)
			if(y2==ry[j] && x2 ==rx[j])break;
		if(j==r)
			ret=(ret+solve(y2,x2))%mod;
	}
	return ret;
}
FILE *in=fopen("d-small-attempt0.in","r");
FILE *out=fopen("d-small-attempt0.out","w");
int main()
{
	int i,j,k;
	fscanf(in,"%d",&cases);
	for(z=0;z<cases;z++)
	{
		CLS(best,-1);
		fscanf(in,"%d%d%d",&h,&w,&r);
		for(i=0;i<r;i++)
			fscanf(in,"%d%d",&ry[i],&rx[i]);
		k=solve(1,1);
		fprintf(out,"Case #%d: %d\n",z+1,k);
	}
	return 0;
}