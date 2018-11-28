#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::string;
int main()
{
	long t;
	string line;
	int unfinished,xwon,owon;
	int a[2][10];
	cin >> t;
	for (int i=1; i<=t; ++i) {
		unfinished=0;
		xwon=0;
		owon=0;
		for (int j=0; j<=1; ++j) {
			for (int k=0; k<=9; ++k) {
				a[j][k]=0;
			}
		}
		for (int j=0; j<=3; ++j) {
			cin >> line;
			for (int k=0; k<=3; ++k) {
				if (line[k]=='.') {
					unfinished=1;
				} else {
					if (line[k]!='X') {
						++a[1][j];
						++a[1][4+k];
						if (a[1][j]==4) {
							owon=1;
						}
						if (a[1][4+k]==4) {
							owon=1;
						}
						if (j==k) {
							++a[1][8];
							if (a[1][8]==4) {
								owon=1;
							}
						}
						if (j+k==3) {
							++a[1][9];
							if (a[1][9]==4) {
								owon=1;
							}
						}
					}
					if (line[k]!='O') {
						++a[0][j];
						++a[0][4+k];
						if (a[0][j]==4) {
							xwon=1;
						}
						if (a[0][4+k]==4) {
							xwon=1;
						}
						if (j==k) {
							++a[0][8];
							if (a[0][8]==4) {
								xwon=1;
							}
						}
						if (j+k==3) {
							++a[0][9];
							if (a[0][9]==4) {
								xwon=1;
							}
						}
					}
				}
			}
		}
		if (xwon==1) {
			cout << "Case #" << i << ": X won" << endl;
		} else {
			if (owon==1) {
				cout << "Case #" << i << ": O won" << endl;
			} else {
				if (unfinished==1) {
					cout << "Case #" << i << ": Game has not completed" << endl;
				} else {
					cout << "Case #" << i << ": Draw" << endl;
				}
			}
		}
	}
	return 0;
}	
