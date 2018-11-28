#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>

# define INF 0x3f3f3f3f

# define MAXN 64

int tc = 1;

char grid[MAXN][MAXN];
char board[MAXN][MAXN];

int T, N, K;

using namespace std;

bool red , blue;

int main (void){
	scanf("%d", &T);
	while(T--){
		red = blue = false;
		printf("Case #%d: ", tc++);
		scanf("%d%d", &N,&K);
		for(int i = 0;i<N;i++) scanf(" %s", board[i]);
		for(int i = 0;i<N;i++){
			for(int j = 0;j<N;j++) grid[i][j] = board[N-1-j][i];
		}
		
		
		/*for(int i = 0;i<N;i++){
			for(int j = 0;j<N;j++){
				printf("%c", grid[i][j]);
			}
			printf("\n");
		}*/
		
		for(int i = N-1;i>=0;i--){
			for(int j = 0;j<N;j++){
				if(grid[i][j] != '.'){
					// printf("%c\n", grid[i][j]);
					if(i<=N-1){
						int k = i+1;
						while(1){
							if(k == N ) break;
							if(grid[k][j] != '.') break;
							k++;
						}
						grid[k-1][j] = grid[i][j];
						if(k-1 != i) grid[i][j] = '.';
					}
				}
			}
		}
		/*printf("\n");
		for(int i = 0;i<N;i++){
			for(int j = 0;j<N;j++){
				printf("%c", grid[i][j]);
			}
			printf("\n");
		}*/
		for(int i = 0;i<N;i++){
			for(int j = 0;j<N;j++){
				if(grid[i][j] == 'R'){
					int cnt = 1;
					for(int k = j+1; k<N;k++){
						if(grid[i][k] == 'R') cnt++;
						else break;
					}
					if(cnt >= K) red = true;
					cnt = 1;
					for(int k = i+1;k<N;k++){
						if(grid[k][j] == 'R') cnt++;
						else break;
					}
					if(cnt >= K) red = true;
					cnt = 1;
					for(int k = 1;k<N;k++){
						if((i+k >= N) || (j + k >= N)) break;
						if(grid[i+k][j+k] == 'R') cnt++;
						else break;
					}
					if(cnt >= K) red = true;
					cnt = 1;
					for(int k = 1;k<N;k++){
						if((i+k >= N) || (j - k < 0)) break;
						if(grid[i+k][j-k] == 'R') cnt++;
						else break;
					}
					if(cnt >= K) red = true;
				}
				if(grid[i][j] == 'B'){
					int cnt = 1;
					for(int k = j+1; k<N;k++){
						if(grid[i][k] == 'B') cnt++;
						else break;
					}
					if(cnt >= K) blue = true;
					cnt = 1;
					for(int k = i+1;k<N;k++){
						if(grid[k][j] == 'B') cnt++;
						else break;
					}
					if(cnt >= K) blue = true;
					cnt = 1;
					for(int k = 1;k<N;k++){
						if((i+k >= N) || (j + k >= N)) break;
						if(grid[i+k][j+k] == 'B') cnt++;
						else break;
					}
					if(cnt >= K) blue = true;
					cnt = 1;
					for(int k = 1;k<N;k++){
						if((i+k >= N) || (j - k < 0)) break;
						if(grid[i+k][j-k] == 'B') cnt++;
						else break;
					}
					if(cnt >= K) blue = true;
				}
			}
		}
		
		if(blue && red) printf("Both\n");
		else if(!blue && !red) printf("Neither\n");
		else if(blue && !red) printf("Blue\n");
		else if(!blue && red) printf("Red\n");
	}
	return 0;
}