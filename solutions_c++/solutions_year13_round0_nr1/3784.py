#include <iostream>
#include <cstdio>
using namespace std;
char in[5][5],O[5][5],X[5][5];
bool check(char a[][5],char x) {
	bool D1(true),D2(true),R,C;
	for(int i(0);i!=4;++i) {
		R = C = true;
		for(int j(0);j!=4;++j) {
			R&=(a[i][j]==x);
			C&=(a[j][i]==x);
		}
		if(R || C) return true;
		D1&=(a[i][i]==x);
		D2&=(a[i][3-i]==x);
	}
	return D1 || D2;
}
bool full() {
	for(int i(0);i!=4;++i)
		for(int j(0);j!=4;++j)
			if(in[i][j]=='.')
				return false;
	return true;
}
int main() {
	int _,ca(0); cin>>_;
	while(_--) {
		for(int i(0);i!=4;++i)
			cin>>in[i];
		for(int i(0);i!=4;++i)
			for(int j(0);j!=4;++j) {
				if(in[i][j]!='T')
					O[i][j] = X[i][j] = in[i][j];
				else O[i][j] = 'O', X[i][j] = 'X';
			}
		printf("Case #%d: ",++ca);
		if(check(O,'O')) puts("O won");
		else if(check(X,'X')) puts("X won");
		else if(full()) puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}
