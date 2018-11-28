#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#define Sqr(x) ((x)*(x))
#define Dist(a,b) Sqr(a.x-b.x)+Sqr(a.y-b.y)

using namespace std;

const int MAXN=10010;

class TC
{
public:
	double r,x,y;
	int i;
}	;

TC C[MAXN];
int N;
double W,L;

bool CmpR(const TC &A,const TC &B)
{	return A.r>B.r;	}

bool CmpI(const TC &A,const TC &B)
{	return A.i<B.i;	}

void PutRight(const TC & A,TC & B)
{
	B.x=A.x+A.r+B.r;
	B.y=A.y-A.r+B.r;
	B.x=min(max(B.x,0.0),W);
	B.y=min(max(B.y,0.0),L);
}

void PutDown(const TC & A,TC & B)
{
	B.y=A.y+A.r+B.r;
	B.x=A.x-A.r+B.r;
	B.x=min(max(B.x,0.0),W);
	B.y=min(max(B.y,0.0),L);
}

bool Check(int x)
{
	if (C[x].x>W||C[x].y>L||C[x].x<0||C[x].y<0)
		return false;
	for (int i=1;i<x;++i)
		if (Dist(C[i],C[x])<Sqr(C[i].r+C[x].r))
			return false;
	return true;
}

void Solve()
{
	scanf("%d%lf%lf",&N,&W,&L);
	for (int i=1;i<=N;++i)
	{
		scanf("%lf",&C[i].r);
		C[i].i=i;
	}
	sort(C+1,C+N+1,CmpR);
	C[1].x=C[1].y=0;
	for (int i=2;i<=N;++i)
	{
		bool Put=false;
		for (int j=i-1;j&&!Put;--j)
		{
			PutRight(C[j],C[i]);
			Put=Check(i);
		}	 
		for (int j=i-1;j&&!Put;--j)
		{
			PutDown(C[j],C[i]);
			Put=Check(i);
		}
		if (!Put)
			printf("E[%lf]",C[i].r);
	}
	sort(C+1,C+N+1,CmpI);
	for (int i=1;i<=N;++i)
		printf(" %lf %lf",C[i].x,C[i].y);
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
	{
		printf("Case #%d:",i);
		Solve();
		printf("\n");
	}
	return 0;
}
