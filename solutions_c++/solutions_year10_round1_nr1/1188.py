#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <math.h>

using namespace std;

int nTestCases;
fstream	fin;
fstream fout;
int N, K;
char board[50][50];
char rotated[50][50];

void rotateBoard(){
	memset(rotated, '.', sizeof(rotated));
	for(int i=N-1; i>=0; i--){
		int row = N-1;
		for(int j=N-1; j>=0; j--){
			if(board[i][j]!='.'){
				rotated[row][N-1-i] =board[i][j];
				row--;
			}
		}
	}
}

bool testWin(char C){
	for(int i=0; i<N; i++){
		int nCount = 0;
		for(int j=0; j<N; j++){
			if(rotated[i][j] == C){
				nCount++;
				if(nCount == K)
					return true;
			}
			else
				nCount=0;
		}
	}

	for(int i=0; i<N; i++){
		int nCount = 0;
		for(int j=0; j<N; j++){
			if(rotated[j][i] == C){
				nCount++;
				if(nCount == K)
					return true;
			}
			else
				nCount=0;
		}
	}

	for(int s=0; s<2*N-1; s++){
		int nCount = 0;
		int i=s;
		for(int j=0; j<N;){
			if(i>=0 && i<N){
				if(rotated[i][j] == C){
					nCount++;
					if(nCount == K)
						return true;
				}
				else
					nCount=0;
			}
			i--;
			j++;
		}
	}

	for(int s=-(N-1); s<N; s++){
		int nCount = 0;
		int i=s;
		for(int j=0; j<N;){
			if(i>=0 && i<N){
				if(rotated[i][j] == C){
					nCount++;
					if(nCount == K)
						return true;
				}
				else
					nCount=0;
			}
			i++;
			j++;
		}
	}

	return false;
}

void main()
{
	fin.open("z:\\input.txt", ifstream::in);
	fout.open("z:\\output.txt", ifstream::out);


	fin >> nTestCases;

	for(int testCase = 1; testCase <= nTestCases; testCase++){
		fin >> N >> K;
		for(int i=0; i<N; i++)
			fin >> board[i];

			rotateBoard();
		
			bool RWin, BWin;
			RWin = testWin('R');
			BWin = testWin('B');

			fout << "Case #" << testCase <<": ";
			if(RWin){
				if(BWin)
					fout << "Both" << endl;
				else
					fout << "Red" << endl;
			}
			else if(BWin)
				fout << "Blue" << endl;
			else
				fout << "Neither" << endl;
	}

	fin.close();
	fout.close();
}