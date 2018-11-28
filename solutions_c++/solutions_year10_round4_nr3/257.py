#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

int grid[100][100], N, temp[100][100], res;

bool isNorth(int i, int j){
	return i-1 >= 0 && grid[i-1][j];
}
bool isWest(int i, int j){
	return j-1 >= 0 && grid[i][j-1];
}

void simulate(){

	res = 0;
	bool again = true;
	while(again){
		res++;
		again = false;
		memcpy(temp, grid, sizeof grid);

//		for(int i = 0 ; i < 5 ; i++){
//			for(int j = 0 ; j < 6 ; j++)
//				cout << grid[i][j];
//			cout << endl;
//		}
//		cout << endl;


		for(int i = 0 ; i < 100 ; i++)
			for(int j = 0 ; j < 100 ; j++){

				if(grid[i][j]){
					bool n = isNorth(i, j);
					bool w = isWest(i, j);
					if(!n && !w)
						temp[i][j] = 0;
				}else{
					bool n = isNorth(i, j);
					bool w = isWest(i, j);
					if(n && w)
						temp[i][j] = 1;
				}

				if(temp[i][j])
					again = true;
			}

		memcpy(grid, temp, sizeof grid);
	}
}

int main(){

	//freopen("1.in", "rt", stdin);
	//freopen("1.out", "wt", stdout);
	freopen("C-small-attempt0.in", "rt", stdin);
	freopen("C-small-attempt0.out", "wt", stdout);
	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){

		memset(grid, 0, sizeof grid);
		res = 0;

		cin >> N;
		for(int i = 0 ; i < N ; i++){
			int c1, r1, c2, r2; cin >> c1 >> r1 >> c2 >> r2;
			c1--;r1--;c2--;r2--;
			for(int r = r1 ; r <= r2 ; r++)
				for(int c = c1 ; c <= c2 ; c++)
					grid[r][c] = 1;
		}
		simulate();
		cout << "Case #" << t+1 << ": " << res << endl;
	}

	return 0;
}
