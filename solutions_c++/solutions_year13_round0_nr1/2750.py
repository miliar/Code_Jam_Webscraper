#include <iostream>
#include <fstream>
#include <conio.h>
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <algorithm>
#include <climits>
#include <bitset>
#include <math.h>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <map>
#include <set>
using namespace std;

string solve(vector<string>vec){
	int x,o,t,empty=0;
	for(int i=0; i<4; ++i){
		x=0;o=0;t=0;
		for(int j=0; j<4; ++j){
			if(vec[i][j]=='O')o++;
			if(vec[i][j]=='X')x++;
			if(vec[i][j]=='T')t++;
			if(vec[i][j]=='.')empty++;
		}
		if(x+t==4) return "X won";
		if(o+t==4) return "O won";
	}
	for(int i=0; i<4; ++i){
		x=0;o=0;t=0;
		for(int j=0; j<4; ++j){
			if(vec[j][i]=='O')o++;
			if(vec[j][i]=='X')x++;
			if(vec[j][i]=='T')t++;
			if(vec[j][i]=='.')empty++;
		}
		if(x+t==4) return "X won";
		if(o+t==4) return "O won";
	}
	x=0;o=0;t=0;
	for(int i=0; i<4; ++i){
		if(vec[i][i]=='X')x++;
		if(vec[i][i]=='O')o++;
		if(vec[i][i]=='T')t++;
	}
	if(x+t==4) return "X won";
	if(o+t==4) return "O won";
	x=0;o=0;t=0;
	for(int i=0; i<4; ++i){
		if(vec[i][3-i]=='X')x++;
		if(vec[i][3-i]=='O')o++;
		if(vec[i][3-i]=='T')t++;
	}
	if(x+t==4) return "X won";
	if(o+t==4) return "O won";

	if(!empty)return "Draw";
	return "Game has not completed";
}

int main(){
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	int n;
	cin >> n;
	string t;
	vector<string>vec(4);
	for(int i=0; i<n; ++i){
		cin >> vec[0] >> vec[1] >> vec[2] >> vec[3];
		printf("Case #%d: ",i+1);
		cout << solve(vec) << endl;
	}
}