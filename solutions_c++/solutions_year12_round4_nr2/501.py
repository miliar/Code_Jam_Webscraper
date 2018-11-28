#pragma comment(linker,"/STACK:128000000")
#include <cstdio>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <complex>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <functional>

using namespace std;

typedef unsigned long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef unsigned char uc;
typedef short int si;
typedef unsigned short int usi;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define all(x) (x).begin(),(x).end()
#define movmax(A,B) {if(A<(B)) A=(B);}
#define movmin(A,B) {if(A>(B)) A=(B);}
//#define x first
//#define y second

const double PI=acos(-1.0);
template<class T> T SQR(const T &a){return a*a;}

struct circle
{
	bool place;
	double x,y;
	int ind;
	int r;
} A[2000];
int n;
bool operator<(const circle &a,const circle &b)
{
	return a.r>b.r;
}

double Eps=1e-9;

bool check(int w,int h)
{
	rep(i,0,n)
	{
		if (!A[i].place) 
			return false;
		if (A[i].x<0 || A[i].x>w || A[i].y<0 || A[i].y>h)
			return false;
		rep(j,0,n)
		if (i!=j && sqrt(SQR(A[i].x-A[j].x)+SQR(A[i].y-A[j].y))<A[i].r+A[j].r)
			return false;
	}
	return true;
}

#define bit(x,i) (((x)>>(i))&1)
#define nill(x,i) ((x)&(~(1<<(i))))

void put(int x0,int y0,int w0,int h0,int mask)
{
	int x,y,w,h;
	rep(i,0,n)
	{
		h=h0;
		w=w0;
		x=x0;
		y=y0;
		if (bit(mask,0))
			y-=A[i].r;
		if (bit(mask,3))
			x-=A[i].r;
		if (bit(mask,0))
			h+=A[i].r;
		if (bit(mask,1))
			w+=A[i].r;
		if (bit(mask,2))
			h+=A[i].r;
		if (bit(mask,3))
			w+=A[i].r;
		if (!A[i].place && min(w,h)>=2*A[i].r)
		{
			A[i].x=x+A[i].r;
			A[i].y=y+A[i].r;
			if (A[i].x>w0 || A[i].y>h0) continue;
			A[i].place=true;
			if (w0-2*A[i].r>1 || (nill(mask,3) && w0-2*A[i].r>0))
			{
				int nm=nill(mask,3);
				if (h0-A[i].y-A[i].r>0) nm=nill(nm,2);
				put(x+2*A[i].r,y0,w0-2*A[i].r,min((int)A[i].y+A[i].r,h0),nm);
			}
			if (h0-2*A[i].r>1 || (nill(mask,0) && h0-2*A[i].r>0))
			{
				int nm=nill(mask,0);
				if (w0-A[i].x-A[i].r>0)
					nm=nill(nm,1);
				put(x0,y+2*A[i].r,min((int)A[i].x+A[i].r,w0),h0-2*A[i].r,nm);
				if (w-2*A[i].r>1 || (nill(mask,3) && w-2*A[i].r>0))
				{
					put(x+2*A[i].r,y+2*A[i].r,w-2*A[i].r,h-2*A[i].r,nill(nill(mask,3),0));
				}
			}
			break;
		}
	}
}

bool cmp(circle a,circle b)
{
	return a.ind<b.ind;
}

void test(int T)
{
	int w,h;
	cin>>n>>w>>h;
	rep(i,0,n)
	{
		A[i].place=false;
		A[i].ind=i;
		scanf("%d",&A[i].r);
	}
	sort(A,A+n);
	fprintf(stderr,"(%d",T);
	put(0,0,w,h,0xF);
	if (!check(w,h))
		fprintf(stderr,"Error",T);
	fprintf(stderr,")\n");
	sort(A,A+n,cmp);
	rep(i,0,n)
		printf(" %.1lf %.1lf",A[i].x,A[i].y);
	printf("\n");
}

void run()
{
	int t;
	cin>>t;
	rep(i,0,t)
	{
		printf("Case #%d:",i+1);
		test(i+1);
	}
}

#define F_NAME "B-large"
int main()
{
#ifndef F_NAME
		freopen("test.in","r",stdin);
		freopen("test.out","w",stdout);
#else
		freopen(F_NAME".in","r",stdin);
		freopen(F_NAME".out","w",stdout);
#endif
	time_t beg=clock();
	run();
	fprintf(stderr,"Time: %.3lf s.\n",(clock()-beg)/double(CLOCKS_PER_SEC));
	return 0;
}

/*

*/