#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

#define size(x) int((x).size())
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
typedef long long I64; typedef unsigned long long U64;
const double EPS=1e-12;
const int INF=999999999;
typedef vector<int> VI;
typedef vector<string> VS;

const int MOD=10007;

int m,n;
int na;
int f[101][101];
bool flag[101][101];

int com(int x,int y)
{
	if(x>m || y>n) return 0;
	if(flag[x][y]) return 0;
	if(x==m && y==n) return 1;
	int &res=f[x][y];
	if(res>=0) return res;

	res=com(x+1,y+2);
	res=(res+com(x+2,y+1))%MOD;
	return res;
}

void solve()
{
	scanf("%d%d%d",&m,&n,&na);
	memset(flag,0,sizeof(flag));
	for(int i=0;i<na;i++) {
		int x,y;
		scanf("%d%d",&x,&y);
		flag[x][y]=1;
	}

	memset(f,-1,sizeof(f));
	printf("%d",com(1,1));
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		solve();
		printf("\n");
	}

	return 0;
}
