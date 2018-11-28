#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
#define mod 10007
typedef long long ll;
typedef vector<int> VI;

int U,N, i,j,r, w,h,u;
int a[101][101];

int main()
{
	freopen("d-small.in","r",stdin);//large-small
	freopen("d-small.out","w",stdout);
	scanf("%d",&N);
	rep(U,N)
	{
		scanf("%d%d%d",&h,&w,&r);
		mset(a,0);
		rep(u,r)
		{
			scanf("%d%d",&i,&j);
			a[i-1][j-1]=-1;
		}
		a[0][0]=1;
		forr(i,1,h-1) forr(j,1,w-1) if(a[i][j]!=-1)
		{
			if(i>1 && a[i-2][j-1]!=-1) a[i][j]=a[i-2][j-1];
			if(j>1 && a[i-1][j-2]!=-1) a[i][j]=(a[i][j]+a[i-1][j-2]) % mod;
		}			 
		printf("Case #%d: %d\n",U+1,a[h-1][w-1]);		
	}
	return 0;
}
