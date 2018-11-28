#include <algorithm>
#include <iostream>
#include <complex>
#include <numeric>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define sz(a) int((a).size())
#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define REP(i,n) FOR(i,0,n)
#define UN(a) sort(all(a)),(a).erase(unique(all(a)), (a).end())
#define CL(a,b) memset(a,b,sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

#define N 110

bool a[2][N][N];
int n,r,X1,Y1,X2,Y2,page;

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int test;
	scanf("%d",&test);
	REP(t,test)
	{
		scanf("%d",&r);
		memset(a,0,sizeof(a));
		page=0;
		REP(i,r)
		{
			scanf("%d%d%d%d",&X1,&Y1,&X2,&Y2);
			FOR(j,X1,X2+1)
				FOR(k,Y1,Y2+1)
					a[page][j][k]=1;
		}
		bool flag=1;
		int time=0;
		while(flag)
		{
			page=1-page;
			memset(a[page],0,sizeof(a[page]));
			++time;
			flag=0;
			FOR(i,1,N)
				FOR(j,1,N)
					if(a[1-page][i][j] && (a[1-page][i-1][j] || a[1-page][i][j-1]) ||
					   a[1-page][i-1][j] && a[1-page][i][j-1])
					   	{
							a[page][i][j]=1;
							flag=1;
						}
		}
		printf("Case #%d: %d\n",t+1,time);
	}
	return 0;
}
