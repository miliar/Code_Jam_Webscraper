#include "tem.h"

#ifdef ProbC

//This template is CopyRight By WenX(R), SEU, P.R.China
//wenxiao1992@gmail.com
//2010-5-24
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

void maxs(long &i,long &max){
	if(i>max||max==-1)
		max=i;
}
void mins(long &i,long &min){
	if(i<min||min==-1)
		min=i;
}

#define MAXN 1111
#define MAXN 100000
#define _ufind_run(x) for(;p[t=x];x=p[x],p[t]=(p[x]?p[x]:x))
#define _run_both _ufind_run(i);_ufind_run(j)

struct ufind{
	int p[MAXN],t;
	void init(){memset(p,0,sizeof(p));}
	void set_friend(int i,int j){_run_both;p[i]=(i==j?0:j);}
	int is_friend(int i,int j){_run_both;return i==j&&i;}
};


long index[1111][4];
int touch(int i,int j){
	if(min(index[i][2],index[j][2])>=max(index[i][0],index[j][0])&&
		min(index[i][3],index[j][3])>=max(index[i][1],index[j][1]))
		if(index[i][2]==index[j][0]&&index[i][3]==index[j][1])
			return 0;
		else if(index[j][2]==index[i][0]&&index[j][3]==index[i][1])
			return 0;
		else
		return 1;
	else
		return 0;
}

int main(void)
{
	ufind u;
	long cc,tt;
	scanf("%d",&tt);
	long maxx,maxy,minx,miny;
	int vis[1111];
	long nextminx,nextmaxx,nextminy,nextmaxy;
	long k,i,j;
	long time;
	long leftmost;
	long maxleft;long ans;

	
	long x1,x2,y1,y2;
	long x,y;

	for(cc=0;cc<tt;cc++){
		scanf("%d",&k);
		for(i=1;i<=k;i++)
			for(j=0;j<4;j++){
				scanf("%d",&index[i][j]);
				if(j<2)
					index[i][j]--;
			}
		u.init();
		for(i=1;i<=k;i++)
			for(j=1;j<=k;j++)
				if(touch(i,j))
					u.set_friend(i,j);

		leftmost=maxleft=3000000 ;ans=-1;
		memset(vis,0,sizeof(vis));
		for(i=1;i<=k;i++){
			if(!vis[i]){
				maxx=maxy=-1;
				maxleft=3000000;
				for(j=1;j<=k;j++)
					if(u.is_friend(i,j)){
						vis[j]=1;
						if(maxx==-1||index[j][2]>maxx)
							maxx=index[j][2];
						if(maxy==-1||index[j][3]>maxy)
							maxy=index[j][3];
						leftmost=index[j][0]+index[j][1];
						if(leftmost<maxleft)
							maxleft=leftmost;
					}
				if(maxx+maxy-maxleft>ans)
					ans=maxx+maxy-maxleft;
			}
		}
		printf("Case #%d: %d\n",cc+1,ans-1);
	}

	return 0;
}


#endif