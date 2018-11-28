#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

char s[4][10];

bool check(char c) {
	int num;
	for (int i=0;i<4;i++) {
		num=0;
		for (int j=0;j<4;j++)
			if (s[i][j]==c || s[i][j]=='T') num++;
		if (num==4) return true;
		num=0;
		for (int j=0;j<4;j++)
			if (s[j][i]==c || s[j][i]=='T') num++;
		if (num==4) return true;
	}
	num=0;
	for (int i=0;i<4;i++)
		if (s[i][i]==c || s[i][i]=='T') num++;
	if (num==4) return true;
	num=0;
	for (int i=0;i<4;i++)
		if (s[i][3-i]==c || s[i][3-i]=='T') num++;
	if (num==4) return true;
	return false;
}

void solve() {
	if (check('X')) {
		cout<<"X won"<<endl;
		return;
	}
	if (check('O')) {
		cout<<"O won"<<endl;
		return;
	}
	bool empty=false;
	for (int i=0;i<4;i++)
		for (int j=0;j<4;j++)
			if (s[i][j]=='.') empty=true;
	if (empty) cout<<"Game has not completed"<<endl;
	else cout<<"Draw"<<endl;
}

int main() {
	int T,kase=0;
	cin>>T;
	while (T--) {
		for (int i=0;i<4;i++)
			cin>>s[i];
		cout<<"Case #"<<++kase<<": ";
		solve();
	}
	return 0;				
}

