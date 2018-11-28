/*
 *	Category: CodeJam
 *  Problem: A.Tic-Tac-Toe-Tomek.cpp
 *  Status: 
 * 	Date: Apr 13, 2013
 * 	Time: 1:56:30 AM
 * 	Author: Hossam Yousef
 */

#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <algorithm>

using namespace std;

char XOT[4][4];

int main() {
	freopen("test.txt", "rt", stdin);
		freopen("o.txt", "wt", stdout);
	int tc; scanf("%d",&tc);
	for(int t = 0; t < tc; t++){
		int countRx = 0, countCx = 0, countD1x = 0, countD2x = 0;
		int countRo = 0, countCo = 0, countD1o = 0, countD2o = 0;
		bool found = false;
		int dots = 0;
		for(int i = 0; i < 4; i++)
					for(int j = 0; j < 4; j++){
						cin >> XOT[i][j];
						if(XOT[i][j] == '.')dots++;
					}
		printf("Case #%d: ",t+1);
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(j == 0) countRx = 0;
				if(XOT[i][j] == 'X' || XOT[i][j] == 'T'){

					countRx++;
					if(countRx == 4){
						printf("X won\n");
						found = true;
						break;
					}
				}
				if(j == 0) countCx = 0;
				if(XOT[j][i] == 'X' || XOT[j][i] == 'T'){

					countCx++;
					if(countCx == 4){
						printf("X won\n");
						found = true;
						break;
					}
				}
				if(j == 0) countD1x = 0;
				if(XOT[j][j] == 'X' || XOT[j][j] == 'T'){

					countD1x++;
					if(countD1x == 4){
						printf("X won\n");
						found = true;
						break;
					}
				}
				if(j == 0) countD2x = 0;
				if(XOT[j][3-j] == 'X' || XOT[j][3-j] == 'T'){

					countD2x++;
					if(countD2x == 4){
						printf("X won\n");
						found = true;
						break;
					}
				}
				if(j == 0) countRo = 0;
				if(XOT[i][j] == 'O' || XOT[i][j] == 'T'){

					countRo++;
					if(countRo == 4){
						printf("O won\n");
						found = true;
						break;
					}
				}if(j == 0) countCo = 0;
				if(XOT[j][i] == 'O' || XOT[j][i] == 'T'){

					countCo++;
					if(countCo == 4){
						printf("O won\n");
						found = true;
						break;
					}
				}
				if(j == 0) countD1o = 0;
				if(XOT[j][j] == 'O' || XOT[j][j] == 'T'){

					countD1o++;
					if(countD1o == 4){
						printf("O won\n");
						found = true;
						break;
					}
				}
				if(j == 0) countD2o = 0;
				if(XOT[j][3-j] == 'O' || XOT[j][3-j] == 'T'){

					countD2o++;
					if(countD2o == 4){
						printf("O won\n");
						found = true;
						break;
					}
				}
			}
			if(found) break;
		}
		if(!found && !dots) printf("Draw\n");
		if(!found && dots) printf("Game has not completed\n");
	}
	return 0;
}
