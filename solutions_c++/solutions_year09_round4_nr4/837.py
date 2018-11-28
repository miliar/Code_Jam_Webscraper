// Author -Swarnaprakash.U
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define PB 			push_back
#define SZ(x)		((int)((x).size()))
#define TR(i,x) 	for(i=0;i<(x).size();++i)
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;
#define HELLO		if(debug) puts("hello");
#define LL 			long long
#define INF			0x3f3f3f3f
#define M			105

int x[M];
int y[M];
int r[M];

double fun(int a,int b)
{
	double d=(x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]);
	d=sqrt(d);
	return (d+r[a]+r[b])/2.0;
}

int main()
{
	int t,tc;
	scanf("%d",&tc);
	for(t=1;t<=tc;++t)
	{
		int n;
		scanf("%d",&n);
		int i;
		for(i=0;i<n;++i)
			scanf("%d %d %d",&x[i],&y[i],&r[i]);
		double ans;
		if(n==1)
			ans=r[0];
		else if(n==2)
			ans=max(r[0],r[1]);
		else
		{
			double a,b,c;
			a=max(fun(0,1),(double)r[2]);
			b=max(fun(1,2),(double)r[0]);
			c=max(fun(2,0),(double)r[1]);
			ans=min(a,min(b,c));
			
		}
		printf("Case #%d: %lf\n",t,ans);
	}
	return 0;
}
