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
#include <queue>
using namespace std;

char p[2][105][105];
int m,n,last,now;

int west(int x,int y) {
	if (y==0) {
		return 0;
	}
	return p[last][x][y-1]!='0';
}

int north(int x,int y) {
	if (x==0) {
		return 0;
	}
	return p[last][x-1][y]!='0';
}

int main() {
int z,zz,x1,y1,x2,y2,ans,num,t,i,j;
	freopen("d:\\in.in","r",stdin);
	freopen("d:\\out","w",stdout);

	for (scanf("%d",&zz),z=1;z<=zz;++z) {
		printf("Case #%d: ",z);
		m=n=num=0;
		memset(p,'0',sizeof(p));
		for (scanf("%d",&t);t;--t) {
			scanf("%d%d%d%d",&y1,&x1,&y2,&x2);
			--x1;
			--x2;
			--y1;
			--y2;
			
			if (x2>m) {
				m=x2;
			}
			if (y2>n) {
				n=y2;
			}
			for (i=x1;i<=x2;++i) {
				for (j=y1;j<=y2;++j) {
					p[0][i][j]='1';
					++num;
				}
			}
		}
		for (i=0;i<=m;++i) {
			p[0][i][n+1]=0;
		}
		for (ans=last=0;num;++ans) {
			memcpy(p[now=1-last],p[last],sizeof(p[0]));
			for (i=num=0;i<=m;++i) {
				for (j=0;j<=n;++j) {
					if ((p[last][i][j]=='1') && (!north(i,j)) && (!west(i,j))) {
						p[now][i][j]='0';
					}
					if ((p[last][i][j]=='0') && (north(i,j)) && (west(i,j))) {
						p[now][i][j]='1';

					}
					if (p[now][i][j]=='1') {
						++num;
					}
				}
			}
			last=now;
		}
		printf("%d\n",ans);

			

		
	}
	return 0;
}