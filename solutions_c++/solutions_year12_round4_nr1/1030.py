#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <assert.h>

//#pragma warning(disable:4996)
using namespace std;

#define TIME fprintf(stderr,"\n-----------\ntime : %.2f sec\n",double(clock())/CLOCKS_PER_SEC);
#define EXIT exit(0);
#define FIN freopen("input.txt","r",stdin);
#define FOUT freopen("output.txt","w",stdout);
#define INP(_X) scanf("%d",& _X);
#define OUT(_X) printf("%d ",_X);
#define LINE printf("\n");
#define DOUT(_X) fprintf(stderr,"%d ",_X);
#define DLINE fprintf(stderr,"\n");

#define M 10002
#define MOD 0
#define ADD(_X,_Y) _X=(_X+_Y)%MOD;
#define oo 1000000009

#define abs(_Z) (((_Z)<0)?-(_Z):(_Z))
#define f0(_X,_Y) for(_X=0;_X<_Y;++_X)
#define f1(_X,_Y) for(_X=1;_X<=_Y;++_X)
#define ff(_X,_Y,_Z) for(_X=_Y;_X<=_Z;++_X)
#define fF(_X,_Y,_Z) for(_X=_Y;_X<_Z;++_X)
#define pb push_back
#define sz(_X) _X.size()
typedef long long ll;
const double PI=atan2(1.,0);
const int DY[]={0,1,0,-1},DX[]={1,0,-1,0};

struct XY{int x,y;
	XY(int _X=0,int _Y=0){x=_X;y=_Y;}
	bool operator == (const XY &p) const{return x==p.x && y==p.y;}
	bool operator < (const XY &p) const{if(x!=p.x) return x<p.x; return y<p.y;}
	XY operator + (const XY &p) const{return XY(x+p.x,y+p.y);}
	XY operator - (const XY &p) const{return XY(x-p.x,y-p.y);}
	XY operator - () const{return XY(-x,-y);}
	ll norm() const{return (ll)x*x+(ll)y*y;}
};

int x[M],len[M],d[M];
int n,D;

bool reach()
{
	int i,j;

	f1(i,n) d[i]=-1;
	if(len[1]<x[1]) return false;
	d[1]=0; // start with vine 1
	f1(i,n)
	{
		// x[j] <= x[i]*2-d[i] && x[j]-x[i]<=len[j]
		// x[j] <= x[i]*2-d[i] && x[j]-len[j]<=x[i]

		if(d[i]==-1) continue; // unreachable
		if(d[i]<x[i]-len[i]) d[i]=x[i]-len[i];
		ff(j,i+1,n)
		{
			//if(d[j]==-1 && x[j]<=x[i]*2-d[i] && x[j]-len[j]<=x[i])
			if(d[j]==-1 && x[j]<=x[i]*2-d[i])
				d[j]=x[i];
		}
		if(D<=x[i]*2-d[i]) return true;
	}

	return false;
}

int main()
{
	int T,t,i;

	FIN
	FOUT

	INP(t)
	f1(T,t)
	{
		INP(n)
		f1(i,n)
		{
			INP(x[i])
			INP(len[i])
		}
		INP(D)

		printf("Case #%d: ",T);
		if(reach()) printf("YES\n"); else printf("NO\n");
	}
	return 0;
}
