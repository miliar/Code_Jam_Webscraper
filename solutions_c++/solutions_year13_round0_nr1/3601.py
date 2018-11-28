//============================================================================
// Name        : GCJ2013_Q_1.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

char masu[4][4];

bool isTorX(char in){
	return (in == 'X' || in == 'T')? true : false;
}
bool isTorO(char in){
	return (in == 'O' || in == 'T')? true : false;
}

string check(char a, char b, char c, char d){
	string ans = "d";
	// x check
	if( isTorX(a) && isTorX(b) && isTorX(c) && isTorX(d)){
		ans = "X won";
	}else if(isTorO(a) && isTorO(b) && isTorO(c) && isTorO(d)){
		ans = "O won";
	}
	return ans;
}

string solve(bool isFinished){
	string ret;

	// ? won
	for(int i = 0; i < 4; i++){
		string ans = check(masu[i][0], masu[i][1], masu[i][2], masu[i][3]);
		if("d" == ans){
			continue;
		}else{
			return ans;
		}
	}
	for(int i = 0; i < 4; i++){
		string ans = check(masu[0][i], masu[1][i], masu[2][i], masu[3][i]);
		if("d" == ans){
			continue;
		}else{
			return ans;
		}
	}

	string ans = check(masu[0][0], masu[1][1], masu[2][2], masu[3][3]);
	if("d" != ans){
		return ans;
	}
	ans = check(masu[3][0], masu[2][1], masu[1][2], masu[0][3]);
	if("d" != ans){
		return ans;
	}



	if(isFinished){
		ret = "Draw";
	}else{
		ret ="Game has not completed";
	}
	return ret;

}
int main() {
	int testcase_num = 0;
	std::cin >> testcase_num;


	for(int i = 0; i < testcase_num; ++i){
		bool isFinished = true;

		// initialize
		for(int j = 0; j < 4; j++){// 4gyou
			for(int l = 0; l < 4; l++){ // 4retu
				cin >> masu[j][l];

				if(masu[j][l] == '.'){
					isFinished = false;
				}

				//cout << masu[j][l] << " " ;
			}
		}
		//cout << endl;


		string ans = solve(isFinished);

		cout << "Case #" << i+1 << ": " << ans << endl;
	}

	return 0;

}
