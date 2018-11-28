#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdlib>
#include <map>
#include <queue>

#define LL long long int
#define FOR(i, s, e) for (int i=(s);i<(e);i++)
#define FOE(i, s, e) for (int i=(s);i<=(e);i++)
#define FOD(i, s, e) for (int i=(e)-1;i>=(s);i--)
#define CLR(x, a) memset(x, a, sizeof(x))

using namespace std;

#define N 4

int dx[8] = {0, 1, 1, 1, 0, -1, -1, -1};
int dy[8] = {1, 1, 0, -1, -1, -1, 0, 1};
int testcase, full, end, win, sx, sy;
char board[N][N];
string ret;

int main(){
	scanf("%d", &testcase);
	
	FOR(TC, 0, testcase){
		full = 1;
		FOR(i, 0, N){
			scanf("%s", board[i]);
			FOR(j, 0, N)
				if (board[i][j] == '.') full = 0;
		}
		
		end = 0;
		
		FOR(i, 0, N)
		FOR(j, 0, N){
			if (board[i][j] == '.' || board[i][j] == 'T') continue;
			FOR(d, 0, 8){
				win = 1;
				FOR(k, 1, N){
					sx = i + dx[d] * k;
					sy = j + dy[d] * k;
					if (sx < 0 || sx >= N || sy < 0 || sy >= N) win = 0;
					if (board[sx][sy] == '.') win = 0;
					if (board[sx][sy] != board[i][j] && board[sx][sy] != 'T') win = 0;
				}
				if (win){
					end = 1;
					if (board[i][j] == 'X') ret = "X won";
					else ret = "O won";
					//printf("WINNING AT [%d %d]\n", i, j);
				}
			}
		}
		
		if (!end){
			if (full) ret = "Draw";
			else ret = "Game has not completed";
		}

		cout << "Case #" << TC + 1 << ": " << ret << endl;
		
	}
	return 0;
}
