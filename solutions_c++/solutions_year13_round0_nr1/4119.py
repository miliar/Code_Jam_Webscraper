#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <sstream>

using namespace std;


int main() {
	int t;
	cin >> t;
	char arrO[4][4];
	char arrX[4][4];
	char arr[4][4];
	int c = 1;
	while (t--) {
		for (int i = 0; i < 4; i++){
			string s;
			cin >> s;
			for (int j = 0; j < 4; j++){
				arr[i][j] = s[j];
			}
		}
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				arrX[i][j] = arr[i][j] == 'T'? 'X' : arr[i][j];
				arrO[i][j] = arr[i][j] == 'T'? 'O' : arr[i][j];
			}
		}
		bool flag = false;
		for (int i = 0; i < 4 && !flag; i++){
			for (int j = 0;  arrX[i][j] == 'X'; j++)
				if (j == 3){
					flag = true;
					break;
				}
		}
		for (int i = 0; i < 4 && !flag; i++){
			for (int j = 0;  arrX[j][i] == 'X'; j++)
				if (j == 3){
					flag = true;
					break;
				}
		}
		for (int i = 0; arrX[i][i] == 'X' && !flag; i++)
			if (i == 3){
				flag = true;
				break;
		}
		for (int i = 0; arrX[i][3 - i] == 'X' && !flag; i++)
			if (i == 3){
				flag = true;
				break;
		}
		if (flag)
			cout << "Case #" << c << ": " << "X won" << endl;
		else {
			for (int i = 0; i < 4 && !flag; i++){
				for (int j = 0;  arrO[i][j] == 'O'; j++)
					if (j == 3){
						flag = true;
						break;
					}
		}
		for (int i = 0; i < 4 && !flag; i++){
			for (int j = 0;  arrO[j][i] == 'O'; j++)
				if (j == 3){
					flag = true;
					break;
				}
		}
		for (int i = 0; arrO[i][i] == 'O' && !flag; i++)
			if (i == 3){
				flag = true;
				break;
		}
		for (int i = 0; arrO[i][3 - i] == 'O' && !flag; i++)
			if (i == 3){
				flag = true;
				break;
			}
		
			if (flag)
				cout << "Case #" << c << ": " << "O won" << endl;
			else {
				for (int i = 0; i < 4; i++)
					for(int j = 0; j < 4; j++)
						if (arr[i][j] == '.')
							flag = true;
				if (flag)
					cout << "Case #" << c << ": " << "Game has not completed" << endl;
				else 
					cout << "Case #" << c << ": " << "Draw" << endl;
			}
		}
	c++;
	}

}