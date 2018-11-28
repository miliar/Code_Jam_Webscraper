#include<cstdio>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
#include<cmath>
#include<cstdlib>
using namespace std;


int tc;
int n,m,d;
char g[505][505];
double tx,ty;

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d",&tc);
    for (int T=1; T<=tc; T++) {
		scanf("%d%d%d",&n,&m,&d);
		for (int i=0; i<n; i++)
			scanf("%s",g[i]);
		int ret=0;
		for (int i=1; i<n-1; i++)
			for (int j=1; j<m-1; j++) {
				for (int k=3; k<=min(n,m); k++)
					if (i-k/2>=0 && i-k/2+k-1<n && j-k/2>=0 && j-k/2+k-1<m) {
						//printf("%d %d %d\n",i,j,k);
						tx=0; ty=0;
						for (int x=0; x<k; x++)
							for (int y=0; y<k; y++) 
								if (x+y!=0 && x+y!=2*(k-1) && !((x==0 || y==0) && x+y==k-1)) {
									tx+=(x-(k-1.0)/2)*(d+(g[i-k/2+x][j-k/2+y]-'0'));
									ty+=(y-(k-1.0)/2)*(d+(g[i-k/2+x][j-k/2+y]-'0'));
									//if (k==4) printf("%d %.3f\n",x,(k-1.0)/2);
									//printf("  %d,%d  %d %d %f\n",x,y,k/2,d+(g[i-k/2+x][j-k/2+y]-'0'),tx);
								}
						//printf("%f %f\n",tx,ty);
						if (abs(tx)<1e-4 && abs(ty)<1e-4) {
							ret=max(k,ret);
							//printf("%d %d %d\n",i,j,k);
						}
					}
			}
		if (ret>0) printf("Case #%d: %d\n",T,ret);
		else printf("Case #%d: IMPOSSIBLE\n",T);
	}
}
