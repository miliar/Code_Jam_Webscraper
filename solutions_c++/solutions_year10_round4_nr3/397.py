#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;
int TT;
int R;
char grid[128][128];
char aux[128][128];
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		printf("Case #%d: ",T);
		scanf("%d",&R);
		memset(grid,'0',sizeof(grid));
		memset(aux,'0',sizeof(aux));
		for(int i=0;i<R;i++) {
			int x1,y1,x2,y2;
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for(int i=y1;i<=y2;i++)
				for(int j=x1;j<=x2;j++)
					grid[i][j]='1';
		}

		int ans=0;

		for(bool tem=true;tem;ans++) {
			tem=false;
			for(int i=1;i<=100;i++)
				for(int j=1;j<=100;j++) {
					aux[i][j]='0';
					if(grid[i][j]=='1') {
						if(grid[i-1][j]=='1' or grid[i][j-1]=='1') {
							aux[i][j]='1';
							tem=true;
						}
					}
					else {
						if(grid[i-1][j]=='1' and grid[i][j-1]=='1') {
							aux[i][j]='1';
							tem=true;
						}
					}
				}
			memcpy(grid,aux,sizeof(aux));
		}

		printf("%d\n",ans);
	}
	return 0;
}
