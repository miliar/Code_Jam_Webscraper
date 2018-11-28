#include<iostream>
#include<memory.h>
using namespace std;

char buf[100][100];
int r, c;
int dx[] = {0, 0, 1, 1};
int dy[] = {0, 1, 0, 1};

bool chk(int x, int y){
	if(x >= 0 && x < r && y >= 0 && y < c)
		return 1;
	return 0;
}

bool find(int &x, int &y){
	for(int i = 0; i < r; i++){
		for(int j = 0; j < c; j++){
			if(buf[i][j] == '#'){
				x = i; y = j;
				return 1;
			}
		}
	}
	return 0;
}

int main(){
	int cas;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &cas);
	for(int t = 0; t < cas; t++){
		scanf("%d%d", &r, &c);
		for(int i = 0; i < r; i++)
			scanf("%s", buf[i]);
		int x, y;
		printf("Case #%d:\n", t + 1);
		bool ans = 1;
		while(find(x, y)){
			bool flg = 1;
			for(int i = 0; i < 4; i++){
				int tx, ty;
				tx = x + dx[i];
				ty = y + dy[i];
				if(!chk(tx, ty) || buf[tx][ty] != '#'){
					flg = 0; ans = 0;
				}
			}
			if(!flg) {printf("Impossible\n"); break;}
			else{
				buf[x][y] = '/';
				buf[x][y + 1] = '\\';
				buf[x + 1][y] = '\\';
				buf[x + 1][y + 1] = '/';
			}
		}
		if(ans){
			for(int i = 0; i < r; i++){
				puts(buf[i]);
			}
		}
	}
	return 0;
}