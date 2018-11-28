#include <iostream>

using namespace std; 

const int pos[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};

int T, H, W;
int a[105][105];
int flow[105][105];
char label[105][105];

bool valid(int x, int y){
				return (x>=0 && x<H && y>=0 && y<W);
}

void bfs(int x, int y, char c){
				pair<int,int> myqueue[10050];
				int head, tail;

				head = 0; 
				myqueue[0] = make_pair(x, y);
				label[x][y] = c;	
				tail = 1;	

				while (head<tail){
								int qx = myqueue[head].first;
								int qy = myqueue[head].second;

								for (int i=0; i<4; ++i){
												int nx = qx+pos[i][0];
												int ny = qy+pos[i][1];
												if (valid(nx, ny) && label[nx][ny]==' '){
																if (i==flow[qx][qy] || flow[nx][ny] == 3-i){
																				myqueue[tail] = make_pair(nx, ny);
																				label[nx][ny] = c;
																				tail++;
																}
												}
								}
								head++;
				}
}

int main(){

				cin >> T;
				for (int cnt=0; cnt<T; ++cnt){
								cin >> H >> W;
								for (int i=0; i<H; ++i){
												for (int j=0; j<W; ++j){
																cin >> a[i][j];
																label[i][j] = ' ';
												}
								} 

								// precompute flow position
								for (int i=0; i<H; ++i){
												for (int j=0; j<W; ++j){
																flow[i][j] = -1; // value if sink
																for (int k=0; k<4; ++k){
																				int nx = i+pos[k][0];
																				int ny = j+pos[k][1];
																				if (valid(nx, ny)){
																								if (a[nx][ny]<a[i][j]){
																												if (flow[i][j]!= -1){
																																if (a[nx][ny]<a[i+pos[flow[i][j]][0]][j+pos[flow[i][j]][1]])
																																				flow[i][j] = k;
																												} else {
																																flow[i][j] = k;
																												}
																								}
																				}
																}
												}
								}

								// start working
								char label_c = 'a';
								for (int i=0; i<H; ++i){
												for (int j=0; j<W; ++j){
																if (label[i][j] == ' '){
																				bfs(i, j, label_c);
																				label_c++;
																}
												}
								}

								// output answer
								cout << "Case #" << cnt+1 << ": " << endl;

								/* debug
									 for (int i=0; i<H; ++i){
									 for (int j=0; j<W-1; ++j){
									 cout << flow[i][j] << ' ';
									 }
									 cout << flow[i][W-1] << endl;
									 }
									 */
								for (int i=0; i<H; ++i){
												for (int j=0; j<W-1; ++j){
																cout << label[i][j] << ' ';
												}
												cout << label[i][W-1] << endl;
								}
				}
}
