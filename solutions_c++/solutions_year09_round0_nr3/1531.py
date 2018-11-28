#include <iostream>
#include <cctype>
#include <string>

using namespace std;

int CNT [20][501];
int N;
int main () {
	cin >> N;
	cin.ignore(80, '\n');
	for (int x = 0; x < N; ++x) {
		string L;
		getline(cin, L);
		memset (CNT, 0, sizeof (CNT));
		CNT [0][0] = 1;
		for (int i = 0; i < L.length(); ++i) {
			for (int j = 0; j <= 19; ++j) CNT [j][i+1] = CNT [j][i] % 10000;
			switch (L [i]) {
/*
welcome to code jam
*/
				case 'w':
					CNT [1][i+1] += CNT [0][i];
					break;
				case 'e':
					CNT [2][i+1] += CNT [1][i];
					CNT [7][i+1] += CNT [6][i];
					CNT [15][i+1] += CNT [14][i];
					break;
				case 'l':
					CNT [3][i+1] += CNT [2][i];
					break;
				case 'c':
					CNT [4][i+1] += CNT [3][i];
					CNT [12][i+1] += CNT [11][i];
					break;
				case 'o':
					CNT [5][i+1] += CNT [4][i];
					CNT [10][i+1] += CNT [9][i];
					CNT [13][i+1] += CNT [12][i];
					break;
				case 'm':
					CNT [6][i+1] += CNT [5][i];
					CNT [19][i+1] += CNT [18][i];
					break;
				case ' ':
					CNT [8][i+1] += CNT [7][i];
					CNT [11][i+1] += CNT [10][i];
					CNT [16][i+1] += CNT [15][i];
					break;
				case 't':
					CNT [9][i+1] += CNT [8][i];
					break;
				case 'd':
					CNT [14][i+1] += CNT [13][i];
					break;
				case 'j':
					CNT [17][i+1] += CNT [16][i];
					break;
				case 'a':
					CNT [18][i+1] += CNT [17][i];
					break;
			}
/*			
			for (int j = 0; j < 19; ++j) cout << CNT [j][i+1] << " ";
			cout << endl;
*/
		}
		CNT [19][L.length()] %= 10000;
		cout << "Case #" << x + 1 << ": ";
		string out = "    ";
		for (int i = 0; i < 4; ++i) {
			out [3 - i] = CNT [19][L.length()] % 10 + '0';
			CNT [19][L.length()] /= 10;
		}
		cout << out << endl;
	}	
}
