// Test.cpp : Defines the entry point for the console application.
//
#include <time.h>
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

int check(string s[], char c) {
	int flag;
	for (int i = 0; i < 4; ++i) {
		flag = 1;
		for (int j = 0; j < 4; ++j) {
			if (s[i][j] != c && s[i][j] != 'T') {
				flag = 0;
				break;
			}
		}
		if (flag) {
			cout<<c<<" won"<<endl;
			return 1;
		}
	}
	for (int i = 0; i < 4; ++i) {
		flag = 1;
		for (int j = 0; j < 4; ++j) {
			if (s[j][i] != c && s[j][i] != 'T') {
				flag = 0;
				break;
			}
		}
		if (flag) {
			cout<<c<<" won"<<endl;
			return 1;
		}
	}
	flag = 1;
	for (int i = 0; i < 4; ++i) {
		if (s[i][i] != c && s[i][i] != 'T') {
			flag = 0;
			break;
		}
	}
	if (flag) {
		cout<<c<<" won"<<endl;
		return 1;
	}
	flag = 1;
	for (int i = 0; i < 4; ++i) {
		if (s[i][3 - i] != c && s[i][3 - i] != 'T') {
			flag = 0;
			break;
		}
	}
	if (flag) {
		cout<<c<<" won"<<endl;
		return 1;
	}
	return 0;
}

void solve() {
	string s[4];
	for (int i = 0; i < 4; ++i) {
		cin>>s[i];
	}
	if (!check(s, 'X') && !check(s, 'O')) {
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if (s[i][j] == '.') {
					cout<<"Game has not completed"<<endl;
					return;
				}
			}
		}
		cout<<"Draw"<<endl;
	}
}

int main(int argc, char* argv[]) {
	int n;
	cin>>n;
	for (int i = 0; i < n; ++i) {
		cout<<"Case #"<<i + 1<<": ";
		solve();
	}
}