/*
 * =====================================================================================
 *
 *       Filename:  ProblemA.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/13/2013 10:04:45
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Cong Zhao (), zhaocong89@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */
#include <stdlib.h>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define FF(i,n) for(int(i)=0;(i)<(n);(i)++)
#define FOR(i,l,h) for(int(i)=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
#define CC(n,what) memset(n,what,sizeof(n))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

char gameBoard[4][5];
int isWon(char cha){
	// check the row
	for(int i = 0; i < 4; i++){
		int tmpResult = 1;
		for(int j = 0; j < 4; j++){
			if(!(gameBoard[i][j] == cha || gameBoard[i][j] == 'T')){
				tmpResult = 0;
				break;
			}
		}
		if(tmpResult == 1){
			return 1;
		}
	}

	// check the col
	for(int i = 0; i < 4; i++){
		int tmpResult = 1;
		for(int j = 0; j < 4; j++){
			if(!(gameBoard[j][i] == cha || gameBoard[j][i] == 'T')){
				tmpResult = 0;
				break;
			}
		}
		if(tmpResult == 1){
			return 1;
		}
	}
	
	// check the diag
	int tmpResult = 1;
	for(int i = 0; i < 4; i++){
		if(!(gameBoard[i][i] == cha || gameBoard[i][i] == 'T')){
			tmpResult = 0;
			break;
		}
	}
	if(tmpResult == 1){
		return 1;
	}
	
	tmpResult = 1;
	for(int i = 0; i < 4; i++){
		if(!(gameBoard[i][3 - i] == cha || gameBoard[i][3 - i] == 'T')){
			tmpResult = 0;
			break;
		}
	}
	if(tmpResult == 1){
		return 1;
	}

	return 0;
}

int main(){
	int ncase = 0;
	scanf("%d\n", &ncase);
	for(int nn = 1; nn <= ncase; nn++){
		memset(gameBoard, 0, sizeof(gameBoard));
		int empty = 0;
		for(int i = 0; i < 4; i++){
			scanf("%s", gameBoard[i]);
			for(int j = 0; j < 4; j++){
				if(gameBoard[i][j] == '.'){
					empty = 1;
				}
			}
		}
		if(isWon('X')){
			printf("Case #%d: X won\n", nn);
		}
		else if(isWon('O')){
			printf("Case #%d: O won\n", nn);
		}
		else if(empty == 0){
			printf("Case #%d: Draw\n", nn);
		}
		else{
			printf("Case #%d: Game has not completed\n", nn);
		}
	}
	return 0;
}
