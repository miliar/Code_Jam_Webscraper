#include "H.h"
#ifdef ProC

//This template is CopyRight By WenX(R), SEU, P.R.China//wenxiao1992@gmail.com//This is for GCJ 2010 Round 3//2010-6-12
#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#pragma warning (disable: 4996)

//SYS
#include <iostream>
#include <string>/////////
#include <cstring>////////This two
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
//ALG
#include <list>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <algorithm>
///Unknown
#include <cstddef>
#include <cassert>///?
#include <sstream>///?
#include <functional>
#include <numeric>
#include <utility>
#include <climits>
#include <numeric>

using namespace std;

#define fori(n)	 for(i=0;i<n;i++)
#define forj(n)  for(j=0;j<n;j++)
#define fork(n)  for(k=0;k<n;k++)
#define fori1(n) for(i=1;i<=n;i++)
#define forj1(n) for(j=1;j<=n;j++)
#define fork1(n) for(k=1;k<=n;k++)
#define FOR(i,n) for(i=0;i<n;i++)

typedef vector<int> vi;
typedef vector<string> vs;

#define pub(x) push_back(x)
#define puf(x) push_front(x)
#define pob(x) pop_back(x)
#define pof(x) pop_front(x)

const double pi=acos(-1.0);
const double eps=1e-9;
const long dx[]={1,0,-1,0};
const long dy[]={0,1,0,-1};
#define zero(f){f>0?(f<eps):(f>-eps)}//ONLY for float and double

template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
template<class T> inline int countbit(T n)
{return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(
template<class T> inline T gcd(T a,T b)//NOTES:gcd(
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//NOTES:lcm(
{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber(
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}

int ss[1300000];
int qss[1300000];
int notgood[1300000];
int numss[1300000];
int pss;


char g[501][501];

int main()
{
	int T,R,C,D;
	int i,j,ii,jj,ix,iy,tot;
	//freopen("B.in","r",stdin);
	//freopen("Bout.txt","w",stdout);
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		scanf("%d%d%d",&R,&C,&D);
		for (int i=0;i<R;i++)
		{
			scanf("%s",&g[i]);
			for (int j=0;j<C;j++) g[i][j]-='0';
		}
		int d=R;
		int ans=-1;
		if (C<d) d=C;
		for (;d>=3;d--)
		{
			for (i=0;i<R-d+1;i++)
				for (j=0;j<C-d+1;j++)
				{
					ix=0,iy=0,tot=0;
					for (ii=i;ii<i+d;ii++)
						for (jj=j;jj<j+d;jj++)
						{
							ix+=ii*g[ii][jj];
							iy+=jj*g[ii][jj];
							tot+=g[ii][jj];
						}
					tot-=g[i][j]+g[i][j+d-1]+g[i+d-1][j]+g[i+d-1][j+d-1];
					ix-=i*(g[i][j]+g[i][j+d-1])+(i+d-1)*(g[i+d-1][j]+g[i+d-1][j+d-1]);
					iy-=j*(g[i][j]+g[i+d-1][j])+(j+d-1)*(g[i][j+d-1]+g[i+d-1][j+d-1]);
					if (d%2==1&&ix==(i+d/2)*tot&&iy==(j+d/2)*tot||
						d%2==0&&ix*2==(2*i+d-1)*tot&&iy*2==(2*j+d-1)*tot)
					{
						ans=d;
						goto lab;
					}
				}
		}
lab:
		if (ans!=-1)
			printf("Case #%d: %d\n",cas,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",cas);


	}
	return 0;
}



#endif