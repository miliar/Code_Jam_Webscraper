#include <cstdio>
#include <string>
#include <map>
using namespace std;

int dp[1010];
int n;
char s[1000];
map<string,int> save;


int main() {
int z,zz,i,j,k,x;
	for (scanf("%d",&zz),gets(s),z=1;z<=zz;++z) {
		save.clear();
		for (scanf("%d",&n),gets(s),i=0;i<n;++i) {
			gets(s);
			dp[save[s]=i]=0;
		}
		for (scanf("%d",&j),gets(s);j;--j) {
			gets(s);
			x=save[s];
			k=100000;
			for (i=0;i<n;++i) {
				if (dp[i]<k) {
					k=dp[i];
				}
			}
			for (i=0;i<n;++i) {
				if (dp[i]>k+1) {
					dp[i]=k+1;
				}
			}
			dp[x]=100000;
		}
		for (k=1000000,i=0;i<n;++i) {
			if (dp[i]<k) {
				k=dp[i];
			}
		}
		printf("Case #%d: %d\n",z,k);
	}
	return 0;
}


