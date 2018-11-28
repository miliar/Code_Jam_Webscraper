// Helloworld : Console application project sample.

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <ios>
using namespace std;
string board[60];

bool check(char s, int m, int l, int n, int k)
{
	int i;
	bool res = false;
	if (l + k <= n){
		for (i = 0; i < k; i++){
			cout << board[m][l+i];
			if (board[m][l+i] != s)
				break;
		}
		cout << " hor " << endl;
		if (i == k)
			res = true;
	}
	if (m + k <= n){
		for (i = 0; i < k; i++){
			cout << board[m+i][l];
			if (board[m+i][l] != s)
				break;
		}
		cout << " ver "<<endl;
		if (i == k)
			res = true;
	}
	if ((m + k <= n) && (l + k < n)){
		for (i = 0; i < k; i++){
			cout << board[m+i][l+i];
			if (board[m+i][l+i] != s)
				break;
		}
		cout << "dia " <<  endl;
		if (i == k)
			res = true;
	}
	if ((m + k <= n) && (l + 1 - k >= 0)){
		for (i = 0; i < k; i++){
			cout << board[m+i][l-i];
			if (board[m+i][l-i] != s)
				break;
		}
		cout << " dia " << endl;
		if (i == k)
			res = true;
	}
	return res;
}
int main()
{
	ifstream fin ("A-small-attempt3.in");
	//ifstream fin ("in.txt");
	ofstream fout ("out.txt");
	int t, i, j;
	int n, k;
	int l, m;
	int win;
	string line;
	fin >> t;
	for (i = 0; i < t; i++){
		fin >> n >> k;
		win = 0;
		fout << "Case #" << i+1 << ": ";
		for (j = 0; j < n; j++){
			fin >> line;
		
			for (m = l = line.length() - 1; l >= 0; l--){
				if (line[l] != '.'){
					line[m] = line[l];
					m--;
				}
			}
			while(m >= 0) line[m--] = '.';
			board[j] = line;
			cout << line << endl;
		}
		for (m = 0; m < n; m++){
			for (l = 0; l < n; l++){
				if (board[m][l] == 'B'){
					if (check('B', m, l, n, k))
						win |= 1;
				}
				if (board[m][l] == 'R'){
					if (check('R', m, l, n, k))
						win |= 2;
				}
			}
		}
		cout << win << endl;
		switch (win){
		case 0:
			fout << "Neither" << endl;
			break;
		case 1:
			fout << "Blue" << endl;
			break;
		case 2:
			fout << "Red" << endl;
			break;
		case 3:
			fout << "Both" << endl;
			break;
		}
	}
	
	return 0;
}
