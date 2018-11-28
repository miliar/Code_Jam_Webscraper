/*
 *  File: Program4.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 5/21/10.
 *
 */
 
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int N, K;
int Bwins;
int Rwins;
char table[50][50];
int res[50][50];


void setResToZero() {
	for(int j = 0; j < N; ++j) {
		for(int k = 0; k < N; ++k) {
			res[j][k] = 0;
		}
	}
}

void checkVert(char ch) {
	if(!((ch == 'B' && Bwins == 0) || (ch == 'R' && Rwins == 0))) {
		return;
	}
	//setResToZero();
	for(int k = 0; k < N; ++k) {
		for(int j = 0; j < N; ++j) {
			if(table[j][k] == '.') {
				continue;
			}
			if(table[j][k] == ch) {
				if(j == 0) {
					res[j][k] = 1;
				} else {
					res[j][k] = res[j-1][k] + 1;
				}
				if(res[j][k] == K) {
					if(ch == 'B') {
						Bwins = 1;
					} else {
						Rwins = 1;
					}
					return;
				}
			} else {
				res[j][k] = 0;
			}
		}
	}
	return;
}

void checkHoriz(char ch) {
	if(!((ch == 'B' && Bwins == 0) || (ch == 'R' && Rwins == 0))) {
		return;
	}
	for(int j = 0; j < N; ++j) {
		for(int k = 0; k < N; ++k) {
			if(table[j][k] == ch) {
				if(k == 0) {
					res[j][k] = 1;
				} else {
					res[j][k] = res[j][k-1] + 1;
				}
				if(res[j][k] == K) {
					if(ch == 'B') {
						Bwins = 1;
					} else {
						Rwins = 1;
					}
					return;
				}
			} else {
				res[j][k] = 0;
			}
		}
	}
	return;
}

void checkLDiag(char ch) {
	if(!((ch == 'B' && Bwins == 0) || (ch == 'R' && Rwins == 0))) {
		return;
	}
	for(int j = 0; j < N; ++j) {
		for(int k = 0; k < N; ++k) {
			if(table[j][k] == ch) {
				if(k > 0 && j > 0) {
					res[j][k] = res[j-1][k-1] + 1;
				} else {
					res[j][k] = 1;
				}
				if(res[j][k] == K) {
					if(ch == 'B') {
						Bwins = 1;
					} else {
						Rwins = 1;
					}
					return;
				}
			} else {
				res[j][k] = 0;
			}
		}
	}
	return;
}

void checkRDaig(char ch) {
	if(!((ch == 'B' && Bwins == 0) || (ch == 'R' && Rwins == 0))) {
		return;
	}
	char table1[50][50];
	for(int k = N-1; k >= 0; --k) {
		for(int j = 0; j < N; ++j) {
			table1[j][k] = table[N-1 - j][k];
		}
	}
	for(int j = 0; j < N; ++j) {
		for(int k = 0; k < N; ++k) {
			if(table1[j][k] == ch) {
				if(k > 0 && j > 0) {
					res[j][k] = res[j-1][k-1] + 1;
				} else {
					res[j][k] = 1;
				}
				if(res[j][k] == K) {
					if(ch == 'B') {
						Bwins = 1;
					} else {
						Rwins = 1;
					}
					return;
				}
			} else {
				res[j][k] = 0;
			}
		}
	}
	return;

}

void gravity() {
	for(int k = 0; k < N; ++k) {
		int c = 0;
		for(int j = 0; j < N; ++j) {
			if(table[j][k] != '.') {
				table[c++][k] = table[j][k];
			}
		}
		for(int j = c; j < N; ++j) {
			table[j][k] = '.';
		}
	}
	
}

void print() {
	for(int j = N-1; j >= 0; --j) {
		for(int k = 0; k < N; ++k) {
			cout << table[j][k];
		}
		cout << endl;
	}
}

int main() {
	freopen("/Users/erobeva/Downloads/A-large(2).in","r",stdin);
	freopen("/Users/erobeva/Downloads/AAAout.txt", "w", stdout);
	
	int T;
	cin >> T;
	
	
	//int vert[50][50];
	//int hor[50][50];
	//int ldiag[50][50];
	//int rdiag[50][50];
	for(int i =0; i < T; ++i) {
		cin >> N >> K;
		Bwins = 0;
		Rwins = 0;
		char table1[50][50];
		char table2[50][50];
		for(int j = 0; j < N; ++j) {
			for(int k = 0; k < N; ++k) {
				cin >> table1[j][k];
			}
		}
		for(int j = N-1; j >= 0; --j) {
			for(int k = 0; k < N; ++k) {
				table2[j][k] = table1[N-1 - j][k];
			}
		}
		/*for(int j = N-1; j >= 0; --j) {
			for(int k = 0; k < N; ++k) {
				cout << table1[j][k];
			}
			cout << endl;
		}*/
		/*for(int j = N-1; j >= 0; --j) {
			for(int k = 0; k < N; ++k) {
				cout << table2[j][k];
			}
			cout << endl;
		}*/
		for(int j = 0; j < N; ++j) {
			for(int k = 0; k < N; ++k) {
				table[N-1-k][j] = table2[j][k];
			}
		}
		//print();
		gravity();
		//print();
		checkVert('B');
		checkVert('R');
		setResToZero();
		checkHoriz('B');
		checkHoriz('R');
		setResToZero();
		checkLDiag('B');
		checkLDiag('R');
		setResToZero();
		checkRDaig('B');
		checkRDaig('R');
		cout << "Case #" << i + 1 << ": ";
		if(Bwins == 1 && Rwins == 1) {
			cout << "Both" << endl;
		} else {
			if(Bwins == 1) {
				cout << "Blue" << endl;
			} else {
				if(Rwins == 1) {
					cout << "Red" << endl;
				} else {
					cout << "Neither" << endl;
				}
			}
		}
	}
	
	
	return 0;
}