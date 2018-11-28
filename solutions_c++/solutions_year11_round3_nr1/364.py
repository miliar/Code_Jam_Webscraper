// Paste me into the FileEdit configuration dialog

#include <cmath>
#include <ctime>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
char a[100][100];
int main(int argc, char *argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	for (int t = 1; t<=tt; ++t)
	{
		int n, r, c;
		cin >> r >> c;
		
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
			{
				cin >> a[i][j];
			}
		for (int i = 0; i < r-1; ++i)
			for (int j = 0; j < c-1; ++j)
				if (a[i][j] == '#' && a[i][j+1]=='#' && a[i+1][j] == '#' && a[i+1][j+1]=='#')
				{
					a[i][j]='/';
					a[i][j+1]='\\';
					a[i+1][j]='\\';
					a[i+1][j+1]='/';
				}
		bool ans = true;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (a[i][j] == '#')
					ans = false;

						

		cout << "Case #" << t << ": " << endl;
		if (ans)
		{
			for (int i = 0; i < r; ++i)
			{
				for (int j = 0; j < c; ++j)
					cout << a[i][j];
				cout << endl;
			}
		}
		else {
			cout << "Impossible";
			cout << endl;
		}
		
	}
	fclose(stdout);
}
