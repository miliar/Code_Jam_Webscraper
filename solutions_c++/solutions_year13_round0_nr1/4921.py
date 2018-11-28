#include <iostream>
#include <cstring>
using namespace std;

string s[4];
bool find(char x)
{
	for (int i = 0; i < 4; ++i) {
		bool flag = true;
		for (int j = 0; j < 4; ++j)
			flag &= s[i][j] == x || s[i][j] == 'T';
		if (flag) return true;
		flag = true;
		for (int j = 0; j < 4; ++j)
			flag &= s[j][i] == x || s[j][i] == 'T';
		if (flag) return true;
		flag = true;		
		for (int j = 0; j < 4; ++j)
			flag &= s[j][j] == x || s[j][j] == 'T';
		if (flag) return true;
		flag = true;		
		for (int j = 0; j < 4; ++j)
			flag &= s[j][3 - j] == x || s[j][3 - j] == 'T';
		if (flag) return true;
		flag = true;				
	}
	return false;
}
int main()
{
	int cases;
	cin >> cases;
	for (int tcase = 1; tcase <= cases; ++tcase) {
		cout << "Case #" << tcase << ": ";
		for (int i = 0; i < 4; ++i)
			cin >> s[i];
		if (find('O')) cout << "O won" << endl;
		else if (find('X')) cout << "X won" << endl;
		else {
			bool k = false;
			for (int i = 0; i < 4; ++i)
				for (int j = 0; j < 4; ++j)
					if (s[i][j] == '.') k = true;
			if (k) cout << "Game has not completed" << endl;
			else cout << "Draw" << endl;
		}
	}
	return 0;
}
