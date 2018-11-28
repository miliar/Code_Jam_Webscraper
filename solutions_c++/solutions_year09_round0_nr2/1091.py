#include <cstdlib>
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cmath>
#define INF 21474836
using namespace std;

int H,W;
char now;
int board[102][102];
bool used[102][102];
vector<string> ret;
int dx[] = {0,-1,1, 0,1,-1, 1,-1};
int dy[] = {-1,0, 0,1,1,-1,-1, 1};

char dfs(int row, int col){
	int bestX=-1,bestY=-1,best=board[row][col];
	used[row][col] = true;
	for(int k = 0; k<4; k++){
		int newRow = row + dy[k], newCol = col + dx[k];
		if(newRow >= H || newRow < 0 || newCol>=W || newCol<0) continue;
		if(board[newRow][newCol] < best){
			bestX = newCol; 
			bestY = newRow;
			best = board[newRow][newCol];
		}
	}
	if(bestX != -1){
		char r;
		if(used[bestY][bestX]) r = ret[bestY][bestX];
		else r = dfs(bestY,bestX);
		ret[row][col] = r;
		return r;
	}
	now++;
	ret[row][col] = now;
	return now;
}

void solve(){
	now = 'a'-1;
	for(int i = 0; i<H; i++)
		for(int j = 0; j<W; j++)
			if(!used[i][j]) 
				ret[i][j] = dfs(i,j);
}

int main()
{
	//FILE *in  = fopen("B-small-attempt1.in","r");
	//FILE *out = fopen("B-small-attempt1.out","w");
	ifstream in("B-small-attempt1.in");
	ofstream out("B-small-attempt1.out");

	int tests;
	in >> tests;
	
	for(int t = 0; t<tests; t++){
		in >> H >> W;
		ret.clear();
		ret.resize(H);
		for(int i = 0; i<H; i++) 
			for(int j = 0; j<W; j++) 
				ret[i].push_back('z'+1);
		cout << " caso " << t+1 << endl;
		
		for(int i = 0; i<H; i++)
			for(int j = 0; j<W; j++)
				in >> board[i][j];
		memset(used,false,sizeof(used));
		solve();
		out << "Case #" << t+1 << ": " << endl;
		for(int i = 0; i<H; i++){
			for(int j = 0; j<W; j++){
				out << ret[i][j];
				if(j != W-1) out << " ";
			}
			out << endl;
		}
	}
    return EXIT_SUCCESS;
}

