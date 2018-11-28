#include <iostream>
#include <vector>
#include <cmath>
#include <cstring>
#include <algorithm>
// #include <set>
// #include <map>
// #include <queue>
#define pb push_back
#define fi first
#define se second
#define INF 1000000000
#define MOD 10007
using namespace std;
typedef long long ll;
typedef pair<int,int> pi;
typedef pair<int,pi> pii;
int solve()
{
	int t[201][201];
	int x,y,k;
	scanf("%d %d %d",&x,&y,&k);
	for (int i=0; i<=x; i++)
		for (int j=0; j<=y; j++)
			t[i][j]=0;
	for (int i=0; i<k; i++)
	{
		int a,b;
		scanf("%d %d",&a,&b);
		t[a][b]=-1;
	}
	t[1][1]=1;
	for (int i=1; i<=x; i++)
		for (int j=1; j<=y; j++)
		{
			if (t[i][j]<0) continue;
			t[i][j]%=MOD;
			if (t[i+2][j+1]>=0) t[i+2][j+1]+=t[i][j];
			if (t[i+1][j+2]>=0) t[i+1][j+2]+=t[i][j];
			//printf("%d %d : %d %d %d  %d\n",i,j,t[i][j],t[i+1][j+2],t[i+2][j+1],t[x][y]);
		}
	return t[x][y];
}

int main()
{
	int tests;
	scanf("%d",&tests);
	for (int te=1; te<=tests; te++)
	{
		int w=solve();
		printf("Case #%d: %d\n",te,w);
	}
}
