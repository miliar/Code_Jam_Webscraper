#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("C:/1.txt", "r", stdin);
	freopen("C:/2.txt", "w", stdout);
	int ttt;
	cin >> ttt;
	for (int go=1;go<=ttt;++go)
	{
		string s[4];
		for (int i = 0; i < 4; ++i) cin >> s[i];
		cout << "Case #" << go << ": ";
		for (int i = 0; i < 4; ++i) {int q=0; for (int j = 0; j < 4; ++j) if (s[i][j]=='X' || s[i][j]=='T') ++q; if (q==4) goto xw;}
		for (int i = 0; i < 4; ++i) {int q=0; for (int j = 0; j < 4; ++j) if (s[j][i]=='X' || s[j][i]=='T') ++q; if (q==4) goto xw;}
		{ int q=0; for (int i = 0; i < 4; ++i) if (s[i][i]=='X' || s[i][i]=='T') ++q; if (q==4) goto xw;}
		{ int q=0; for (int i = 0; i < 4; ++i) if (s[i][3-i]=='X' || s[i][3-i]=='T') ++q; if (q==4) goto xw;}
		for (int i = 0; i < 4; ++i) {int q=0; for (int j = 0; j < 4; ++j) if (s[i][j]=='O' || s[i][j]=='T') ++q; if (q==4) goto ow;}
		for (int i = 0; i < 4; ++i) {int q=0; for (int j = 0; j < 4; ++j) if (s[j][i]=='O' || s[j][i]=='T') ++q; if (q==4) goto ow;}
		{ int q=0; for (int i = 0; i < 4; ++i) if (s[i][i]=='O' || s[i][i]=='T') ++q; if (q==4) goto ow;}
		{ int q=0; for (int i = 0; i < 4; ++i) if (s[i][3-i]=='O' || s[i][3-i]=='T') ++q; if (q==4) goto ow;}
		for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) if (s[i][j]=='.') goto gn; goto dr;
		xw: cout << "X won\n"; goto e; ow: cout << "O won\n"; goto e; dr: cout << "Draw\n"; goto e; gn: cout << "Game has not completed\n";goto e; e: ;
	}
	return 0;
}
