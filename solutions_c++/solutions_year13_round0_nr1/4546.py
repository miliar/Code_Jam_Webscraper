#include<string>
#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;

int S[10][10];

bool draw() {
	int c=0;
	for (int i=1;i<5;i++) for (int j=1;j<5;j++) if (S[i][j]!='.') c++;
	if (c==16) return true;
	return false;
}

bool win(char ch) {
	for (int i=1;i<5;i++) {
		int c1=0,c2=0;
		for (int j=1;j<5;j++) {
			if (S[i][j]==ch) c1++;
			if (S[i][j]=='T') c2++;
		}
		if (c1==3 && c2==1) return true;
		if (c1==4) return true;
	}
	for (int i=1;i<5;i++) {
		int c1=0,c2=0;
		for (int j=1;j<5;j++) {
			if (S[j][i]==ch) c1++;
			if (S[j][i]=='T') c2++;
		}
		if (c1==3 && c2==1) return true;
		if (c1==4) return true;
	}

	int c1=0,c2=0;
	for (int i=1;i<5;i++) {
		if (S[i][i]==ch) c1++;
		if (S[i][i]=='T') c2++;
	}
	if (c1==3 && c2==1) return true;
	if (c1==4) return true;

	c1=0; c2=0;

	for (int i=1;i<5;i++) {
		if (S[i][4-i+1]==ch) c1++;
		if (S[i][4-i+1]=='T') c2++;
	}
	if (c1==3 && c2==1) return true;
	if (c1==4) return true;

	return false;

}

int main() {
	int t;
	cin >> t;
	for (int tc=1;tc<=t;tc++) {
		for (int i=1;i<5;i++) {
			string s;
			cin >> s;
			for (int j=1;j<5;j++) S[i][j]=s[j-1];
		}
		if (win('O')) cout << "Case #" << tc << ": O won" << endl;
		else if (win('X')) cout << "Case #" << tc << ": X won" << endl;
		else if (draw()) cout << "Case #" << tc << ": Draw" << endl;
		else cout << "Case #" << tc << ": Game has not completed" << endl;
	}
	return 0;
}
