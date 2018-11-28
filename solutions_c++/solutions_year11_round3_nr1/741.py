#include<cstdio>
#include<cstring>
char g[55][55];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cas,r=1; scanf("%d",&cas);
	while(cas--){
		int n,m;
		scanf("%d%d",&n,&m);
		int ok=1;
		for(int i=0; i<n; i++) {
		    scanf("%s",g[i]);
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				if(g[i][j]=='#'){
					if(i+1<n && j+1<m){
						if(g[i][j+1]=='#' && g[i+1][j]=='#' && g[i+1][j+1]=='#'){
							g[i][j]='/';
							g[i][j+1]='\\';
							g[i+1][j]='\\';
							g[i+1][j+1]='/';
						}
					}
				}
			}
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++) if(g[i][j]=='#') ok=0;
		}
		printf("Case #%d:\n",r++);
		if(ok==0) puts("Impossible\n");
		else {
			for(int i=0; i<n; i++){
				for(int j=0; j<m; j++){
					printf("%c",g[i][j]);
				}
				puts("");
			}
		}
	}
}
