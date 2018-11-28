#include <iostream>
#include <string>
using namespace std;


const int MAX = 105;
const int INF = INT_MAX;

int map[MAX][MAX];
int s[MAX][MAX];
int a, b;
int top;
int num;
int move[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};

int jud(int x, int y)
{
	return (x >= 0 && x < a && y >= 0 && y < b);
}

void dfs(int x, int y)
{
	int i, j, di = -1, ds = INF;
	int small = map[x][y];
	for(i = 0; i < 4; i++){
		int dx = x + move[i][0];
		int dy = y + move[i][1];
		if(jud(dx, dy) && map[dx][dy] < small){
			small = map[dx][dy];
			di = i;
		}
	}
	if(di == -1){
		num = top++;
		s[x][y] = num;
	}
	else{
		int dx = x + move[di][0];
		int dy = y + move[di][1];
		if(s[dx][dy]){
			num = s[dx][dy];
			s[x][y] = num;
		}
		else{
			dfs(dx, dy);
			s[x][y] = num;
		}
	}
}


void go()
{
	int i, j;
	top = 1;
	memset(s, 0, sizeof(s));
	for(i = 0; i < a; i++){
		for(j = 0; j < b; j++){
			if(s[i][j] == 0){
				dfs(i, j);
			}
		}
	}
	for(i = 0; i < a; i++){
		for(j = 0; j < b; j++){
			if(j == 0)  printf("%c", s[i][j] - 1 + 'a');
			else  printf(" %c", s[i][j] - 1 + 'a');
		}
		printf("\n");
	}
}

int main()
{
	int T, cnt = 0;
	freopen("f://B-large.in", "r", stdin);
	freopen("f://B-large.out", "w", stdout);
	scanf("%d", &T);
	while(T--){
		int i, j;
		cnt++;
		scanf("%d%d", &a, &b);
		for(i = 0; i < a; i++){
			for(j = 0; j < b; j++)
				scanf("%d", &map[i][j]);
		}
		printf("Case #%d:\n", cnt);
		go();
	}
}