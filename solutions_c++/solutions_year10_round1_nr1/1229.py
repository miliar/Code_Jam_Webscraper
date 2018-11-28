/*
 * 1a.cpp
 *
 *  Created on: May 21, 2010
 *      Author: Justin Li
 */
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <utility>
#include <queue>
#include <stack>
#include <fstream>
using namespace std;

void printboard(int board[50][50], int N) {
	for (int j=0;j<N;j++) {
		for (int k=0;k<N;k++) {
			cout << board[j][k];
		}
		cout << endl;
	}
	cout << endl;
}

int main() {
	ifstream in;
	in.open("A-small-attempt1.in.txt"); //IS THIS RIGHT?
	ofstream out;
	out.open("/file3.out"); //IS THIS RIGHT?
	int i, j, k, T, N, K, x, y;
	int board[50][50], rotboard[50][50];
	char temp;
	in >> T;
	for (i=0; i<T; i++) {
		in >> N >> K;
		for (j=0; j<N; j++) {
			for (k=0; k<N; k++) {
				in >> temp;
				board[j][k] = temp=='B'?2:temp=='R'?1:0;
				//cout << board[j][k];
				rotboard[k][N-j-1] = board[j][k];
			}
			//cout << endl;
		}
		for (j=N-1; j>=0; j--) {
			for (k=0; k<N; k++) {
				if (rotboard[j][k]) {
					y=j+1;
					//cout << j << " " << k << endl;
					while (!rotboard[y][k] && y<N) {
						//cout << y << endl;
						rotboard[y][k] = rotboard[y-1][k];
						rotboard[y-1][k] = 0;
						y++;
						//printboard(rotboard,N); cout << endl;
					}
				}
			}
		}//cout << endl;printboard(rotboard,N);
		int cver, cverlast, chor, chorlast, cdiagl, cdiagllast, cdiagr, cdiagrlast;
		bool red, blue;
		for (j=0;j<N;j++) {
			for (k=0;k<N;k++) {
				if (rotboard[j][k]==0) {
					cver=0;
					cverlast=0;
					cdiagl=0;
					cdiagllast=0;
					cdiagr=0;
					cdiagrlast=0;
				}
				if (rotboard[k][j]==0) {
					chor=0;
					chorlast=0;
				}

				if (rotboard[j][k]==1) {
					if (cverlast==1) cver++;
					else cver = 1;
				} else if (rotboard[j][k]==2) {
					if (cverlast==2) cver++;
					else cver = 1;
				}
				if (cver==K) {
					if (rotboard[j][k]==1)
					red=true; else blue=true;
				}

				cverlast = rotboard[j][k];
				if (rotboard[k][j]==1) {
					if (chorlast==1) chor++;
					else chor = 1;
				} else if (rotboard[k][j]==2) {
					if (chorlast==2) chor++;
					else chor = 1;
				}
				if (chor==K) {
					if (rotboard[k][j]==1)
					red=true; else blue=true;
				}

				chorlast = rotboard[k][j];
			}
			cver=0;cverlast=0;chor=0;chorlast=0;
		}
		for (j=0; j<N; j++) {
			for (k=0;k<=j;k++) {
				if (rotboard[j-k][k]==0) {
					chor=0;chorlast=0;
				}
				if (rotboard[N-1-j+k][N-1-k]==0) {
					cver=0;cverlast=0;
				}
				if (rotboard[j-k][k]==1) {
					if (chorlast==1) chor++;
					else chor = 1;
				} else if (rotboard[j-k][k]==2) {
					if (chorlast==2) chor++;
					else chor = 1;
				}
				if (chor==K) {
					//cout << "...";

					if (rotboard[j-k][k]==1)
					red=true; else blue=true;
				}

					if (rotboard[N-1-j+k][N-1-k]==1) {
						if (cverlast==1) cver++;
						else cver = 1;
					} else if (rotboard[N-1-j+k][N-1-k]==2) {
						if (cverlast==2) cver++;
						else cver = 1;
					}
					if (cver==K) {
						//cout << "...";

						if (rotboard[N-1-j+k][N-1-k]==1)
						red=true; else blue=true;
					}
				//cout <<N-1-j+k << " " << N-1-k << " " << cver << " " << cverlast << endl;

				cverlast = rotboard[N-1-j+k][N-1-k];
			}
			cver=0;cverlast=0;chor=0;chorlast=0;
			//cout << endl;
		}
		for (j=N-1; j>=0; j--) {
			for (k=N-1;k>=j;k--) {
				if (rotboard[j-k][k]==0) {
					chor=0;chorlast=0;
				}
				if (rotboard[N-1+j-k][N-1-k]==0) {
					cver=0;cverlast=0;
				}
				if (rotboard[j-k][k]==1) {
					if (chorlast==1) chor++;
					else chor = 1;
				} else if (rotboard[j-k][k]==2) {
					if (chorlast==2) chor++;
					else chor = 1;
				}
				if (chor==K) {
					//cout << "...";

					if (rotboard[j-k][k]==1)
					red=true; else blue=true;
				}

					if (rotboard[N-1+j-k][N-1-k]==1) {
						if (cverlast==1) cver++;
						else cver = 1;
					} else if (rotboard[N-1+j-k][N-1-k]==2) {
						if (cverlast==2) cver++;
						else cver = 1;
					}
					if (cver==K) {
						//cout << "...";

						if (rotboard[N-1+j-k][N-1-k]==1)
						red=true; else blue=true;
					}
				//cout << k-j << " " << k << " " << cver << " " << cverlast << endl;

				cverlast = rotboard[N-1+j-k][N-1-k];
			}
			cver=0;cverlast=0;chor=0;chorlast=0;
			//cout << endl;
		}
		//cout << red << " " << blue << endl;
		if (red&&blue) {
			cout << "Case #" << i+1 << ": " << "Both";
		} else if (red) {
			cout << "Case #" << i+1 << ": " << "Red";
		} else if (blue) {
			cout << "Case #" << i+1 << ": " << "Blue";
		} else {
			cout << "Case #" << i+1 << ": " << "Neither";
		}
		cout << endl;
		red=false;blue=false;
	}
	in.close();
	out.close();
	return 0;
}
