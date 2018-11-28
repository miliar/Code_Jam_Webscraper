/**
 * Codejam template
 * - daftmutt
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <new>
#include <memory>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

const int MAXN = 50 + 5;

int TC;

int N, K;

char board[MAXN][MAXN];
char boardR[MAXN][MAXN];
char win;
void rotate(){
	for (int i = 0; i < N; i++){
		int col = (N - 1) - i;
		for (int j = 0; j < N; j++){
			boardR[j][col] = board[i][j];
		}
	}
}

void gravity(){
	for (int i = N - 1; i > 0; i--){
		for (int j = 0; j < N; j++){
			if (boardR[i][j] == '.'){
				for (int t = i - 1; t >= 0; t--){
					if (boardR[t][j]!='.'){
						boardR[i][j] = boardR[t][j];
						boardR[t][j] = '.';
						break;
					}
				}
			}
		}
	}
}

void checkRow(){
	for (int i = 0; i < N; i++){
		int count  = 0;
		char player;
		for (int j = 0; j < N; j++){
			if (boardR[i][j] == '.'){
				continue;
			} else if (boardR[i][j] == player){
				++count;
				if (count == K){
					if (win == 'N') win = player;
					if (win != 'N' && win != player) win = 'T';
				}
			} else {
				count = 1;
				player = boardR[i][j];
			}
		}
	}
}

void checkCol(){
	for (int j = 0; j < N; j++){
		int count  = 0;
		char player;
		for (int i = 0; i < N; i++){
			if (boardR[i][j] == '.'){
				continue;
			} else if (boardR[i][j] == player){
				++count;
				if (count == K){
					if (win == 'N') win = player;
					if (win != 'N' && win != player) win = 'T';
				}
			} else {
				count = 1;
				player = boardR[i][j];
			}
		}
	}
}

void checkDiagR(){
	for (int i = 0; i < N; i++){
		if ((i + K - 1) >= N) continue;
		for (int j = 0; j < N; j++){
			if ((j + K - 1) >= N) continue;
			if (boardR[i][j] == '.') continue;
			char player = boardR[i][j];
			int count = 1;
			for (; count < K && count > 0;){
				if (boardR[i+count][j+count] == boardR[i][j]){
					++count;
				}
				else {
					count = 0-K;
				}
			}
			if (count == K){
				if (win == 'N') win = player;
				if (win != 'N' && win != player) win = 'T';
			}
		}
	}
}

void checkDiagL(){
	for (int i = 0; i < N; i++){
		if ((i + K - 1) >= N) continue;
		for (int j = 0; j < N; j++){
			if ((j - K + 1) < 0) continue;
			if (boardR[i][j] == '.') continue;
			char player = boardR[i][j];
			int count = 1;
			for (; count < K && count > 0;){
				if (boardR[i+count][j-count] == boardR[i][j]){
					++count;
				}
				else {
					count = 0-K;
				}
			}
			if (count == K){
				if (win == 'N') win = player;
				if (win != 'N' && win != player) win = 'T';
			}
		}
	}
}
int main()
{
	
	cin >> TC;
	 
	for (int C = 1; C <=TC; C++)
	{
		win = 'N';
		cin >> N >> K;
		
		memset (board, '.', sizeof(board));
		memset (boardR, '.', sizeof(boardR));
		for (int i = 0; i < N; i++){
			cin >> board[i];
		}
		
		rotate();
		
		gravity();
		
		checkRow();
		checkCol();
		checkDiagR();
		checkDiagL();
		
		cout << "Case #" << C << ": ";
		if (win == 'N') cout << "Neither";
		if (win == 'R') cout << "Red";
		if (win == 'B') cout << "Blue";
		if (win == 'T') cout << "Both";
		cout << "\n";
	}
}
