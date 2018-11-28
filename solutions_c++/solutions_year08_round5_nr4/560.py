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
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)

#define PI 3.14159265358979323846264338327950288
#define mod 10007
//typedef __int64 int64;

int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	//freopen("D-large.in","r",stdin);
	//freopen("D-large.out","w",stdout);
	int cas,ca;
	int map[124][124],a[124][124];
	for(scanf("%d",&cas),ca=1;ca<=cas;ca++)
	{
		int i,j,n,m,t,x,y;
		printf("Case #%d: ",ca);
		scanf("%d%d%d",&n,&m,&t);
		memset(map,0,sizeof(map));
		for(i=0;i<t;i++)
		{
			scanf("%d%d",&x,&y);
			map[x][y]=1;
		}
		memset(a,0,sizeof(a));
		a[1][1]=1;
		for(i=2;i<=n;i++)
			for(j=2;j<=m;j++)
				if(!map[i][j])
				{
					if(i>=3)a[i][j]=(a[i][j]+a[i-2][j-1])%mod;
					if(j>=3)a[i][j]=(a[i][j]+a[i-1][j-2])%mod;
				}
				else a[i][j]=0;
		printf("%d\n",(a[n][m])%mod);
	}
}


