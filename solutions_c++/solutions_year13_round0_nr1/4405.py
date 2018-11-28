#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;

typedef long long li;

char a[10][10];
int ans[300];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	//cout.setf(ios::fixed);
	//cout.precision(6);
	int t;
	cin >> t;
	int i, j, z;
	for(z = 0; z < t; z++){
		int k = 0;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++){
				cin >> a[i][j];
				if(a[i][j] == '.') k++;
			}
		bool fl = 0;


		for(i = 0; i < 4; i++){
			memset(ans, 0, sizeof(ans));
			for(j = 0; j < 4; j++)
				ans[a[i][j]]++;
			if(ans['O'] == 4 || (ans['O'] == 3 && ans['T'] == 1)){
				cout << "Case #" << z + 1 << ": " << "O won" << "\n";
				fl = 1;
				break;
			}
			if(ans['X'] == 4 || (ans['X'] == 3 && ans['T'] == 1)){
				cout << "Case #" << z + 1 << ": " << "X won" << "\n";
				fl = 1;
				break;
			}
		}
		if(fl == 1)
			continue;


		for(j = 0; j < 4; j++){
			memset(ans, 0, sizeof(ans));
			for(i = 0; i < 4; i++)
				ans[a[i][j]]++;
			if(ans['O'] == 4 || (ans['O'] == 3 && ans['T'] == 1)){
				cout << "Case #" << z + 1 << ": " << "O won" << "\n";
				fl = 1;
				break;
			}
			if(ans['X'] == 4 || (ans['X'] == 3 && ans['T'] == 1)){
				cout << "Case #" << z + 1 << ": " << "X won" << "\n";
				fl = 1;
				break;
			}
		}
		if(fl == 1)
			continue;


		memset(ans, 0, sizeof(ans));
		for(i = 0; i < 4; i++)
			ans[a[i][i]]++;
		if(ans['O'] == 4 || (ans['O'] == 3 && ans['T'] == 1)){
			cout << "Case #" << z + 1 << ": " << "O won" << "\n";
			fl = 1;
		}
		if(ans['X'] == 4 || (ans['X'] == 3 && ans['T'] == 1)){
			cout << "Case #" << z + 1 << ": " << "X won" << "\n";
			fl = 1;
		}
		if(fl == 1)
			continue;


		memset(ans, 0, sizeof(ans));
		for(i = 0; i < 4; i++)
			ans[a[i][3 - i]]++;
		if(ans['O'] == 4 || (ans['O'] == 3 && ans['T'] == 1)){
			cout << "Case #" << z + 1 << ": " << "O won" << "\n";
			fl = 1;
		}
		if(ans['X'] == 4 || (ans['X'] == 3 && ans['T'] == 1)){
			cout << "Case #" << z + 1 << ": " << "X won" << "\n";
			fl = 1;
		}
		if(fl == 1)
			continue;


		if(k == 0){
			cout << "Case #" << z + 1 << ": " << "Draw" << "\n"; 
		}
		else
			cout << "Case #" << z + 1 << ": " << "Game has not completed" << "\n";
	}
	return 0;
}
/*
4 5 1 4 3 100
1 2
1 3
2 3
2 4
3 4
*/