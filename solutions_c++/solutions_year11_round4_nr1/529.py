#include "H.h"
#ifdef ProA

//This template is CopyRight By WenX(R), SEU, P.R.China
//wenxiao1992@gmail.com
//This is for GCJ 2010 Round 3
//2010-6-12
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
#define abs(f) (f>0?(f):(-f))


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


int leasts[105];

struct walkway{
	double len;
	int spd;
};

int cmps(const void *a,const void *b){
	return (*(walkway*)a).spd>(*(walkway*)b).spd?1:-1;
}

walkway way[1500];
int waynum;

int main(void)
{	
	int cc,tt;
	int x,s,r,t,n,i;
	int b,e,w;
	double tttime;
	int normalwalkway;
	double remainrunningtime;
	scanf("%d",&tt);
	for(cc=0;cc<tt;cc++){
		scanf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		normalwalkway=x;
		waynum=1;
		for(i=0;i<n;i++){
			scanf("%d%d%d",&b,&e,&w);
			way[waynum].len=e-b;
			way[waynum].spd=w;
			normalwalkway-=(e-b);
			waynum++;
		}
		way[0].len=normalwalkway;
		way[0].spd=0;

		qsort(way,waynum,sizeof(way[0]),cmps);
		remainrunningtime=t;
		i=0;
		while(i<waynum&&((double)way[i].len/(way[i].spd+r)<remainrunningtime)){
			way[i].spd+=r;
			remainrunningtime-=way[i].len/(way[i].spd);
			i++;
		}
		if(i<waynum){
			way[i].len-=remainrunningtime*(way[i].spd+r);
			way[waynum].len=remainrunningtime*(way[i].spd+r);
			way[waynum].spd=way[i].spd+r-s;
			waynum++;
		}
		while(i<waynum){
			way[i].spd+=s;
			i++;
		}
		tttime=0;
		for(i=0;i<waynum;i++)
			tttime+=(double)way[i].len/(double)way[i].spd;

		printf("Case #%d: %.7lf\n",cc+1,tttime);
	}


	return 0;
}


#endif
