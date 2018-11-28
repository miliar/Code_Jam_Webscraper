#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

const int maxn = 120;
const int big = 1000000000;
const int nil = -1;

int forward[][2] = { { -1, 0}, { 0, -1}, { 0, 1}, { 1, 0}};

struct Node{
	int bx, by;
	char label;
	bool calced;
};

int input[maxn][maxn];
Node data[maxn][maxn];
bool visited[maxn][maxn];
int H, W;

void dfs(int r, int c){
	int x, y, i, max = input[r][c], sel = nil;
	if(data[r][c].calced) return;
	data[r][c].calced = true;
	for(i = 0; i < 4; i++){
		x = r + forward[i][0];
		y = c + forward[i][1];
		if(x >= 0 && x < H && y >= 0 && y < W && input[x][y] < max){
			max = input[x][y];
			sel = i;
		}
	}
	if(sel == nil){
		data[r][c].bx = r; data[r][c].by = c;
		return;
	}
	x = r + forward[sel][0]; y = c + forward[sel][1];
	dfs(x, y);
	data[r][c].bx = data[x][y].bx; data[r][c].by = data[x][y].by;
}	

void get_basin(){
	int i, j, k, p, q;
	for(i = 0; i < H; i++){
		for(j = 0; j < W; j++) data[i][j].calced = false;
	}
	for(i = 0; i < H; i++){
		for(j = 0; j < W; j++){
			if(!data[i][j].calced) dfs(i, j);
		}
	}
}

void give_label(int r, int c, char label){
	int i, x, y, p, q;
	queue<int> fifo;
	data[r][c].label = label;
	visited[r][c] = true;
	fifo.push(r); fifo.push(c);
	while(!fifo.empty()){
		x = fifo.front(); fifo.pop();
		y = fifo.front(); fifo.pop();
		data[x][y].label = label;
		for(i = 0; i < 4; i++){
			p = x + forward[i][0];
			q = y + forward[i][1];
			if(p >= 0 && p < H && q >= 0 && q < W && !visited[p][q]){
				if(data[p][q].bx == data[x][y].bx && data[p][q].by == data[x][y].by){
					visited[p][q] = true;
					fifo.push(p); fifo.push(q);
				}
			}
		}
	}
}
					
		

void get_label(){
	int i, j, k, x, y;
	char label = 'a';
	queue<int> fifo;
	for(i = 0; i < H; i++){
		for(j = 0; j < W; j++) visited[i][j] = false;
	}
	for(i = 0; i < H; i++){
		for(j = 0; j < W; j++){
			if(!visited[i][j]){
				give_label(i, j, label);
				label++;
			}
		}
	}
}

void read_in(){
	int i, j;
	scanf("%d%d", &H, &W);
	for(i = 0; i < H; i++){
		for(j = 0; j < W; j++){
			scanf("%d", &(input[i][j]));
		}
	}
}

void output(int cases){
	int i, j;
	printf("Case #%d:\n", cases);
	for(i = 0; i < H; i++){
		for(j = 0; j < W; j++){
			printf("%c ", data[i][j].label);
		}
		printf("\n");
	}
}

int main(){
	freopen("B.out", "w", stdout);
	int t, i;
	scanf("%d", &t);
	for(i = 1; i <= t; i++){
		read_in();
		get_basin();
		get_label();
		output(i);
	}
}
