#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
int test, N, K;
const int MAXN = 55;
char board[MAXN][MAXN], tmp[MAXN][MAXN]; 
int dx[] = {0,1,1,1,0,-1,-1,-1};
int dy[] ={1,0,1,-1,-1,0,1,-1};
bool check(char c, int x, int y, int k, int dx, int dy){
	if(k == 0) return true;
	if(x >= N || y >= N || x < 0 || y < 0 ) return false;
	if(board[x][y] != c) return false;
	return check(c, x + dx, y + dy, k-1, dx, dy);
}
void rotate(){
	for(int i=N-1;i>=0; i--){
		for(int j = 0; j < N; j++){
			tmp[j][N-1-i] = board[i][j]; 
		}
	}
	for(int i=N-1; i>=0; i--){
		for(int j=0; j< N; j++){
			int x = i, y = j;
			while(x+1 < N && tmp[x][y] != '.' && tmp[x+1][y] == '.'){
				tmp[x+1][y] = tmp[x][y];
				tmp[x][y] = '.';
				x++;
			}
		}
	}
	REP(i,N){
		REP(j,N){
			board[i][j] = tmp[i][j];
		}
	}
}
int main() {
	ifstream fin("A-large.in");
	ofstream fout("a-large.out");
	fin>>test;
	for(int t = 1; t <= test; t ++ ){
		fin>>N>>K;
		fout<<"Case #"<<t<<": "; 
		REP(i,N){
			REP(j,N){
				fin>>board[i][j];
				tmp[i][j] = board[i][j];
			}
		}
		rotate();
		bool red = false;
		bool blue = false;
		REP(i,N){
			REP(j,N){
				for(int k=0;k<4;k++){
					red |= check('R', i, j, K, dx[k], dy[k]);
					blue |= check('B', i, j, K, dx[k], dy[k]);
				}	
			}
		}
		if(red && blue) fout<<"Both"<<endl;
		else if(red) fout<<"Red"<<endl;
		else if(blue) fout<<"Blue"<<endl;
		else fout<<"Neither"<<endl;
	}
    return 0;
}
