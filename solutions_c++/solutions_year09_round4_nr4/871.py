#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <vector>
#include <set>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;i++)
#define FOR(i,a,b) for(int i=(a),_n=(b);i<=_n;i++)
#define _m(a,b) memset(a,b,sizeof(a))

int x[10],y[10],r[10];

int sqr(int x) {return x*x;}

double dist(int i,int j)
{
	return sqrt(sqr(x[i]-x[j])+sqr(y[i]-y[j]));	
}

int main()
{
	int t,n;
	scanf("%d",&t);
	REP(__,t)
	{
		scanf("%d",&n);
		REP(i,n) scanf("%d %d %d",x+i,y+i,r+i);
		double res = 100000;
		if (n==3)
		{
			res <?= max((double)r[0], (dist(1,2) + r[1] + r[2])/2.0);
			res <?= max((double)r[1], (dist(0,2) + r[0] + r[2])/2.0);
			res <?= max((double)r[2], (dist(0,1) + r[0] + r[1])/2.0);		
		}
		if (n==2) res = max(r[0],r[1]);
		if (n==1) res = r[0];
		fprintf(stderr,"Case #%d: %.6lf\n",__+1,res);
		printf("Case #%d: %.6lf\n",__+1,res);
	}
	return 0;	
}
