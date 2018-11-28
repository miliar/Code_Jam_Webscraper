#include <iostream>
#include <sstream>
#include <cstdio>
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
typedef long long ll;
typedef vector<int> VI;

int i,j,n,m,a, U,N;
int x1,y1,x2,y2;

int main()
{
	freopen("b-small.in","r",stdin);//large
	freopen("b-small.out","w",stdout);
	scanf("%d",&N);
	rep(U,N)
	{
		scanf("%d%d%d",&n,&m,&a); n++; m++;
		printf("Case #%d: ",U+1);
		rep(x1,n) rep(y1,m) rep(x2,n) rep(y2,m)
			if((x1*y2)-(x2*y1)==a) { printf("0 0 %d %d %d %d\n",x1,y1,x2,y2); goto go; }
		printf("IMPOSSIBLE\n");
		go:;
	}
	getchar();
	return 0;
}
