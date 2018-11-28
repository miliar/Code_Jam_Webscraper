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

int W,H;
int dx1,dy1,dx2,dy2;
int ans;
bool flag[110][110];

void go(int x,int y)
{
	if(x<0 || x>=W || y<0 || y>=H) return;
	if(flag[x][y]) return;
	flag[x][y]=1;
	ans++;

	go(x+dx1,y+dy1);
	go(x+dx2,y+dy2);
}

void solve()
{
	int x,y;
	scanf("%d%d",&W,&H);
	scanf("%d%d",&dx1,&dy1);
	scanf("%d%d",&dx2,&dy2);
	scanf("%d%d",&x,&y);

	memset(flag,0,sizeof(flag));
	ans=0;
	go(x,y);
	printf("%d",ans);
}

int main()
{	
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		printf("Case #%d: ",t);
		solve();
		printf("\n");
	}


	return 0;
}
