#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

#define INF 1000000

int altitude[102][102];
int flow[102][102]; // x<<10+y
char basin[102][102], label;
int T, H, W, nCase;
int dx[4]={-1,0,0,1}, dy[4]={0,-1,1,0};

inline int Hash(int x, int y){ return ((x<<10)|y); }

int Sink(int x, int y){
	if(flow[x][y]==Hash(x, y)) return flow[x][y];
	else return (flow[x][y] = Sink( (flow[x][y]>>10), (flow[x][y]&1023) ));
}

char Label(int x, int y){
	int sink = Sink(x, y);
	int Sx=(sink>>10), Sy=(sink&1023);
	if(basin[Sx][Sy]==0){
		return (basin[Sx][Sy]=label++);
	}
	else return basin[Sx][Sy];
}

int main(){
	scanf("%d", &T);
	for(nCase=1;T-->0;nCase++){
		scanf("%d%d", &H, &W);
		for(int i=0;i<=H+1;i++) altitude[i][0] = altitude[i][W+1] = INF;
		for(int j=0;j<=W+1;j++) altitude[0][j] = altitude[H+1][j] = INF;
		for(int i=1;i<=H;i++)
			for(int j=1;j<=W;j++)
				scanf("%d", &altitude[i][j]);
		for(int i=1;i<=H;i++){
			for(int j=1;j<=W;j++){
				int minA = min( min(altitude[i+1][j], altitude[i-1][j]), min(altitude[i][j+1], altitude[i][j-1]) );
				if(minA<altitude[i][j]){
					for(int k=0;k<4;k++)
						if(minA==altitude[i+dx[k]][j+dy[k]]){
							flow[i][j] = Hash(i+dx[k], j+dy[k]);
							break;
						}
				}
				else flow[i][j] = Hash(i, j);
//				printf("(%d, %d) ", flow[i][j]>>10, flow[i][j]&1023);
			}
//			printf("\n");
		}
		memset(basin, 0, sizeof basin);
		label = 'a';
		printf("Case #%d:\n", nCase);
		for(int i=1;i<=H;i++){
			for(int j=1;j<W;j++)
				printf("%c ", Label(i,j));
			printf("%c\n", Label(i,W));
		}
				
				
	}
    return 0;
}

