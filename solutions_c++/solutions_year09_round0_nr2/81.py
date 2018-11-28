#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef pair<int, int> pii;

int alt[123][123];
int status[123][123];
bool vis[123][123];
char res[123][123];
char let_sink[40];

vector<pii> from[123][123];

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

int qt_sinks;

int N, M;

void make_graph(){

	qt_sinks = 0;

	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++){
			from[i][j] = vector<pii>();
		}


	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			int ch = -1;

			int at_alt = 12312313;
			for(int k = 0; k < 4; k++){
				int nx = j + dx[k];
				int ny = i + dy[k];

				if(nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
				if(alt[ny][nx] >= at_alt) continue;

				ch = k;
				at_alt = alt[ny][nx];
			}
			if(at_alt < alt[i][j]){
				//printf("colocando em (%d, %d) [%d] \n",i+dy[ch], j+dx[ch], ch);
				from[i+dy[ch]][j+dx[ch]].push_back(pii(i,j));
			} else {
				status[i][j] = -(++qt_sinks);
			}
		}
	}
}

void dfs(int x, int y, int sink){
	if(vis[y][x]) return;
	vis[y][x] = true;
	status[y][x] = sink;

	for(int i = 0; i < from[y][x].size(); i++){
		pii p = from[y][x][i];
		int xx, yy;
		xx = p.second;
		yy = p.first;

		dfs(xx,yy,sink);
	}
}

void make_dfs(){
	memset(vis, 0, sizeof(vis));
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if(status[i][j] < 0){
				status[i][j] *= -1;
				dfs(j,i,status[i][j]);
			}
		}
	}
}

void resolve(){
	char let = 'a';
	memset(let_sink, 0, sizeof(let_sink));
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			int k = status[i][j];
			if(let_sink[k] == 0) let_sink[k] = let++;
			res[i][j] = let_sink[k];
		}
	}
}

int main(void){
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> N >> M;
		for(int j = 0; j < N; j++){
			for(int k = 0; k < M; k++){
				cin >> alt[j][k];
			}
		}

		memset(status, 0, sizeof(status));

		make_graph();
		make_dfs();
		resolve();

		printf("Case #%d:\n", i+1);
		for(int j = 0; j < N; j++){
			printf("%c", res[j][0]);
			for(int k = 1; k < M; k++){
				printf(" %c", res[j][k]);

			}

			printf("\n");
		}
	}
}




