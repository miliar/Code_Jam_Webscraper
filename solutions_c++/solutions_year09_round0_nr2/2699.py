#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int linkTo[10000];
char result[10000];
int MAX_ALTITUTES;

void flowback(int nowNum,char mark){
	result[nowNum] = mark;
	for(int i = 0 ; i < MAX_ALTITUTES ; i++){
		if(linkTo[i] == nowNum) flowback(i,mark);
	}
	return;
}
int targetToNW(int toNum){
	if(linkTo[toNum] == -1) return toNum;
	return targetToNW(linkTo[toNum]);
}

int main(){

	ifstream ifs;
	ifs.open("B-small-attempt2.in");
	ofstream ofs;
	ofs.open("B-small-attempt2.out");
	

	int aMap[100][100];
	
	int H = 0;
	int W = 0;
	int min;

	int tc;
	ifs>>tc;
	for(int caseCnt = 1; caseCnt <= tc; caseCnt++){

		memset(result,0,sizeof(result));
		memset(aMap,0,sizeof(aMap));
		memset(linkTo,0,sizeof(linkTo));

		ifs>>H>>W;
		MAX_ALTITUTES = H*W;

		int t;
		for(int i = 0 ; i < H ; i++){
			for(int j = 0 ; j < W ; j++){
				ifs>>t;
				aMap[i][j] = t;
			}
		}
		int mini;
		int minj;
		for(int i = 0 ; i < H ; i++){
			for(int j = 0 ; j < W ; j++){
				min = aMap[i][j];

				if(i-1 >= 0){
					if(aMap[i-1][j] < min){
						min = aMap[i-1][j];
						mini = i-1;
						minj = j;
					}
				}
				if(j-1 >= 0){
					if(aMap[i][j-1] < min) {
						min = aMap[i][j-1];
						mini = i;
						minj = j-1;
					}
				}
				if(j+1 < W){
					if(aMap[i][j+1] < min) {
						min = aMap[i][j+1];
						mini = i;
						minj = j+1;
					}
				}
				if(i+1 < H){
					if(aMap[i+1][j] < min) {
						min = aMap[i+1][j];
						mini = i+1;
						minj = j;
					}
				}
				

				if(min == aMap[i][j]) linkTo[(i*W) + (j)] = -1;
				else linkTo[(i*W) + (j)] = (mini*W) + (minj) ;
			}
		}
		char mark = 'a';
		int idxA = targetToNW(0);

		result[idxA] = mark;
		flowback(idxA,mark++);
		
		for(int i = 0 ; i < MAX_ALTITUTES ; i++){
			if(linkTo[i] == -1 && i != idxA){
				result[i] = mark;
				flowback(i,mark++);
			}
		}
		int tempIdx = 0;
		ofs<<"Case #"<<caseCnt<<":"<<endl;
		for(int i = 0 ; i < H ; i++){
			for(int j = 0 ; j < W ; j++){
				ofs<<result[tempIdx++]<<" ";
			}
			ofs<<endl;
		}
	}

	ifs.close();
	return 0;
}