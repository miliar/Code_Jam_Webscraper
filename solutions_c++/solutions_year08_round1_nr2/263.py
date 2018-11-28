#include <cstdio>
#include <string>
using namespace std;

bool a[105][12][2];
int n,m,p,ans;

void gao(int now,int may,int state) {
int i,j;

	if (now==n) {
		if ((ans>=0) && (ans<may)) {
			return;
		}
		for (i=0;i<m;++i) {
			for (j=0;j<n;++j) {
				if (a[i][j][(state>>j)&1]) {
					break;
				}
			}
			if (j>=n) {
				return;
			}
		}
		ans=may;
		p=state;
		return;
	}
	gao(now+1,may,state);
	gao(now+1,may+1,state|(1<<now));
}

int main() {
int x,y,z,zz,i,j;
	freopen("d:\\in","r", stdin);
    freopen("d:\\out","w",stdout);


	for (scanf("%d",&zz),z=1;z<=zz;++z){
		scanf("%d%d",&n,&m);
		for (i=0;i<m;++i){
			memset(a[i],0,sizeof(a[0]));
			for (scanf("%d",&j);j;--j){
				scanf("%d%d",&x,&y);
				a[i][--x][y]=true;
				
			}
		}
		ans=-1;
		p=0;
		gao(0,0,0);
		printf("Case #%d:",z);
		if (ans>=0) {
			for (i=0;i<n;++i) {
				printf(" %d",(p>>i)&1);
			}
			puts("");
		}
		else {
			puts(" IMPOSSIBLE");
		}
	}
	return 0;
}
			


