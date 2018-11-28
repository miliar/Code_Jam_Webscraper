#include <stdio.h>
#include <string.h>

int a[2][120][120];

int main(){
	int T;
	scanf("%d", &T);
	for(int TT=1;TT<=T;TT++){
		int r;
		scanf("%d", &r);
		memset(a,0,sizeof(a));
		for(int i=0;i<r;i++){
			int x1,x2,y1,y2;
			scanf("%d%d%d%d", &x1,&y1,&x2,&y2);
			for(int xx=x1;xx<=x2;xx++){
				for(int yy=y1;yy<=y2;yy++){
					a[0][xx][yy]=1;
				}
			}
		}
		int ret;
		bool ok=1;
		for(ret=0;ok;ret++){
			ok=0;
			int now = ret%2;
			int next = 1-now;
			for(int i=1;i<=100;i++){
				for(int j=1;j<=100;j++){
					a[next][i][j] = 0;
					if(a[now][i][j]){
						if(!(a[now][i][j-1] || a[now][i-1][j])){
							a[next][i][j] = 0;
						}else{
							a[next][i][j] = 1;
							ok=1;
						}
					}
					if(a[now][i][j-1] && a[now][i-1][j]){
						a[next][i][j] = 1;
						ok=1;
					}
				}
			}
		}
		printf("Case #%d: %d\n", TT, ret);
	}
}