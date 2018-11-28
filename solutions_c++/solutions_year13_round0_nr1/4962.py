#include <fstream>
using namespace std;

int check(char a, char b, char c, char d)
{
	if (a == 'X' || a == 'T')
	if (b == 'X' || b == 'T')
	if (c == 'X' || c == 'T')
	if (d == 'X' || d == 'T')
		return 1;
	if (a == 'O' || a == 'T')
	if (b == 'O' || b == 'T')
	if (c == 'O' || c == 'T')
	if (d == 'O' || d == 'T')
		return 2;
	return 0;
}

int main()
{
	ifstream fin ("A-large.in");
	ofstream fout ("a.out");

	string output[4] = {"Draw", "X won", "O won", "Game has not completed"};
	int n;
	fin >> n;
	char a[4][4];
	for (int i = 1; i <= n; ++i) {
		bool comp = true;
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				fin >> a[j][k];
				if (a[j][k] == '.')
					comp = false;
			}
		}
		int res = 0;
		for (int j = 0; j < 4 && !res; ++j)
			res = check(a[j][0], a[j][1], a[j][2], a[j][3]);
		for (int j = 0; j < 4 && !res; ++j)
			res = check(a[0][j], a[1][j], a[2][j], a[3][j]);
		if (!res)
			res = check(a[0][0], a[1][1], a[2][2], a[3][3]);
		if (!res)
			res = check(a[0][3], a[1][2], a[2][1], a[3][0]);

		fout << "Case #" << i << ": ";
		if (res) fout << output[res];
		else if (comp) fout << output[0];
		else fout << output[3];
		fout << '\n';
	}
	return 0;
}
