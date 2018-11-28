//============================================================================
// Name        : Codejame.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

char arr[4][4];
string ret;
bool check(string find[]) {

	ret = "";
	string str, str2;
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			str += arr[i][j];
			str2 += arr[j][i];
		}
		for (int x = 0; x < 10; x++) {
			if (str == find[x] || str2 == find[x]) {
				ret = find[x];
				return true;
			}
		}
		str = "";
		str2 = "";
	}

	for (int i = 0; i < 4; i++) {
		str += arr[i][i];
		str2 += arr[i][3 - i];
	}

	for (int x = 0; x < 10; x++) {
		if (str == find[x] || str2 == find[x]) {
			ret = find[x];
			return true;
		}
	}

	return false;
}
bool draw(){
	for(int  i = 0 ;i < 4;i++){
		for(int j = 0; j < 4 ;j++){
			if(arr[i][j] == '.')return false;
		}
	}
	return true;
}
int main() {

#ifndef ONLINE_JUDGE
	freopen("out.txt", "rt", stdin);
	freopen("in.txt", "wt", stdout);
#endif
	string f[10] = { "XXXT", "XXTX", "XTXX", "TXXX", "OOOT", "OOTO", "OTOO",
			"TOOO", "OOOO", "XXXX" };

	int tc = 0 ,cas = 1;

	cin >> tc;

	while (tc--) {

		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> arr[i][j];
			}
		}
		cout<<"Case #"<<cas<<": ";
		if (check(f)) {
			if (ret[0] == 'X')
				cout << "X won" << endl;
			else if (ret[0] == 'T' && ret[1] == 'X')
				cout << "X won" << endl;
			else if (ret[0] == 'O')
				cout << "O won" << endl;
			else if (ret[0] == 'T' && ret[1] == 'O')
				cout << "O won";
		} else {
			if(draw())cout<<"Draw"<<endl;
			else cout<<"Game has not completed"<<endl;
		}
		cas++;
	}

	return 0;
}
