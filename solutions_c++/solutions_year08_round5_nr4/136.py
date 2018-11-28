#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

typedef long long LL;
const int MOD=10007;
int dp[110][110];
bool G[110][110];
int W, H; 
bool can(int x, int y){ return x>=0 && x<W && y>=0 && y<H && G[x][y]; }
int doit(int x, int y){
	if(x==W-1 && y==H-1)
		return 1; 
	int& ref=dp[x][y];
	if(ref!=-1)return ref; 
	ref=0;  
	int xs[2]={2,1};
	int ys[2]={1,2};
	for(int i=0;i<2;++i){
		if(can(x+xs[i],y+ys[i])){
			ref+=doit(x+xs[i],y+ys[i]);
			ref%=MOD; 
		}
	}
	return ref; 
}

int main() {
	int NCASES;
	scanf("%d", &NCASES);
	for (int z=1;z<=NCASES;++z) {
		int R; 
		scanf("%d %d %d\n", &W,&H,&R);
		memset(G,1,sizeof G);
		for(int i=0; i<R; ++i){
			int r, c; 
			scanf("%d %d", &r, &c);
			G[r-1][c-1]=0; 
		}
		memset(dp,-1,sizeof dp);
		printf("Case #%d: %d\n", z,doit(0,0));
	}
}
