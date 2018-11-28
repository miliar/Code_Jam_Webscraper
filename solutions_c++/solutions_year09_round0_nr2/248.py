
#include <iostream>
#include <map>

using namespace std;

int grid[100][100];
int par[10000];

bool legal(int a, int b, int h, int w){
	
	return a<h && a>=0 && b<w && b>=0;
}

int findpar(int x){
	
	if(x == par[x]){
		return x;
	}

	return par[x] = findpar(par[x]);
}

int main(){
	
	int T, H, W;

	cin >> T;
	
	int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
	
	map<int, char> trs;

	char ssymbol;

	for(int ncase = 1; ncase <= T; ++ncase){
		
		trs.clear();
		ssymbol = 'a';

		cin >> H >> W;

		for(int i=0; i<H; ++i){
			for(int j=0; j<W; ++j){
				cin >> grid[i][j];
			}
		}

		for(int i=0; i<H*W; ++i){
			par[i] = i;
		}

		for(int i=0; i<H; ++i){
			for(int j=0; j<W; ++j){
				int min = grid[i][j];
				int dir = -1;
				for(int k=0; k<4; ++k){
					int x = i+d[k][0];
					int y = j+d[k][1];
					if(legal(x, y, H, W)){
						if(min > grid[x][y]){
							min = grid[x][y];
							dir = k;
						}
					}
				}
				if(dir != -1){
					int u = findpar(i*W+j);
					int v = findpar((i+d[dir][0])*W+(j+d[dir][1]));
					if(u < v){
						par[v] = u;
					}else{
						par[u] = v;
					}
				}
			}
		}

		for(int i=0; i<H; ++i){
			for(int j=0; j<W; ++j){
				findpar(i*W+j);
			}
		}

		cout << "Case #" << ncase << ":" << endl;

		for(int i=0; i<H; ++i){
			for(int j=0; j<W; ++j){
				if(trs.find(par[i*W+j]) == trs.end()){
					trs[par[i*W+j]] = ssymbol;
					ssymbol++;
				}
				cout << trs.find(par[i*W+j])->second;
				if(j == W-1){
					cout << endl;
				}else{
					cout << " ";
				}
			}
		}
	}
	return 0;
}
