//{{{
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
//}}}


typedef long long LL; 
vector<vector<int> > board;

bool bacteria(int x, int y){
	if (x>=0 && y>=0 && x<board.size() && y<board[x].size()) return board[x][y];
	return 0; 
}

bool isempty(){
	for (int i=0;i<board.size();++i)
		for (int j=0;j<board[i].size();++j) if (board[i][j])
			return 0; 
	return 1; 
}

void simulate(){
	vector<vector<int> > nboard = board; 
	for (int i=0;i<board.size();++i) {
		for (int j=0;j<board[i].size();++j) {
			if (bacteria(i-1,j) && bacteria(i,j-1)) nboard[i][j]=1; 
			else if (!(bacteria(i-1,j) || bacteria(i, j-1))) nboard[i][j]=0; 
		}
	}
	board=nboard; 
}

int main(){
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z){
		int R;
		cin >> R;
		board = vector<vector<int> >(105, vector<int>(105));
		for (int i=0;i<R;++i) {
			int x1,x2,y1,y2; 
			cin >> x1 >> y1 >> x2 >> y2;
			for (int j=x1-1;j<x2;++j) {
				for (int k=y1-1;k<y2;++k) {
					board[j][k]=1; 
				}
			}
		}
		int result=0;
		while (!isempty()) {
			simulate();
			++result;
		}
		printf("Case #%d: %d\n", z,result);
	}
}
