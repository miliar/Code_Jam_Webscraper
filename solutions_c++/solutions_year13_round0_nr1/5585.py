/*
 * =====================================================================================
 *
 *       Filename:  tic-tac.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Saturday 13 April 2013 10:08:01  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:   (), 
 *        Company:  
 *
 * =====================================================================================
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
void print(vector<string> &a){
	for(int i=0;i<int(a.size());i++) cout << a[i] << endl;
	cout << endl;
}
bool iswin(vector<string> &s, char c){
	for(int i=0;i<4;i++){
		if(s[i][0] == c && s[i][1] == c && s[i][2] == c && s[i][3] == c) return true;
		if(s[0][i] == c && s[1][i] == c && s[2][i] == c && s[3][i] == c) return true;
	}
	if(s[0][0] == c && s[1][1] == c && s[2][2] == c && s[3][3] == c) return true;
	if(s[0][3] == c && s[1][2] == c && s[2][1] == c && s[3][0] == c) return true;
	return false;
}
bool isended(vector<string> &s){
	for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(s[i][j] == '.') return false;
	return true;
}
int main(){
	string input;
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		vector<string> s;
		for(int i=0;i<4;i++) { cin >> input; s.push_back(input); }
		//print(s);
		int tc, tr;
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) if(s[i][j] == 'T') { tr=i;tc=j;}
		string res = "";
		s[tr][tc] = 'O';
		if(iswin(s, 'O')) res = "O won";
		
		s[tr][tc] = 'X';
		if(iswin(s, 'X')) res = "X won";
		
		s[tr][tc] = 'T';
		if(res.size() == 0) {
			if (isended(s)) res = "Draw";
			else res = "Game has not completed";
		}
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	return 0;
}

