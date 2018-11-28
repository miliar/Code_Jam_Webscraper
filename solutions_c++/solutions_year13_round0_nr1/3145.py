#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

bool haswon(bool b[4][4]) {
	for (int i=0;i<4;++i) {
		bool th=true;
		bool tv = true;
		for (int j=0;j<4;++j) {
			th = th & b[i][j];
			tv = tv & b[j][i];
		}
		if (th|tv) {
			return true;
		}
	}	
	bool td1 = true;
	bool td2 = true;
	for (int i=0;i<4;++i){
		td1 = td1 & b[i][i];
		td2 = td2 & b[3-i][i];
	}
	return (td1|td2);
}

int main(void) {
	int T;
	cin>>T;
	bool bx[4][4];
	bool by[4][4];
	for (int i=0;i<T;++i){
		string s;
		bool complete = true;
		for (int j=0;j<4;++j) {
			cin>>s;
			for (int k=0;k<4;++k) {
				char c = s[k];
				if (c=='X') {
					bx[j][k] = true;
					by[j][k] = false;
				} else if (c=='O') {
					bx[j][k] = false;
					by[j][k] = true;
				} else if (c=='T') {
					bx[j][k] = true;
					by[j][k] = true;
				} else if (c=='.') {
					bx[j][k] = false;
					by[j][k] = false;
					complete = false;
				}
			}
		}
		bool xwon = haswon(bx);
		bool ywon = haswon(by);
		cout << "Case #"<<i+1<<": ";
		if (xwon) {
			cout<< "X won\n";
		} else if (ywon) {
			cout << "O won\n";
		} else if (complete) {
			cout << "Draw\n";
		} else {
			cout << "Game has not completed\n";
		}
	}// end test i
}