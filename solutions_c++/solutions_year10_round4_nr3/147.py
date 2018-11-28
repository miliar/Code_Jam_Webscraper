#include <stdio.h>
#include <memory.h>

int map[110][110],after[110][110], x1, y1, x2, y2, R;
int main(){
	freopen("input.txt","r", stdin);
	freopen("output.txt","w",stdout);
	int T,t,i,j, sol;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		memset(map, 0, sizeof(map));
		scanf("%d",&R);
		int i, j, k;
		for(i=0;i<R;i++){
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for(j=x1;j<=x2;j++){
				for(k=y1;k<=y2;k++){
					map[j][k] = 1;
				}
			}
		}
		for(sol = 0; ; sol ++){
			memset(after, 0, sizeof(after));
			bool okay = false;
			for(i=1;i<=100;i++){
				for(j=0;j<=100;j++){
					if(map[i][j] == 1) okay = true;
					if(map[i][j] == 1 && (map[i-1][j] == 1 || map[i][j-1] == 1)) after[i][j] = 1;
					if(map[i][j] == 0 && map[i-1][j] == 1 && map[i][j-1] == 1) after[i][j] = 1;
				}
			}
			if(!okay) break;
			for(i=1;i<=100;i++){
				for(j=1;j<=100;j++){
					map[i][j] = after[i][j];
				}
			}
		}
		printf("Case #%d: %d\n", t, sol);
	}
	return 0;
}