#include <cstdlib>
#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int T, K, N;

int B[50][50];
bool RED_WIN,BLUE_WIN;

void solve()
{
	RED_WIN = false;
	BLUE_WIN = false;
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N - 1; ++j) {
			if (B[i][j] != '.' && B[i][j + 1] == '.') {
				swap(B[i][j] , B[i][j + 1]);
				j = -1;
				continue;
			}
		}
	}
	
/*
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			printf("%c", B[i][j]);
		}
		printf("\n");
	}
*/
	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N; ++j) {
			if (B[i][j] == '.') continue;
			bool c1, c2, c3, c4;
			c1 = c2 = c3 = c4 = true;
			for (int k = 1; k < K; ++k) {
				if (c1 && (i + k >= N || B[i][j] != B[i + k][j]) ) c1 = false;
				if (c2 && (j + k >= N || B[i][j] != B[i][j + k]) ) c2 = false;
				if (c3 && (i + k >= N || j + k >= N || B[i][j] != B[i + k][j + k]) ) c3 = false;
				if (c4 && (i + k >= N || j - k < 0 || B[i][j] != B[i + k][j - k]) ) c4 = false;
			}
			if (c1 || c2 || c3 || c4) {
				//printf("%d, %d - %c\, %d, %d, %d, %d\n", i, j, B[i][j], c1, c2, c3, c4);
				if (B[i][j] == 'R') RED_WIN = true;
				else BLUE_WIN = true;
			}
		}
	}
	
	return;
}
				
int main(int argc, char *argv[])
{
    string x;
    
    cin >> T;
    
    for (int i = 0; i < T; ++i) {
		cin >> N >> K;
		memset(B, '.', sizeof(B) );
		for (int j = 0; j < N; ++j) {
			cin >> x;
			for (int k = 0; k < N; ++k) B[j][k] = x[k];
		}
		
		solve();
		if (RED_WIN) {
			if (BLUE_WIN) printf("Case #%d: Both\n", i + 1);
			else printf("Case #%d: Red\n", i + 1);
		} else {
			if (BLUE_WIN)  printf("Case #%d: Blue\n", i + 1);
			else  printf("Case #%d: Neither\n", i + 1);
		}
	}
	
    return EXIT_SUCCESS;
}
