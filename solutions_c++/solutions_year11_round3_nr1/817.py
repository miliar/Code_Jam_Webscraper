//#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <iomanip>
#include <string>
#include <fstream>
using namespace std;
ifstream cin("A-large.in");
ofstream cout("A-large.out");

//ifstream cin("A-large.in");
//ofstream cout("A-large.out");

bool inrange(int x, int y, int R, int C) {
	return (x>=0 && y>=0 && x<R && y<C);
}

int main() {
int T;
int R,C;
cin >> T;
char B[50][50];
for (int r=1; r<=T; r++) {
	cin >> R >> C;
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			cin >> B[i][j];
		}
	}
	bool thebreak = false;
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			if (B[i][j] == '#') {
				if (inrange(i,j+1,R,C) && inrange(i+1,j,R,C) && inrange(i+1,j+1,R,C) && B[i][j+1] == '#' && B[i+1][j+1] == '#' && B[i+1][j] == '#' ) {
					B[i][j] = '/';
					B[i][j+1]  = '['+1;
					B[i+1][j] = '['+1;
					B[i+1][j+1] = '/';
				}	else {
					thebreak = true;
					break;		
				}
			}
		}
		if (thebreak) break;
	}

	cout << "Case #"<<r<<":"<<endl;
	if (thebreak) 	cout << "Impossible"<<endl;
	else {
		for (int i=0; i<R; i++) {
			for (int j=0; j<C; j++) {
			cout << B[i][j];
			}
		cout << endl;
		}
	}
}
cout << endl;
return 0;
}
