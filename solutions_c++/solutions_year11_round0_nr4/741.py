// include file
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <ctime>

#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <list>
#include <functional>

using namespace std;

// typedef
typedef __int64 LL;

// 
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)

#define Z(a,b) ((a)<<(b))
#define Y(a,b) ((a)>>(b))

const double eps = 1e-6;
const double INFf = 1e100;
const int INFi = 1000000000;
const LL INFll = (LL)1<<62;
const double Pi = acos(-1.0);

template<class T> inline T sqr(T a){return a*a;}
template<class T> inline T TMAX(T x,T y)
{
	if(x>y) return x;
	return y;
}
template<class T> inline T TMIN(T x,T y)
{
	if(x<y) return x;
	return y;
}
template<class T> inline T MMAX(T x,T y,T z)
{
	return TMAX(TMAX(x,y),z);
}
template<class T> inline T MMIN(T x,T y,T z)
{
	return TMIN(TMIN(x,y),z);
}
template<class T> inline void SWAP(T &x,T &y)
{
	T t = x;
	x = y;
	y = t;
}


// code begin
// 是这么做的
/*
	对于要调整m个
	p = 1/m
	q = 1-q;
	s = 1*1/m + 2*((m-1)/m)^1*1/m + 3*((m-1)/m)^2*1/m + ....
	
	s = 1*p + 2*q^1*p + 3*q^2*p + 4*q^3*p + ...
	s/p = 1*1 + 2*q^1 + 3*q^2 + 4*q^3 + ...
	s/(pq) = 1/q + 2 + 3*q + 4*q^2 + ...
	s/(pq)-s/p = 1/q+1+q+q^2+q^3+...
	s/(pq)-s/p = 1/q+(1)/(1-q)
	s/(pq)-s/p = 1/q+1/p
	s/q - s= p/q+1;
	s(1/q-1) = p/q+1
	s = (p/q+1)*(q/(1-q)) = (p/q+1)*(q/p) = (p+q)/p = 1/p;
	当p = 1/3,q = 2/3;
	s = (1/2+1)*(2) = 3
	当p = 1/4,q=3/4
	s = (1/3+1)*(3) = 4

*/
int T,N,data[1010];
bool used[1010];
int main()
{
	freopen("D-large.in","r",stdin);
	write;
	int cas = 1,tmp,loc;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&N);
		for(int i=1;i<=N;i++)
		{
			scanf("%d",data+i);
		}
		double ans = 0;
		for(int i=1;i<=N;i++)
		{
			if(data[i]!=i) ans+=1;
		}
		printf("Case #%d: ",cas++);
		printf("%.6f\n",ans);
	}
	return 0;
}