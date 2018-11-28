#include <cstdio>
#include <list>
using namespace std;
int map[105][105];
int T, W, H;
list<int> Graph[10005];
int color[10005];
int currentEtiq = 0;
int etiq[105][105];
void init(){
	for (int i = 0; i < 105; i++)
		for(int j = 0; j < 105; j++)
			map[i][j] = etiq[i][j] = 999999;
	for (int i = 0; i < 10005; i++){
		color[i] = 0;
		Graph[i].clear();
	}
	currentEtiq = 0;
}

void loadData(){
	scanf("%d %d", &H, &W);
	for(int i = 1; i <= H; i++)
		for (int j = 1; j <= W; j++)
			scanf ("%d", &map[i][j]);
}

void printData(){
	for(int i = 1; i <= H; i++){
		for (int j = 1; j <= W; j++)
			printf ("%c ", etiq[i][j]-1+'a');
		printf("\n");
	}
}

void makeGraph(){
	for (int i = 1; i <= H; i++)
		for (int j = 1; j <= W; j++){
			int minimal = map[i][j];
			int where = 0;
			if (map[i-1][j] < minimal){
				where = (i-2)*W+j;
				minimal = map[i-1][j];
			}
			if (map[i][j-1] < minimal){
				where = (i-1)*W+j-1;
				minimal=map[i][j-1];
			}
			if (map[i][j+1] < minimal){
				where = (i-1)*W+j+1;
				minimal=map[i][j+1];
			}
			if (map[i+1][j] < minimal){
				where = i*W+j;
				minimal=map[i+1][j];
			}
			if (minimal < map[i][j]){
				Graph[(i-1)*W+j].push_back(where);
				Graph[where].push_back((i-1)*W+j);
			}
		}
}
void printGraph(){
	for (int i = 1; i <= H; i++){
		for (int j = 1; j <= W; j++){
			printf ("%d %d : ", i, j);
			for(list<int>::iterator a = Graph[(i-1)*W+j].begin(); a != Graph[(i-1)*W+j].end(); a++)
				printf ("%d %d\t", (*a-1)/W+1, (*a)%W);
		}
		printf ("\n");
	}
}
void DFS(int v){
	if (color[v] == 0){
		color[v] = 1;
		int h = (v-1)/W+1;
		int w = v%W;
		if (w == 0)
			w = W;
		etiq[h][w] = currentEtiq;
		for (list<int>::iterator a = Graph[v].begin(); a != Graph[v].end(); a++)
			DFS(*a);
	}
}

int main(){
	scanf("%d", &T);
	for (int q = 0; q < T; q++){
		init();
		loadData();
		makeGraph();
		//printGraph();
		for (int x = 1; x <= H*W; x++){
			if (color[x] == 0){
				currentEtiq++;
				DFS(x);
			}
		}
		printf ("Case #%d:\n", q+1);
		printData();
	}
	
	return 0;
}
