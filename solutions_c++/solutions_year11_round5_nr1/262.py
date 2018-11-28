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
#include <memory.h>
using namespace std;

#define FRsmall(x,y) freopen(#x"-small-attempt"#y".in","r",stdin);freopen(#x"-small-attempt"#y".out","w",stdout);
#define FRlarge(x) freopen(#x"-large.in","r",stdin);freopen(#x"-large.out","w",stdout);

#define eps 1e-8

struct Point{
	int x;
	int y;
};

Point pl[110],pu[110];

double ly(double x)
{
	int i;
	for(i=1;pl[i].x+eps<x;i++);
	return pl[i-1].y+(pl[i].y-pl[i-1].y)*1.0/(pl[i].x-pl[i-1].x)*(x-pl[i-1].x);
}

double uy(double x)
{
	int i;
	for(i=1;pu[i].x+eps<x;i++);
	return pu[i-1].y+(pu[i].y-pu[i-1].y)*1.0/(pu[i].x-pu[i-1].x)*(x-pu[i-1].x);
}

int pre,now;

int tot;
int p[210];

double f(double x)
{
	return uy(x)-ly(x);
}

double Romberg(double x)
{
	int i;
	double S=0;
	for(i=1;p[i]+eps<x;i++)
	{
		S+=(f(p[i])+f(p[i-1]))/2*(p[i]-p[i-1]);
	}
	S+=(f(x)+f(p[i-1]))/2*(x-p[i-1]);
	return S;
}


int main()
{
	//freopen("A.in","r",stdin);
	//FRsmall(A,0)
	FRlarge(A)

	int T,C=0;
	scanf("%d",&T);
	while(++C<=T)
	{
		printf("Case #%d:\n",C);
		
		int W,L,U,G;
		scanf("%d %d %d %d",&W,&L,&U,&G);
		int i;
		tot=0;
		for(i=0;i<L;i++)
		{
			scanf("%d %d",&pl[i].x,&pl[i].y);
			p[tot++]=pl[i].x;
		}
		for(i=0;i<U;i++)
		{
			scanf("%d %d",&pu[i].x,&pu[i].y);
			p[tot++]=pu[i].x;
		}
		sort(p,p+tot);
		double S=Romberg(W)/G;
		for(i=1;i<=G-1;i++)
		{
			double lo=0,hi=W,mi;
			while(lo+eps<hi)
			{
				mi=(lo+hi)/2;
				if(Romberg(mi)<S*i)lo=mi;
				else hi=mi;
			}
			printf("%.8f\n",lo);
		}
	}
	return 0;
}
