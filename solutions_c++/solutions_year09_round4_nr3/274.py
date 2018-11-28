#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;


#define MAXN 310
#define _clr(x) memset(x,0xff,sizeof(int)*MAXN)

int b[MAXN][MAXN],a[MAXN][33],c[MAXN],d[MAXN];

int gao(int i,int j,int k) {
int x;
	for (x=0;x<k;++x) {
		if (a[i][x]<=a[j][x]) {
			return 0;
		}
	}
	return 1;
}



int hungary(int m,int n,int mat[][MAXN],int* match1,int* match2){
	int s[MAXN],t[MAXN],p,q,ret=0,i,j,k;
	for (_clr(match1),_clr(match2),i=0;i<m;ret+=(match1[i++]>=0))
		for (_clr(t),s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (mat[k][j]&&t[j]<0){
					s[++q]=match2[j],t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p)
							match2[j]=k=t[j],p=match1[k],match1[k]=j;
				}

	return ret;
}

int main() {
int z,zz,i,j,n,k;


	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&zz);
	for (z=1;z<=zz;++z) {
		
		scanf("%d%d",&n,&k);
		for (i=0;i<n;++i) {
			for (j=0;j<k;++j) {
				scanf("%d",&a[i][j]);
			}
		}
		for (i=0;i<n;++i) {
			for (j=0;j<n;++j) {
				b[i][j]=gao(i,j,k);
			}
		}
		printf("Case #%d: %d\n",z,n-hungary(n,n,b,c,d));


	}

	
	return 0;
}