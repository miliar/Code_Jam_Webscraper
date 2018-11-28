/*
 * Watersheds.cpp
 *
 *  Created on: Sep 3, 2009
 *      Author: fu4ny
 */

#include <iostream>
#include <fstream>
using namespace std;
#define INPUT "input.txt"
#define OUTPUT "output.txt"
void flow();
int T,H,W;
int alt[102][102];
int flow_[102][102];
char res[102][102];
int main() {
	ifstream ifs(INPUT);
	ofstream ofs(OUTPUT);
	ifs >> T;
	for (int k=1; k<=T; k++ ) {
		ifs >> H >> W;
		for (int i=1; i<=H; i++)
			for (int j=1; j<=W; j++ )
				ifs >> alt[i][j];

		flow();
		char c = 'a';
		for ( int i=1;i<=H;i++ )
			for (int j=1;j<=W;j++)
				res[i][j] = '0';
		for ( int i=1;i<=H;i++ )
			for (int j=1;j<=W;j++)
				if (res[i][j] == '0' ) {
					res[i][j] = c;
					int same = flow_[i][j];
					for ( int ii = 1; ii<=H; ii++)
						for (int jj=1;jj<=W;jj++)
							if ( flow_[ii][jj] == same)
								res[ii][jj] = c;
					c++;
				}
		ofs << "Case #" << k << ": " << endl;
				for (int i=1; i<=H; i++)
				{
							for (int j=1; j<=W; j++ )
								ofs << res[i][j] << " ";
							ofs << endl;
				}


	}
	ifs.close();
	ofs.close();
}
bool check() {
	for ( int i=1; i<=H; i++)
		for ( int j=1; j<=W; j++ )
			if ( flow_[i][j] == 0)
				 return false;
	return true;
}

void run(int i, int j, int count) {
	int temp = alt[i][j];
	flow_[i][j] = count;
	if ( alt[i-1][j] > temp && flow_[i-1][j]==0 ) flow_[i-1][j] = count;
	if ( alt[i+1][j] > temp &&  flow_[i+1][j] ==0 ) flow_[i+1][j] = count;
	if ( alt[i][j-1] > temp && flow_[i][j-1]==0) flow_[i][j-1] = count;
	if ( alt[i][j+1] > temp &&flow_[i][j+1]==0) flow_[i][j+1] = count;
}

void flow() {
	for (int i=0; i<=H+1; i++ ) {
		alt[i][0] = -1;
		alt[i][W+1] = -1;
	}
	for (int j=0; j<=W+1; j++ ) {
		alt[0][j] = -1;
		alt[H+1][j] = -1;
	}
	for ( int i=1; i<=H; i++)
			for ( int j=1; j<=W; j++ )
				flow_[i][j] = 0;
	int count = 0;
	while ( !check() ) {
		int mini=1,minj=1;
		int min = 10001;
		for (int i=1; i<=H; i++)
			for (int j=1;j<=W;j++)
				if ( min > alt[i][j] && alt[i][j] != -1) {
					mini = i;
					minj = j;
					min = alt[i][j];
				}
		if ( flow_[mini][minj] == 0 ) {
			count++;
			run(mini,minj,count);
		} else run(mini,minj,flow_[mini][minj]);
		alt[mini][minj] = -1;
	}
}

