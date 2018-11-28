#include <cstdio>
#include <memory.h>
int g[11111];
int c[11111];
bool d[11111][2];
int a[11111][2];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tt=1; tt<=t; tt++){
		memset(g,0,sizeof(g));
		memset(c,0,sizeof(c));
		memset(d,0,sizeof(d));
		memset(a,0,sizeof(a));
		int n,m;
		scanf("%d %d\n",&n,&m);
		for(int i=1; i<=(n-1)/2; i++){
			scanf("%d %d\n",&g[i],&c[i]);
		}
		for(int i=(n-1)/2+1; i<=n; i++){
			int t;
			scanf("%d\n",&t);
			d[i][t] = true;
			d[i][1-t] = false;
		}
		for(int i=(n-1)/2; i>=1; i--){
			if(g[i]==1){
				if(d[i*2][1] && d[i*2+1][1]){
					if(d[i][1]==false){
						d[i][1] = true;
						a[i][1] = a[i*2][1]+a[i*2+1][1];
					}
					else if(a[i][1] > a[i*2][1]+a[i*2+1][1])
						a[i][1] = a[i*2][1] + a[i*2+1][1];
				}
				if(d[i*2][1] && d[i*2+1][0]){
					if(d[i][0]==false){
						d[i][0] = true;
						a[i][0] = a[i*2][1]+a[i*2+1][0];
					}
					else if(a[i][0] > a[i*2][1]+a[i*2+1][0])
						a[i][0] = a[i*2][1]+a[i*2+1][0];
				}
				if(d[i*2][0] && d[i*2+1][1]){
					if(d[i][0]==false){
						d[i][0] = true;
						a[i][0] = a[i*2][0]+a[i*2+1][1];
					}
					else if(a[i][0] > a[i*2][0]+a[i*2+1][1])
						a[i][0] = a[i*2][0]+a[i*2+1][1];
				}
				if(d[i*2][0] && d[i*2+1][0]){
					if(d[i][0]==false){
						d[i][0] = true;
						a[i][0] = a[i*2][0]+a[i*2+1][0];
					}
					else if(a[i][0] > a[i*2][0]+a[i*2+1][0])
						a[i][0] = a[i*2][0]+a[i*2+1][0];
				}
			}
			else{
				if(d[i*2][1] && d[i*2+1][1]){
					if(d[i][1]==false){
						d[i][1] = true;
						a[i][1] = a[i*2][1]+a[i*2+1][1];
					}
					else if(a[i][1] > a[i*2][1]+a[i*2+1][1])
						a[i][1] = a[i*2][1] + a[i*2+1][1];
				}
				if(d[i*2][1] && d[i*2+1][0]){
					if(d[i][1]==false){
						d[i][1] = true;
						a[i][1] = a[i*2][1]+a[i*2+1][0];
					}
					else if(a[i][1] > a[i*2][1]+a[i*2+1][0])
						a[i][1] = a[i*2][1] + a[i*2+1][0];
				}
				if(d[i*2][0] && d[i*2+1][1]){
					if(d[i][1]==false){
						d[i][1] = true;
						a[i][1] = a[i*2][1]+a[i*2+1][1];
					}
					else if(a[i][1] > a[i*2][0]+a[i*2+1][1])
						a[i][1] = a[i*2][0] + a[i*2+1][1];
				}
				if(d[i*2][0] && d[i*2+1][0]){
					if(d[i][0]==false){
						d[i][0] = true;
						a[i][0] = a[i*2][0]+a[i*2+1][0];
					}
					else if(a[i][1] > a[i*2][0]+a[i*2+1][0])
						a[i][0] = a[i*2][0] + a[i*2+1][0];
				}
			}
			if(c[i]==1){
				if(g[i]==0){
					if(d[i*2][1] && d[i*2+1][1]){
						if(d[i][1]==false){
							d[i][1] = true;
							a[i][1] = a[i*2][1]+a[i*2+1][1]+1;
						}
						else if(a[i][1] > a[i*2][1]+a[i*2+1][1]+1)
							a[i][1] = a[i*2][1] + a[i*2+1][1]+1;
					}
					if(d[i*2][1] && d[i*2+1][0]){
						if(d[i][0]==false){
							d[i][0] = true;
							a[i][0] = a[i*2][1]+a[i*2+1][0]+1;
						}
						else if(a[i][0] > a[i*2][1]+a[i*2+1][0]+1)
							a[i][0] = a[i*2][1]+a[i*2+1][0]+1;
					}
					if(d[i*2][0] && d[i*2+1][1]){
						if(d[i][0]==false){
							d[i][0] = true;
							a[i][0] = a[i*2][0]+a[i*2+1][1]+1;
						}
						else if(a[i][0] > a[i*2][0]+a[i*2+1][1]+1)
							a[i][0] = a[i*2][0]+a[i*2+1][1]+1;
					}
					if(d[i*2][0] && d[i*2+1][0]){
						if(d[i][0]==false){
							d[i][0] = true;
							a[i][0] = a[i*2][0]+a[i*2+1][0]+1;
						}
						else if(a[i][0] > a[i*2][0]+a[i*2+1][0]+1)
							a[i][0] = a[i*2][0]+a[i*2+1][0]+1;
					}
				}
				else{
					if(d[i*2][1] && d[i*2+1][1]){
						if(d[i][1]==false){
							d[i][1] = true;
							a[i][1] = a[i*2][1]+a[i*2+1][1]+1;
						}
						else if(a[i][1] > a[i*2][1]+a[i*2+1][1]+1)
							a[i][1] = a[i*2][1] + a[i*2+1][1]+1;
					}
					if(d[i*2][1] && d[i*2+1][0]){
						if(d[i][1]==false){
							d[i][1] = true;
							a[i][1] = a[i*2][1]+a[i*2+1][0]+1;
						}
						else if(a[i][1] > a[i*2][1]+a[i*2+1][0]+1)
							a[i][1] = a[i*2][1] + a[i*2+1][0]+1;
					}
					if(d[i*2][0] && d[i*2+1][1]){
						if(d[i][1]==false){
							d[i][1] = true;
							a[i][1] = a[i*2][1]+a[i*2+1][1]+1;
						}
						else if(a[i][1] > a[i*2][0]+a[i*2+1][1]+1)
							a[i][1] = a[i*2][0] + a[i*2+1][1]+1;
					}
					if(d[i*2][0] && d[i*2+1][0]){
						if(d[i][0]==false){
							d[i][0] = true;
							a[i][0] = a[i*2][0]+a[i*2+1][0]+1;
						}
						else if(a[i][0] > a[i*2][0]+a[i*2+1][0]+1)
							a[i][0] = a[i*2][0] + a[i*2+1][0]+1;
					}
				}
			}
		}
		if(d[1][m])
			printf("Case #%d: %d\n",tt,a[1][m]);
		else
			printf("Case #%d: IMPOSSIBLE\n",tt);
	}
	return 0;
}