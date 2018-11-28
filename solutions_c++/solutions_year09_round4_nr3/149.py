#include <iostream>

using namespace std;

int n,m,p[150][150],link[150];
bool g[150][150],h[150];

bool find(int k){
	for (int i=1; i<=n; ++i)
		if ((! h[i]) && g[k][i]){
			h[i] = true;
			if (link[i] == 0 || find(link[i])){
				link[i] = k; return true;
			}
		}
	return false;
}

int main(){
	freopen("C.in","r",stdin); freopen("C.out","w",stdout);
	int t1,t2 = 0;
	scanf("%d\n",&t1);
	while (t1){
		t1--; t2+= 1;
		printf("Case #%d: ",t2);
		scanf("%d %d\n",&n,&m);
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=m; ++j)
				scanf("%d",&p[i][j]);
		for (int i=1; i<=n; ++i)
			for (int j=1; j<=n; ++j){
				g[i][j] = true;
				for (int k=1; k<=m; ++k)
					if (p[i][k] >= p[j][k]){
						g[i][j] = false; break;
					}
			}
		memset(link,0,sizeof(link));
		int ans = n;
		for (int i=1; i<=n; ++i){
			memset(h,false,sizeof(h));
			if (find(i)) ans -= 1;
		}
		printf("%d\n",ans);
	}
}
