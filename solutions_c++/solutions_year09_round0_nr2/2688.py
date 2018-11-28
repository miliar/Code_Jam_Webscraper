#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <map>

using namespace std;

#define MAX 110	
#define MAXX 11000
// North, West, East, South

int adj[MAX][MAX], lbl[MAX][MAX], letter;
int dx[] = { 0, -1, 1, 0};
int dy[] = {-1,  0, 0, 1};

int dfs(int i, int j) {

	if(lbl[i][j] == 0) {

		int minCST = adj[i][j], ii = 0, jj = 0;
		
		for(int k = 0; k < 4; k++) {
			if(adj[i+dy[k]][j+dx[k]] < MAXX && minCST > adj[i+dy[k]][j+dx[k]]) {
				minCST = adj[i+dy[k]][j+dx[k]];
				ii = i+dy[k];
				jj = j+dx[k];
			}
		}
		if(minCST == adj[i][j]) lbl[i][j] = letter++;
		else lbl[i][j] = dfs(ii, jj);
	}
	
return lbl[i][j];
}

int main() {

	int count = 1, t, n, m;
	scanf("%d", &t);
	for(;t;t--) {
		scanf("%d %d", &n, &m);
		for(int i = 0; i < n + 2; i++) 
			for(int j = 0; j < m + 2; j++) {
				adj[i][j] = MAXX;
				lbl[i][j] = 0;
			}
			
		letter = 'a';
		for(int i = 1; i < n + 1; i++) 
			for(int j = 1; j < m + 1; j++) 
				scanf("%d", &adj[i][j]);
				
		for(int i = 1; i < n + 1; i++) 
			for(int j = 1; j < m + 1; j++)
				if(lbl[i][j] == 0) lbl[i][j] = dfs(i, j);
		
		printf("Case #%d:\n", count++);
		for(int i = 1; i < n + 1; i++) {
			printf("%c", lbl[i][1]);
			for(int j = 2; j < m + 1; j++)
				printf(" %c", lbl[i][j]);
			puts("");	
		}
	}

return 0;
}
