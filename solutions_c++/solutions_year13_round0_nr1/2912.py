#include<cstdio>
#include<string>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
char gp[20][20];
int dr[4][2] = {0,1,1,0,1,1,-1,1};
int check() {
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++) {

			for(int k = 0; k < 4; k++) {
				int a = 0,b = 0,cnt = 0,x = i,y = j;
				while(cnt < 4) {
					//printf("%c",gp[x][y]);
					if(gp[x][y] == 'X') a = 1;
					if(gp[x][y] == 'O') b = 1;
					if(gp[x][y] ==  '.') a = 1,b = 1;
					cnt++;
					x = x + dr[k][0],y = y + dr[k][1];
					if(x < 0 || y < 0 || x > 3 || y > 3 )
						break;
				}
				if(cnt == 4 && ((a^b) == 1))
					if(a) return 1;
					else return 2;
			}
		}
		return 0;
}

int main () {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas++) {
		for(int i = 0; i < 4; i++) {
			scanf("%s",gp[i]);
		}
		gets(gp[10]);
		int flag = 0;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) {
				if(gp[i][j] == '.')
					flag = 1;
			}
			printf("Case #%d: ",cas);
			int ans = check();
			if(ans) {
				printf("%s\n",ans > 1?"O won":"X won");
			}else if(flag) puts("Game has not completed");
			else puts("Draw");
	}
	return 0;
}