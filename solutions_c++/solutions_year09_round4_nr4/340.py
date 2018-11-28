#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cstring>
#include <ctime>
#include <queue>
using namespace std;
#define   max(a,b)    ((a)>(b)?(a):(b))
#define   min(a,b)    ((a)<(b)?(a):(b))
#define   sqr(a)         ((a)*(a))
#define   rep(i,a,b)  for(i=(a);i<(b);i++)
#define   REP(i,n)     rep(i,0,n)
#define   clr(a)      memset((a),0,sizeof (a));
#define   mabs(a)     ((a)>0?(a):(-(a))) 
#define   inf         1000000000
#define  MAXL     20
#define  MAXD     5010
#define  eps      1e-6
#define  MAXN      50
typedef __int64 int64;
FILE *fin;
FILE *fout;
int N;
typedef struct node 
{
	double x;
	double y;
	double r;
}node;
node pt[MAXN];
double getdis(node a,node b)
{
	return sqrt(sqr(a.x-b.x)+sqr(a.y-b.y));
}
double doit(int msk)
{
    int cnt=0;
	int i;
	node a,b;
    REP(i,N)
		if(msk&(1<<i)) 
		{
           cnt++;
		   if(cnt==1) 
			   a=pt[i];
		   else b=pt[i];
		}
	if(cnt==3||cnt==1) return a.r;
    return (a.r+b.r+getdis(a,b))/2;
}
double  solve()
{
	int i,j,k;
	double ret=1e99; 
	REP(i,1<<N)
	{
		int cnt=0;
		REP(j,N) if(i&(1<<j)) cnt++;
		if(cnt==0||cnt==3) continue;
       double tret=max(doit(i),doit(~i&((1<<N)-1)));
		ret=min(ret,tret);
	}
	return ret;
}
int main()
{
   	fin=fopen("D-small-attempt1.in","r");
	fout=fopen("output.txt","w");
	int i,j,k;
	int T;
	fscanf(fin,"%d",&T);
    int rounds;
	for (rounds=1;rounds<=T;rounds++)
	{
		  fscanf(fin,"%d",&N);
		  REP(i,N)
		  {
			  node &n=pt[i];
			  fscanf(fin,"%lf%lf%lf",&n.x,&n.y,&n.r);
		  }
	      double ret=solve();
		  
		  printf("Case #%d: %.10lf\n",rounds,ret);
          fprintf(fout,"Case #%d: %.10lf\n",rounds,ret);
	}
}
