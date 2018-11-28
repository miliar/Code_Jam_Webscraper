#pragma warning(disable:4996)

#include <iostream>

#define N (50 + 10)

int n, m, c;

bool pos;

char map[N][N];

void input(){
	int i;
	scanf("%d %d", &n, &m);
	for(i = 0; i < n; i++){
		scanf("%s", &map[i]);
	}
	fcloseall();
}

void process(){
	int i, j;
	for(i = 0; i < n - 1; i++){
		for(j = 0; j < m - 1; j++){
			if(map[i][j] == '#'){
				if(map[i][j + 1] == '#' && map[i + 1][j] == '#' && map[i + 1][j + 1] == '#'){
					map[i][j] = map[i + 1][j + 1] = '/';
					map[i][j + 1] = map[i + 1][j] = '\\';
				}
				else{
					pos = false;
					return;
				}
			}
		}
	}
	for(i = 0; i < n; i++){
		if(map[i][m - 1] == '#'){
			pos = false;
			return;
		}
	}
	for(j = 0; j < m; j++){
		if(map[n - 1][j] == '#'){
			pos = false;
			return;
		}
	}
}

void output(){
	int i;
	printf("Case #%d:\n", c);
	if(pos){
		for(i = 0; i < n; i++){
			printf("%s\n", map[i]);
		}
	}
	else{
		printf("Impossible\n");
	}
}

int main(){
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(c = 1; c <= t; c++){
		pos = true;
		memset(map, 0, sizeof(map));

		input();
		process();
		output();
	}
	return 0;
}