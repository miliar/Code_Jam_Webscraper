
#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>

// Libraries easily and freely downloadable from cs106b.stanford.edu
// Also, way easy to use.
#include "genlib.h"
#include "simpio.h"
#include "stack.h"
#include "vector.h"
#include "scanner.h"

string executeCase(FILE* fp);

string executeCase(FILE* fp) {
	int N, K;
	fscanf(fp, "%d %d\n", &N, &K);
	//cout << N << " " << K << endl;
	char array[N][N];
	char enter;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			fscanf(fp, "%c", &(array[i][j]));
		}
		fscanf(fp, "%c", &enter);
	}
	char rotated[N][N];
	int cur = N-1;
	for (int i = 0; i < N; i++) {
		for (int j = N-1; j >= 0; j--) {
			if (array[i][j] == 'R' || array[i][j] == 'B') {
				rotated[cur--][i] = array[i][j];
			}
		}
		for (; cur >= 0; cur--) {
			rotated[cur][i] = '.';
		}
		cur = N-1;
	}
	
	/*for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << rotated[i][j];
		}
		cout << endl;
	}
	cout << endl;*/
	
	bool canRWin = false;
	bool canBWin = false;
	
	int count = 0;
	char last = '.';
	
	// horizontal
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if ((rotated[i][j] == 'R' || rotated[i][j] == 'B')) {
				if (rotated[i][j] == last) {
					count++;
				} else {
					count = 1;
				}

				if (count == K) {
					if (rotated[i][j] == 'R') {
						canRWin = true;
					} else {
						canBWin = true;
					}

				}
				last = rotated[i][j];
			} else {
				last = '.';
				count = 0;
			}

		}
		count = 0;
		last = '.';
	}
	
	// vertical
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			if ((rotated[i][j] == 'R' || rotated[i][j] == 'B')) {
				if (rotated[i][j] == last) {
					count++;
				} else {
					count = 1;
				}
				
				if (count == K) {
					if (rotated[i][j] == 'R') {
						canRWin = true;
					} else {
						canBWin = true;
					}
					
				}
				last = rotated[i][j];
			} else {
				last = '.';
				count = 0;
			}
			
		}
		count = 0;
		last = '.';
	}
	
	//diag
	
	for (int i = 0; i < N - K; i++) {
		int start = i;
		for (int j = 0; start < N; start++, j++) {
			//cout << rotated[start][j];
			if ((rotated[start][j] == 'R' || rotated[start][j] == 'B')) {
				if (rotated[start][j] == last) {
					count++;
				} else {
					count = 1;
				}
				
				if (count == K) {
					if (rotated[start][j] == 'R') {
						canRWin = true;
					} else {
						canBWin = true;
					}
					
				}
				last = rotated[start][j];
			} else {
				last = '.';
				count = 0;
			}
			
		}
		count = 0;
		last = '.';
		//cout << endl;
	}
	
	for (int j = 1; j <= N - K; j++) {
		int start = j;
		for (int i = 0; start < N; start++, i++) {
			//cout << rotated[i][start];
			if ((rotated[i][start] == 'R' || rotated[i][start] == 'B')) {
				if (rotated[i][start] == last) {
					count++;
				} else {
					count = 1;
				}
				
				if (count == K) {
					if (rotated[i][start] == 'R') {
						canRWin = true;
					} else {
						canBWin = true;
					}
					
				}
				last = rotated[i][start];
			} else {
				last = '.';
				count = 0;
			}
			
		}
		//cout << endl;
		count = 0;
		last = '.';
		
	}
	
	//cout << endl;
	
	// check other diagonal
	for (int i = K - 1; i < N; i++) {
		int start = i;
		for (int j = 0; start >= 0; start--, j++) {
			//cout << rotated[start][j];
			if ((rotated[start][j] == 'R' || rotated[start][j] == 'B')) {
				if (rotated[start][j] == last) {
					count++;
				} else {
					count = 1;
				}
				
				if (count == K) {
					if (rotated[start][j] == 'R') {
						canRWin = true;
					} else {
						canBWin = true;
					}
					
				}
				last = rotated[start][j];
			} else {
				last = '.';
				count = 0;
			}
			
		}
		//cout << endl;
		count = 0;
		last = '.';
		
	}
	
	for (int j = 1; j <= N - K; j++) {
		int start = j;
		for (int i = N-1; start < N; start++, i--) {
			//cout << rotated[i][start];
			if ((rotated[i][start] == 'R' || rotated[i][start] == 'B')) {
				if (rotated[i][start] == last) {
					count++;
				} else {
					count = 1;
				}
				
				if (count == K) {
					if (rotated[i][start] == 'R') {
						canRWin = true;
					} else {
						canBWin = true;
					}
					
				}
				last = rotated[i][start];
			} else {
				last = '.';
				count = 0;
			}
			
		}
		//cout << endl;
		count = 0;
		last = '.';
		
	}
	
	//cout << endl;
	//check vertical
	/*for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			if ((rotated[i][j] == 'R' || rotated[i][j] == 'B') && rotated[i][j] == lastSeen) {
				foundInRow++;
				if (foundInRow == K) {
					if (rotated[i][j] == 'R') {
						canRWin = true;
					} else {
						canBWin = true;
					}
					
				}
			}
			else {
				lastSeen = rotated[i][j];
			}
		}	
		foundInRow = 0;
		lastSeen = '.';
	}
	
	//check right diagonal
	int foundInRow = 0;
	char lastSeen = '.';
	for (int i = 0; i < N - K; i++) {
		for (int j = 0; j < N; j++) {
			if ((array[i][j] == 'R' || array[i][j] == 'B') && array[i][j] == lastSeen) {
				foundInRow++;
				if (foundInRow == K) {
					if (array[i][j] == 'R') {
						canRWin = true;
					} else {
						canBWin = true;
					}
					
				}
			} else {
				lastSeen = array[i][j];
			}
			
		}
		foundInRow = 0;
		lastSeen = '.';
	}*/
	if (canBWin && canRWin) {
		return "Both";
	} else if (canBWin) {
		return "Blue";
	} else if (canRWin) {
		return "Red";
	}
	return "Neither";
	
}


int main() {
	FILE* fp = fopen("A.in", "r");
	FILE* fpOut = fopen("A.out", "w");
	
	// get num cases
	int numCases;
	fscanf(fp, "%d", &numCases);
	// go go go!
	string answer;
	for (int i = 0; i < numCases; i++) {
		answer = executeCase(fp);
		fprintf(fpOut, "Case #%d: %s\n", i+1, answer.c_str());
	}
	
	fclose(fp);
	fclose(fpOut);
	return 0;
}



