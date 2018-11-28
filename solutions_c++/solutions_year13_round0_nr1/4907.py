/*
*/
#include <iostream>
#include <cstdio>
using namespace std;

char arr[4][4];
int counter[11][3];

void Judge()
{
	for (int i = 0; i < 11; i++)
		for (int j = 0; j < 3; j++)
			counter[i][j] = 0;
	
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			switch(arr[i][j]) {
				case 'X':
					counter[i][0]++;
					counter[4+j][0]++;
					if (i == j)
						counter[8][0]++;
					if ((i+j) == 3)
						counter[9][0]++;
					break;
				case 'O':
					counter[i][1]++;
					counter[4+j][1]++;
					if (i == j)
						counter[8][1]++;
					if ((i+j) == 3)
						counter[9][1]++;
					break;
				case 'T':
					counter[i][2]++;
					counter[4+j][2]++;
					if (i == j)
						counter[8][2]++;
					if ((i+j) == 3)
						counter[9][2]++;
					break;
				case '.':
					counter[10][0]++;
				default:
					break;
			}
		}
	}
	
	for (int i = 0; i < 10; i++) {
		if ( (counter[i][0] == 4) || ( (counter[i][0] == 3) && (counter[i][2] == 1) ) ) {
			cout << "X won" << endl;
			return ;
		}
		if ( (counter[i][1] == 4) || ( (counter[i][1] == 3) && (counter[i][2] == 1) ) ) {
			cout << "O won" << endl;
			return ;
		}
	}


	if (counter[10][0] == 0) 
		cout << "Draw" << endl;
	else
		cout << "Game has not completed" << endl;
	return ;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		for(int m = 0; m < 4; m++)
			for (int n = 0; n < 4; n++) {
				char tmp;
				cin >> tmp;
				arr[m][n] = tmp; 
			}
		cout << "Case #" << i+1 << ": ";
		Judge();
	}
	
	return 0;

}
