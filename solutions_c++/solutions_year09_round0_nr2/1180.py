#include <cstdio>
using namespace std;
#include <algorithm>
#include <iostream>
#include <string>

#define MAXN 110
int a[MAXN][MAXN];
char res[MAXN][MAXN];
bool used[MAXN][MAXN];

int di[4] = {-1, 0, 0, 1};
int dj[4] = {0, -1, 1, 0};
int h, w;
char no;

void DFS(int i, int j){
	if (used[i][j]) return;
	used[i][j] = true;
	res[i][j] = no;
	int sink = -1;
	for (int k = 0; k < 4; k++){
		int ni = i + di[k];
		int nj = j + dj[k];
		if ((ni >= 0) && (nj >= 0) && (ni < h) && (nj < w))
			if (a[ni][nj] < a[i][j]){
				if (sink == -1) sink = k;
				if (a[ni][nj] < a[i + di[sink]][j + dj[sink]])
					sink = k;
			}
	}
	if (sink != -1){
		DFS(i + di[sink], j + dj[sink]);
		res[i][j] = res[i + di[sink]][j + dj[sink]];
	}
	else
		res[i][j] = no++;
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++){
		printf("Case #%d:\n", tt);
		cerr<<tt<<endl;
		scanf("%d%d", &h, &w);
		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++){
				scanf("%d", &a[i][j]);
				used[i][j] = false;
			}
		no = 'a';
		for (int i = 0; i < h; i++){
			for (int j = 0; j < w; j++){
				DFS(i, j);
				printf("%c ", res[i][j]);
			}
			printf("\n");
		}
		
	}
	return 0;
}
