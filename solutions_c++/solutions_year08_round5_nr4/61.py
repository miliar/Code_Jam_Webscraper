#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <sstream>
#include <iostream>
#include <math.h>
#include <stdio.h>

#define LL long long

using namespace std;

bool ada[200][200];

int H,W,R;

int dp[200][200];

int incx[] = {2,1};
int incy[] = {1,2};

int go(int y, int x) {
	if (y<0 || y>H || x<0 || x>W) return 0;
	if (ada[y][x]) return 0;
	if (y==H && x==W) return 1;
	int &ans=dp[y][x];
	if (ans!=-1) return ans;
	ans=0;
	int i;
	for (i=0; i<2; i++) {
		int ny=y+incy[i];
		int nx=x+incx[i];
		ans+=go(ny,nx);
		ans%=10007;
	}
	return ans;
}


int main() {
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int t,T;
	int i;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		memset(dp,-1,sizeof(dp));
		memset(ada,0,sizeof(ada));

		scanf("%d %d %d", &H, &W, &R);
		for (i=0; i<R; i++) {
			int r,c;
			scanf("%d %d", &r, &c);
			ada[r][c]=true;
		}
		int ans=go(1,1);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}

