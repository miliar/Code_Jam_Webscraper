#include <iostream>
	using namespace std;

int main(){
	int N, K, T, Case, i, j, ind[100];
	char map[100][100];
	int Map[100][100];
	int R, B;
	scanf("%d", &T);
	for(Case = 1; Case <= T; Case++){
		scanf("%d%d", &N, &K);
		for(i = 0; i < N; ++i){
			scanf("%s", map[i]);
		}
		for(i = 0; i < N; ++i)
			ind[i] = N-1;
		for(i = 0; i < N; ++i)
			for(j = 0; j < N; ++j)
				Map[i][j] = 0;
		for(i = 0; i < N; ++i){
			for(j = N-1; j >= 0; --j){
				if(map[i][j] == 'R')
					Map[i][ind[i]--] = 1;
				else if(map[i][j] == 'B')
					Map[i][ind[i]--] = 2;
			}
		}
		R = 0; B = 0;
		/*for(i = 0; i < N; ++i){
			for(j = 0; j < N; ++j)
				printf("%d", Map[i][j]);
			printf("\n");
		}*/
		int longest = 0, now = 0;
		for(i = 0; i < N; ++i){
			longest = 0, now = 0;
			for(j = 0; j < N; ++j){
				if(Map[i][j] != 0){
					if(now == 0){
						now = Map[i][j];
						longest++;
					}
					else if(Map[i][j] == now){
						longest++;
					}
					else{
						now = Map[i][j];
						longest = 1;
					}
				}
				else{
					now = 0;
					longest = 0;
				}
				if(longest >= K){
					if(now == 1){
						//printf("i = %d, j = %d\n", i, j);
						R = 1;
					}
					else
						B = 1;	
				}
			}
		}
		//printf("1 %d %d\n", R, B);
		longest = 0; now = 0;
		for(j = 0; j < N; ++j){
		longest = 0, now = 0;
			for(i = 0; i < N; ++i){
				if(Map[i][j] != 0){
					if(now == 0){
						now = Map[i][j];
						longest++;
					}
					else if(Map[i][j] == now){
						longest++;
					}
					else{
						now = Map[i][j];
						longest = 1;
					}
				}
				else{
					now = 0;
					longest = 0;
				}
				if(longest >= K){
					if(now == 1)
						R = 1;
					else
						B = 1;	
				}
			}
		}
		//printf("2 %d %d\n", R, B);
		longest = 0; now = 0; // 右上半往右下
		for(i = 0; i < N; ++i){
		longest = 0, now = 0;
			for(j = 0; j+i < N; ++j){
				if(Map[j][j+i] != 0){
					if(now == 0){
						now = Map[j][j+i];
						longest++;
					}
					else if(Map[j][j+i] == now){
						longest++;
					}
					else{
						now = Map[j][j+i];
						longest = 1;
					}
				}
				else{
					now = 0;
					longest = 0;
				}
				if(longest >= K){
					if(now == 1)
						R = 1;
					else
						B = 1;	
				}
			}
		}
		//printf("3 %d %d\n", R, B);
		longest = 0; now = 0; // 左下半往右下
		for(i = 0; i < N; ++i){
		longest = 0, now = 0;
			for(j = 0; j+i < N; ++j){
				if(Map[j+i][j] != 0){
					if(now == 0){
						now = Map[j+i][j];
						longest++;
					}
					else if(Map[j+i][j] == now){
						longest++;
					}
					else{
						now = Map[j+i][j];
						longest = 1;
					}
				}
				else{
					now = 0;
					longest = 0;
				}
				if(longest >= K){
					if(now == 1)
						R = 1;
					else
						B = 1;	
				}
			}
		}
		//printf("4 %d %d\n", R, B);
		longest = 0; now = 0; // 右下半往左下
		for(i = 0; i < N; ++i){
		longest = 0, now = 0;
			for(j = 0; j+i < N; ++j){
				if(Map[j+i][N-j-1] != 0){
					if(now == 0){
						now = Map[j+i][N-j-1];
						longest++;
					}
					else if(Map[j+i][N-j-1] == now){
						longest++;
					}
					else{
						now = Map[j+i][N-j-1];
						longest = 1;
					}
				}
				else{
					now = 0;
					longest = 0;
				}
				if(longest >= K){
					if(now == 1)
						R = 1;
					else
						B = 1;	
				}
			}
		}
		//printf("5 %d %d\n", R, B);
		longest = 0; now = 0; // 左上半往左下
		for(i = 0; i < N; ++i){
		longest = 0, now = 0;
			for(j = 0; j+i < N; ++j){
				if(Map[j][N-j-i-1] != 0){
					if(now == 0){
						now = Map[j][N-j-i-1];
						longest++;
					}
					else if(Map[j][N-j-i-1] == now){
						longest++;
					}
					else{
						now = Map[j][N-j-i-1];
						longest = 1;
					}
				}
				else{
					now = 0;
					longest = 0;
				}
				if(longest >= K){
					if(now == 1)
						R = 1;
					else
						B = 1;	
				}
			}
		}
		printf("Case #%d: ", Case);
		if(R == 1 && B == 1)
			printf("Both\n");
		else{
			if(R == 1 && B == 0)
				printf("Red\n");
			else if(B == 1 && R == 0)
				printf("Blue\n");
			else
				printf("Neither\n");
		}
	}
	return 0;
}