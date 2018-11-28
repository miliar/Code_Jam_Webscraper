#pragma warning (disable : 4786)

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>

using namespace std;

#define min(a,b) ((a) < (b) ? (a) : (b))
#define max(a,b) ((a) > (b) ? (a) : (b))

#define CLR(a) memset(a,0,sizeof(a))

#define i64 __int64

int cases,n,caseno;
i64 A,B,C,D,M;

struct Point
{
	i64 x,y;
	bool operator < (const Point &b) const
	{
		if(x==b.x) return y>b.y;
		return x>b.x;
	}
}P[101];

set <Point> S;

void makeInput()
{
	int i;

	for(i=1;i<n;i++)
	{
		P[i].x=(P[i-1].x*A+B)%M;
		P[i].y=(P[i-1].y*C+D)%M;
	}
	for(i=0;i<n;i++) S.insert(P[i]);
}

void process()
{
	int i,j,k,res=0;
	Point temp;

	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			for(k=j+1;k<n;k++)
			{
				if((P[i].x+P[j].x+P[k].x)%3) continue;
				if((P[i].y+P[j].y+P[k].y)%3) continue;
				temp.x=(P[i].x+P[j].x+P[k].x)/3;
				temp.y=(P[i].y+P[j].y+P[k].y)/3;
				res++;
			}
		}
	}
	printf("Case #%d: %d\n",++caseno,res);
}

int main()
{
	freopen("Inputs\\fk.txt","r",stdin);
	freopen("Inputs\\A1.txt","w",stdout);

	scanf("%d",&cases);
	while(cases--)
	{
		scanf("%d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&A,&B,&C,&D,&P[0].x,&P[0].y,&M);
		makeInput();
		process();
	}
	return 0;
}