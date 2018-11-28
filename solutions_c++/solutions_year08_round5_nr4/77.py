#include<iostream>
using namespace std;

int R, C, K;
bool kill[200][200];
int table[200][200];
int dir[2][2] = {{1,2}, {2,1}};

bool valid(int r, int c){
	return r >= 0 && r < R && c >= 0 && c < C;
}

int get(int r, int c){
	
	if(r == R-1 && c == C-1)return 1;
	if(table[r][c] != -1)return table[r][c];

	int res = 0;
	for(int i = 0 ; i < 2 ; i++){
		int nr = r+dir[i][0];
		int nc = c+dir[i][1];
		if(!valid(nr, nc) || kill[nr][nc])continue;
		res = (res+get(nr,nc))%10007;
	}	
	return table[r][c] = res;
}

int main(){

	//freopen("1.in", "rt", stdin);
	freopen("D-small.in", "rt", stdin);
	freopen("D-small.out", "wt", stdout);
	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cin >> R >> C >> K;
		memset(kill, 0, sizeof kill);
		memset(table, -1, sizeof table);
		
		for(int i = 0 ; i < K ; i++){
			int r, c; cin >> r >> c;
			kill[r-1][c-1] = true;
		}
		
		cout << "Case #" << t+ 1<< ": " << get(0, 0) << endl;
	}

	return 0;	
}
