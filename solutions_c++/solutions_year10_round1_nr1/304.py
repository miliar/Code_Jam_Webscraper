#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
#define MAXN 100
int n, k;
int m[MAXN][MAXN];
int last[MAXN];

bool w[3];

int dir[][2] = {{-1, 0}, {1, 0}, {0, 1}, {-1, 1}, {1, 1}, {1, -1}, {-1, -1}, {0, -1}};
//int dir[][2] = {{0, -1}, {0, 1}, {1, 0}, {1, -1}, {1, 1}};
bool islegal(int x, int y){
	if(x < 1 || y < 1 || x > n || y > n)return false;
	return true;
}
int main(){
	int ca = 1, cases;
	char tmp[100][100];
	freopen("test", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d", &cases);
	while(cases--){
		memset(m, 0, sizeof(m));
		memset(last, 0, sizeof(last));
		w[1] = false;
		w[2] = false;

		scanf("%d%d", &n, &k);
		for(int i = 1;i <= n; i++)
			scanf("%s", tmp[i]+1);
		for(int i = 1;i <= n; i++){
			for(int j = 1;j <= n; j++){
				if(tmp[j][i] == 'R'){
					m[n-i+1][j] = 1;
				} else if(tmp[j][i] == 'B'){
					m[n-i+1][j] = 2;
				}
			}
		}
		/*
		for(int i = 1;i <= n; i++){
			for(int j = 1;j <= n; j++){
				printf("%c", tmp[i][j]);
			}
			printf("\n");
		}*/
		for(int i = 1;i <= n; i++){
			last[i] = 1;
			while(m[last[i]][i]){
				last[i]++;
			}
		}
		for(int i = 1;i <= n; i++){
			for(int j = 1;j <= n; j++){
				if(m[i][j] != 0 && last[j] < i){
					m[last[j]][j] = m[i][j];
					m[i][j] = 0;
					while(m[last[j]][j]){
						last[j]++;
					}
				}
			}
		}
		//printf("\n");
		/*for(int i = 1;i <= n; i++){
			for(int j = 1;j <= n; j++){
				printf("%d", m[i][j]);
			}
			printf("\n");
		}
*/


		for(int i = 1;i <= n; i++){
			for(int j = 1;j <= n; j++){
				if(m[i][j] == 0)continue;
				//if(w[m[i][j]])continue;
				//printf("%d\n", m[i][j]);
				for(int p = 0;p < 8; p++){	//dir
					int nowx = i;
					int nowy = j;

					for(int t = 1;t <= k; t++){
						if(t == k){
							w[m[i][j]] = true;
							break;
						}
						nowx = nowx + dir[p][0];
						nowy = nowy + dir[p][1];
						if(!islegal(nowx, nowy))break;
						if(m[i][j] != m[nowx][nowy])break;
					}
				}
			}
		}


		printf("Case #%d: ", ca++);

		if(w[1] && w[2])
			printf("Both\n");
		else if(w[1])
			printf("Red\n");
		else if(w[2])
			printf("Blue\n");
		else
			printf("Neither\n");
	}
	return 0;
}
