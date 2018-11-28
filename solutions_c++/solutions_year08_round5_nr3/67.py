#include<iostream>
using namespace std;

int getBit(int num, int index){return (num >> index) & 1 ? 1 : 0;}

char grid[10][10];
int R, C;

int table[10][1<<10];
int get(int r, int m){
	
	if(r >= R)return 0;
	if(table[r][m] != -1)return table[r][m];
	
	int best = 0;
	for(int i = 0 ; i < (1<<C) ; i++){
		int j = 0, cnt = 0;
		for(j = 0 ; j < C ; j++){
			if(getBit(i,j)){
				if(grid[r][j] == 'x')break;
				if(j+1 < C && getBit(i,j+1))break;
				
				if(j-1 >= 0 && getBit(m,j-1))break;
				if(j+1 < C && getBit(m,j+1))break;			
			}
			cnt += getBit(i,j);
		}
		if(j != C)continue;
		
		int current = cnt + get(r+1, i);
		best = max(current, best);
	}
	return table[r][m] = best;
}

int main(){

	//freopen("1.in", "rt", stdin);
	freopen("C-small.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);
	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cin >> R >> C;
		for(int r = 0 ; r < R ; r++)
			for(int c = 0 ; c < C ; c++)
				cin >> grid[r][c];
		
		memset(table, -1, sizeof table);
		cout << "Case #" << t+1 << ": " << get(0, 0) << endl;
	}

	return 0;	
}
