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

const int inf=20000;
const int M=10011;
int v[M];
int c[M];
bool leaf[M];
int g[M];
int dp[M][2];

int m;

inline void better(int &x,int y) {
	if (x>y) {
		x=y;
	}
}

int gao(int now,int want) {
int i,j,r,may,temp;
	if (now>m) {
		return inf;
	}
	if (dp[now][want]>=0) {
		return dp[now][want];
	}
	if (leaf[now]) {
		return (dp[now][want]=(want==v[now])?0:inf);
	}
	r=inf;
	for (i=0;i<2;++i) {
		for (j=0;j<2;++j) {
			may=gao(now*2,i)+gao(now*2+1,j);
			if (g[now]) {
				temp=(i && j)?1:0;
				if (temp==want) {
					better(r,may);
				}
				if (c[now]) {
					temp=(i || j)?1:0;
					if (temp==want) {
						better(r,may+1);
					}
				}
			}
			else {
				temp=(i || j)?1:0;
				if (temp==want) {
					better(r,may);
				}
				if (c[now]) {
					temp=(i && j)?1:0;
					if (temp==want) {
						better(r,may+1);
					}
				}
			}
		}
	}
	return dp[now][want]=r;
}



			





int main() {
int i,j,p,z,zz,w;
	freopen("d:\\in","r",stdin);
	freopen("d:\\out","w",stdout);
	for (scanf("%d",&zz),z=1;z<=zz;++z) {
		printf("Case #%d: ",z);
		scanf("%d%d",&m,&w);
		p=(m-1)>>1;
		for (i=1;i<=p;++i) {
			leaf[i]=false;
			scanf("%d%d",&g[i],&c[i]);
		}
		j=(m+1)>>1;
		for (i=1;i<=j;++i) {
			leaf[i+p]=true;
			scanf("%d",&v[i+p]);
		}
		memset(dp,0xff,sizeof(dp));
		i=gao(1,w);
		if (i>=inf) {
			puts("IMPOSSIBLE");
		}
		else {
			printf("%d\n",i);
		}
	}
	return 0;
}