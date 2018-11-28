// GCJ2009 Qual B
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <utility>

using namespace std;

int T;
int W;
int H;
int field[102][102];
int dst[102][102];
int dir[102][102];
char res[102][102];
const int INF = 100000;
int dc[] = {0, -1, 1, 0};
int dr[] = {-1, 0, 0, 1};

int findDst(int r, int c){
	if(dst[r][c] != -1){
		return dst[r][c];
	}
	return dst[r][c] = findDst(r + dr[dir[r][c]], c + dc[dir[r][c]]);
}

int main(){
	cin >> T;
	for(int i = 0; i < T; ++i){
		cin >> H >> W;
		for(int r = 0; r < H + 2; ++r){
			field[r][0] = field[r][W+1] = INF;
		}
		for(int c = 0; c < W + 2; ++c){
			field[0][c] = field[H+1][c] = INF;
		}
		for(int r = 1; r < H+1; ++r){
			for(int c = 1; c < W+1; ++c){
				cin >> field[r][c];
				dst[r][c] = dir[r][c] = -1;
			}
		}
		for(int r = 1; r < H+1; ++r){
			for(int c = 1; c < W+1; ++c){
				int d = -1;
				int min = INF;
				for(int k = 0; k < 4; ++k){
					int nr = r + dr[k];
					int nc = c + dc[k];
					if(field[r][c] > field[nr][nc] && field[nr][nc] < min){
						min = field[nr][nc];
						d = k;
					}
				}
				if(d == -1){
					dst[r][c] = r * 1000 + c;
				}else{
					dir[r][c] = d;
				}
			}
		}
		for(int r = 1; r < H+1; ++r){
			for(int c = 1; c < W+1; ++c){
				if(dst[r][c] == -1){
					findDst(r, c);
				}
			}
		}
		map<int, char> name;
		char cur = 'a';
		for(int r = 1; r < H+1; ++r){
			for(int c = 1; c < W+1; ++c){
				if(name.find(dst[r][c]) == name.end()){
					name.insert(make_pair(dst[r][c], cur++));
				}
				res[r][c] = name[dst[r][c]];
			}
		}

		cout << "Case #" << (i + 1) << ":\n";
		for(int r = 1; r < H+1; ++r){
			for(int c = 1; c < W+1; ++c){
				cout << res[r][c] << " ";
			}
			cout << "\n";
		}
		
	}
}

