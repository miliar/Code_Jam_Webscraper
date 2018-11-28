#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

int t;
int agua, n, m;
int chao[101][101], teto[101][101];
int tempo[101][101];
//int nt[101][101];
int rangei[4] = {1,0,-1,0};
int rangej[4] = {0,1,0,-1};

void bfs(int ati, int atj){
	for(int i = 0; i < 4; ++i){
		int ii = ati+rangei[i];
		int jj = atj+rangej[i];
		if(ii >= 0 && ii < n && jj >= 0 && jj < m && tempo[ii][jj] < 0){
			if(min(teto[ati][atj],teto[ii][jj]) - max(max(chao[ati][atj],chao[ii][jj]),agua) >= 50){
				tempo[ii][jj] = 0;
				bfs(ii, jj);
			}
		}
	}
}

void bfs2(int ati, int atj){
	for(int i = 0; i < 4; ++i){
		int ii = ati+rangei[i];
		int jj = atj+rangej[i];
		if(ii >= 0 && ii < n && jj >= 0 && jj < m){
			if(min(teto[ati][atj],teto[ii][jj]) - max(max(chao[ati][atj],chao[ii][jj]),agua) >= 50){
				if(agua-chao[ati][atj] >= 20){
					if(tempo[ii][jj] < 0) tempo[ii][jj] = tempo[ati][atj]+10;
					else tempo[ii][jj] = min(tempo[ii][jj],tempo[ati][atj]+10);
				}else{
					if(tempo[ii][jj] < 0) tempo[ii][jj] = tempo[ati][atj]+100;
					else tempo[ii][jj] = min(tempo[ii][jj],tempo[ati][atj]+100);
				}
			}
		}
	}
}
int mark[101][101];
struct estado{
	int ati, atj, t;
	estado(){}
	estado(int a, int b, int c){
		ati = a;
		atj = b;
		t = c;
	}
	const bool operator< (const estado &that) const{
		return t> that.t;
	}
}atual;

int main(){
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int caso = 0;
	scanf("%d", &t);
	
	while(t--){
		memset(tempo, -1, sizeof tempo);
		tempo[0][0] = 0;
		scanf("%d %d %d", &agua, &n, &m);
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < m; ++j) scanf("%d", &teto[i][j]);
		}
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < m; ++j) scanf("%d", &chao[i][j]);
		}
		bfs(0,0);
		int tem = 0;
		if(tempo[n-1][m-1] < 0){
			priority_queue<estado> fila;
			while(agua--){
				tem++;
				for(int i = 0; i < n; ++i){
					for(int j = 0; j < m; ++j){
						if(tempo[i][j] >= 0 && tempo[i][j] <= tem){
							tempo[i][j] = tem;
							bfs2(i,j);
						}
					}
				}
				//memcpy(tempo, nt, sizeof tempo);
				if(tempo[n-1][m-1] == tem){
					goto fuji;
				}
			}
			
			//while(true){
			memset(mark, 63, sizeof mark);
			
				tem++;
				for(int i = 0; i < n; ++i){
					for(int j = 0; j < m; ++j){
						if(tempo[i][j] >= 0){
							fila.push(estado(i,j,max(tem,tempo[i][j])));
							mark[i][j] = max(tem,tempo[i][j]);
						}
					}
				}
				while(true){
					atual = fila.top(); fila.pop();
					if(atual.ati == n-1 && atual.atj == m-1) break;
					if(atual.t > mark[atual.ati][atual.atj]) continue;
					for(int i = 0; i < 4; ++i){
						int ii = atual.ati+rangei[i];
						int jj = atual.atj+rangej[i];
						if(ii >= 0 && ii < n && jj >= 0 && jj < m){
							if(min(teto[atual.ati][atual.atj],teto[ii][jj]) - max(chao[atual.ati][atual.atj],chao[ii][jj]) >= 50){
								int t = atual.t+100;
								if(mark[ii][jj] > t){
									mark[ii][jj] = t;
									fila.push(estado(ii,jj,t));
								}
							}
						}
					}
					
				}
				//memcpy(tempo, nt, sizeof tempo);
				//if(tempo[n-1][m-1] == tem){
					//goto fuji;
				//}
				tem = atual.t;
			//}
			fuji:;
		}
		int resp = tem;
		printf("Case #%d: %d.%d\n", ++caso, resp/10, resp%10);
	}
	return 0;
}
