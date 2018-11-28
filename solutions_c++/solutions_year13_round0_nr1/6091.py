#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

char a[4][4];
int T;
ofstream ofile ("example.txt");
// 'X' , 'O', 'f'
char issame(char t1, char t2, char t3, char t4) {
	if (t1 == 'T') {
		if (t2==t3 && t3==t4 && t4==t2 && t2!='.') return t2;
	} else if (t2 == 'T') {
		if (t1==t3 && t3==t4 && t4==t1 && t1!='.') return t1;
	} else if (t3 == 'T') {
		if (t1==t2 && t2==t4 && t4==t1 && t2!='.') return t1;
	} else if (t4 == 'T') {
		if (t1==t2 && t2==t3 &&t3==t1 && t2!='.') return t1;
	} else {
		if (t1==t2 && t2==t3 && t3==t4 && t1==t4 && t2!='.') return t1;
	}
	return 'f';
}

char solve1() {
	char t = ' ';
	for (int i=0; i<4; i++) {
		t = issame(a[i][0],a[i][1],a[i][2],a[i][3]);
		if (t!='f') return t;
		t = issame(a[0][i],a[1][i],a[2][i],a[3][i]);
		if (t!='f') return t;
	}
	t = issame(a[0][0],a[1][1],a[2][2],a[3][3]);
	if (t!='f') return t;
	t = issame(a[3][0],a[2][1],a[1][2],a[0][3]);
	if (t!='f') return t;
	// draw case
	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			if (a[i][j] == '.') return t;
		}
	}
	return 'd';
}

void solve() {
	char t = solve1();
	if (t == 'f') {
		cout << "Game has not completed" << endl;
	} else if (t == 'd') {
		cout << "Draw" << endl;
	} else cout << t << " won" << endl;
}
void OPEN() {
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
}
int main() {
	OPEN();
	cin >> T;
	for (int i=0; i<T; i++) {
		char tmp = ' ';
		for (int u=0; u<4; u++)
			for (int v=0; v<4; v++)
				{
					tmp = ' ';
					while (tmp!='X' && tmp!='O' && tmp!='.' && tmp!='T') cin >> tmp;
					a[u][v] = tmp;
				}		
		cout << "Case #" << i+1 << ": ";
		solve();
	}
	
	return 0;
}