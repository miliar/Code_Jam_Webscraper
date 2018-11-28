#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

bool mark[1000][1000];
int dp[1000][1000];

int main() {
int m,n,zz,i,z,xx,yy,x,y;
	freopen("d:\\in","r",stdin);
	freopen("d:\\out","w",stdout);
	scanf("%d",&zz);
	for (z=1;z<=zz;++z) {
		scanf("%d%d",&m,&n);
		memset(dp,0,sizeof(dp));
		memset(mark,0,sizeof(mark));
		dp[0][0]=1;
		for (scanf("%d",&i);i;--i) {
			scanf("%d%d",&x,&y);
			mark[x-1][y-1]=true;
		}
		for (x=0;x<m;++x) {
			for (y=0;y<n;++y) {
				for (xx=1;xx<=x;++xx) {
					for (yy=1;yy<=y;++yy) {
						if ((xx*xx+yy*yy==5) && (x>=xx) && (y>=yy) && (!mark[x-xx][y-yy])) {
							dp[x][y]+=dp[x-xx][y-yy];
							dp[x][y]%=10007;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",z,dp[m-1][n-1]);
	}
	return 0;
}


