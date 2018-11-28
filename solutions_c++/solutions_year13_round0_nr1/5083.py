#include<cstdio>
#include<iostream>
using std::cin;
using std::cout;
using std::endl;

char gp[10][10];
int xi[4] = {0, 1, 1, -1};
int yi[4] = {1, 0, 1, 1};

int check() {
	for (int i = 0;i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				int a = 0, b = 0, cnt = 0;
				int x = i, y = j;
				if (gp[x][y] == '.')
					a = 1,b = 1;
				if (gp[x][y] == 'X')
					a = 1;
				if (gp[x][y] == 'O')
					b = 1;
				while (cnt < 3) {
					x += xi[k], y += yi[k];
					if (x < 0 || y < 0|| x >3 || y > 3)
						break;
					if (gp[x][y] == '.')
						a = 1,b = 1;
					if (gp[x][y] == 'X')
						a = 1;
					if (gp[x][y] == 'O')
						b = 1;
					cnt++;
				}
				if (cnt == 3 && ((a^b) == 1)) {
					if(a == 1)
						return 1;
					else
						return 2;
				}
			}
		}
	}
	return 0;
}
int main () {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin >> T;
	for(int cas = 1; cas <= T; cas++) {
		for(int i = 0; i < 4; i++)
			cin >> gp[i];
		gets(gp[5]);
		int flag = 0;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++)
				if(gp[i][j] == '.')
					flag = 1;
		}
		cout << "Case #" << cas << ": ";
		int ans = check();
		if(ans) {
			if (ans > 1)
				cout << "O won" << endl;
			else
				cout << "X won" << endl;
		} else {
			if (flag)
				cout << "Game has not completed" << endl;
			else
				cout << "Draw" << endl;
		}
	}
	return 0;
}
