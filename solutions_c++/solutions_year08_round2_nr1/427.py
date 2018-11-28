#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SZ(x) (int)x.size()

LL dp[100010][3][3],np[3][3];
VLL x,y;

void main()
{
	int probnum,numtest;
	string ins;
	cin>>numtest;
	//numtest=atoi(ins.c_str());
	for(probnum=0;probnum<numtest;probnum++)
	{
		int i,j,k;
		LL A,B,C,D,x0,y0,M,n,a,b;
		printf("Case #%d: ",probnum+1);
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;

		a=x0;b=y0;
		x.clear();y.clear();
		x.PB(a);y.PB(b);
		for(i=1;i<=n-1;i++)
		{
			a= (A*a+B)%M;
			b= (C*b+D)%M;
			x.PB(a);y.PB(b);
		}
		memset(dp,-1,sizeof(dp));
		memset(np,0,sizeof(np));
		LL res=0;
		for(i=0;i<3;i++)for(j=0;j<3;j++)dp[0][i][j]=0;
		np[x[0]%3][y[0]%3]++;
		for(i=1;i<n;i++)
		{
			int t1,t2,xr,yr;
			t1=x[i]%3;t2=y[i]%3;xr=(3-t1)%3;yr=(3-t2)%3;
			res+= dp[i-1][xr][yr];
			for(j=0;j<3;j++)for(k=0;k<3;k++)dp[i][(t1+j)%3][(t2+k)%3] = np[j][k] + dp[i-1][(t1+j)%3][(t2+k)%3];
			np[t1][t2]++;

		}
		cout<<res<<endl;
		
	}
}