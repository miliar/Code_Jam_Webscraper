//============================================================================
// Name        : o.cpp
// Author      :
// Version     :bot trist
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,s,e) for (int i = int(s); i != int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()

vector<char> color;
vector<int> position;

bool checkdirec(int& o_next,int& b_next, int direc){
	int d1 =direc;
	if(color[d1] == 'O')  {
		o_next = position[d1];
		b_next = 99999;
		while( d1 <= position.size() ){
			if(color[d1] == 'B') {b_next = position[d1]; break;}
			d1++;
		}
//		cout << o_next << " " << b_next << endl;
		return true;
	}
	if(color[d1] == 'B')  {
		b_next = position[d1];
		o_next = 99999;
		while( d1 <= position.size() ){
			if(color[d1] == 'O') {o_next = position[d1]; break;}
			d1++;
		}
//		cout << o_next << " " << b_next << endl;
		return false;
	}
}

int sign(int v)
{
	return v > 0 ? 1 : (v < 0 ? -1 : 0);
}

int solve(){
	int turn = 0;
	int direc = 0;
	int o_now=1, b_now=1;
	int o_next=0, b_next=0;
	bool next;
	while(direc != position.size()){
		next = checkdirec( o_next, b_next, direc);
		if (next == true){ // orange's turn
			while(o_now != o_next){
				o_now += sign(o_next-o_now);
				if(b_now != b_next) b_now += sign(b_next-b_now);
				turn++;
			}
			// push button
			if(b_now != b_next) b_now += sign(b_next-b_now);
			turn++;
		}
		if (next == false){ // orange's turn
			while(b_now != b_next){
				b_now += sign(b_next-b_now);
				if(o_now != o_next) o_now += sign(o_next-o_now);
				turn++;
			}
			// push button
			if(o_now != o_next) o_now += sign(o_next-o_now);
			turn++;
		}
		direc++;
	}
	return turn;
}

int main() {
	int n_case, num;
	int position_temp;
	char color_temp;
	cin >> n_case; //
	vector<int> ans;
	for(int i = 0; i < n_case; i++){
    	cin >> num;
    	for(int k = 0; k < num; k++){
    		cin >> color_temp;
    		cin >> position_temp;
    		color.push_back(color_temp);
    		position.push_back(position_temp);
    	}
//    	ans.push_back(solve());
//    	FORIT(j, color) cout << *j << " ";
//        cout << endl;
//    	FORIT(j, position) cout << *j << " ";
//        cout << endl;
		cout << "Case #" << i+1 << ": " << solve() << endl;
//		cout << endl;
    	color.clear();
    	position.clear();
	}
	return 0;
}

