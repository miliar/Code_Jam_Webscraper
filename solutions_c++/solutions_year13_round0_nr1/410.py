#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
using namespace std;

string s[4];
int check(int bx, int by, int c1, int c2){
		char bfr = ',';
		int m = 0;
		while(bx > -1 && by > -1 && bx < 4 && by < 4){
				if(s[bx][by] == bfr)
					m++;
				else if(s[bx][by] == 'T')
					m ++;
				else if(bfr != '.' && m > 3){
					if(bfr == 'X')
						return 1;
					else
						return 2;
				}else{
					bfr = s[bx][by];
					m = 1;
					if(bfr == 'T'){
						bfr = 'X';
					}
				}
				bx += c1;
				by += c2;
		}
		if(bfr != '.' && m > 3){
					if(bfr == 'X')
						return 1;
					else
						return 2;
		}
		return 0;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A2.out", "w", stdout);
	int n;
	cin >> n;
	int d[8][2] = {{-1, 1}, {1, -1}, {1, 1}, {-1, -1}, {1, 0}, {0, 1}, {-1, 0}, {0, -1}};
	for(int i = 0; i < n; i++){
		int m = 0;
		for(int i = 0; i < 4; i++){
			cin >> s[i];
			for(int j = 0; j < 4; j++)
				if(s[i][j] != '.')
					m++;
		}
		int t = 0;

		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 8; j++){
				int k = check(i, 0, d[j][0], d[j][1]);
				if(k)
					t = k;
				k = check(i, 3, d[j][0], d[j][1]);
				if(k)
					t = k;
				k = check(0, i, d[j][0], d[j][1]);
				if(k)
					t = k;
				k = check(3, i, d[j][0], d[j][1]);
				if(k)
					t = k;
			}
		}
		cout << "Case #" << i + 1 << ": ";

		if(t)
			cout << ((t == 1) ? "X won" : "O won") << endl;
		else if(m == 16)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}
	return 0;
}
