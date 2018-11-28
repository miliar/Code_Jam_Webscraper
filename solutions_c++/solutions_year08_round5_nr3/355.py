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


int dp[2][2048];

int find(long x) {
	x=(x&0x55555555)+((x>>1)&0x55555555);
	x=(x&0x33333333)+((x>>2)&0x33333333);
	x=(x&0x0F0F0F0F)+((x>>4)&0x0F0F0F0F);
	x=(x&0x00FF00FF)+((x>>8)&0x00FF00FF);
	x=(x&0x0000FFFF)+((x>>16)&0x0000FFFF);
	return (int) x;
}

inline int make0(int x,int y) {
	return (x&(~(1<<y)));
}

inline int make1(int x,int y) {
	return (x|(1<<y));
}

inline int gao(int x,int y) {
	return (x&(1<<y));
}

char s[55];

int main() {
int m,mm,h,j,k,n,zz,i,z,xx,yy,x,y,last,now,ans;
	freopen("d:\\in","r",stdin);
	freopen("d:\\out","w",stdout);
	scanf("%d",&zz);
	for (z=1;z<=zz;++z) {
		scanf("%d%d",&m,&n);
		memset(dp[0],0,sizeof(dp[0]));
		mm=(1<<n);
		for (i=last=ans=0;i<m;++i) {
			scanf("%s",s);
			memset(dp[now=1-last],0,sizeof(dp[0]));
			for (k=0;k<mm;++k) {
				for (h=0;h<mm;++h) {
					for (j=0;j<n;++j) {
						if ((s[j]=='x') && gao(h,j)) {
							break;
						}
						if (gao(h,j)==0) {
							continue;
						}
						if ((j) && gao(k,j-1)) {
							break;
						}
						if ((j+1<n) && (gao(k,j+1))) {
							break;
						}
						if ((j) && gao(h,j-1)) {
							break;
						}
						if ((j+1<n) && (gao(h,j+1))) {
							break;
						}
					}
					if (j<n) {
						continue;
					}
					x=dp[last][k]+find(h);
					if (x>dp[now][h]) {
						dp[now][h]=x;
						if (ans<x) {
							ans=x;
						}
					}
				}
			}
			last=now;
		}

		printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}


