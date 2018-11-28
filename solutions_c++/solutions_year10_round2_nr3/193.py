#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <iostream>

using namespace std;

int f[1005][1005];

void gao() { 
int i,j,k;
	f[0][0]=1;
	for (i=0;i<=505;++i) {
		f[0][i]=1;
		f[i][0]=0;
	}
	f[0][0]=1;
	for (i=1;i<=505;++i) {
		for (j=1;j<=505;++j) {
			for (k=1;k<=j && k<=i;++k) {
				f[i][j]+=f[i-k][j];
				f[i][j]%=100003;
			}
		}
	}
}



int main() {
int z,i,j,zz,ans;
	freopen("d:\\in.in","r",stdin);
	freopen("d:\\out","w",stdout);

		
	gao();
	for (scanf("%d",&zz),z=1;z<=zz;++z) {
		scanf("%d",&i);
		for (j=ans=0;j<i;++j) {
			ans+=f[i-1-j][j];
			ans%=100003;
		}
		printf("Case #%d: %d\n",z,ans);
	}
	return 0;
}