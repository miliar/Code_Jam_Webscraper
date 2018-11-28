#include <iostream>
using namespace std;

int t;
int h, w;

int deps[500][500];
int flags[500][500];
char names[500][500];


const int dx[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

void mark(int i, int j, char ch)
{
	if (names[i][j] != 0)
		return;
	names[i][j] = ch;
	int ii, jj;
	for (int k = 0; k < 4; ++k) {
		ii = i + dx[k][0];
		jj = j + dx[k][1];
		
		if (deps[ii][jj] == 10000000)
			continue;

		if (flags[ii][jj] == -1)
			continue;

		if (flags[ii][jj] / 500 == i && flags[ii][jj] % 500 == j)
			mark(ii, jj, ch);
	
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int tt = 0; tt < t; ++tt) {
		printf("Case #%d:\n", tt + 1);

		cin >> h >> w;
		for (int i = 0; i <= h + 1; ++i)
			for (int j = 0; j <= w + 1; ++j)
				deps[i][j] = 10000000;

		for (int i = 1; i <= h; ++i)
			for (int j = 1; j <= w; ++j)
				cin >> deps[i][j];
		
		for (int i = 1; i <= h; ++i) 
			for (int j = 1; j <= w; ++j) {
				int tmp = deps[i][j];
				for (int k = 0; k < 4; ++k)
					tmp = min(tmp, deps[i + dx[k][0]][j + dx[k][1]]);
				if (tmp == deps[i][j])
					flags[i][j] = -1;
				else {
					for (int k = 0; k < 4; ++k)
						if (tmp == deps[i + dx[k][0]][j + dx[k][1]]) {
							flags[i][j] = (i + dx[k][0]) * 500 + (j + dx[k][1]);
							break;
						}
				}
			}
					
		for (int i = 1; i <= h; ++i)
			memset(names[i], 0, sizeof(names[i]));

		char ch = 'a';
		for (int i = 1; i <= h; ++i)
			for (int j = 1; j <= w; ++j)
				if (names[i][j] == 0) {
					int ii = i, jj = j;
					while (flags[ii][jj] != -1) {
						int ti = flags[ii][jj] / 500;
						jj = flags[ii][jj] % 500;
						ii = ti;
					}
					mark(ii, jj, ch);

					++ch;
				}
		
		for (int i = 1; i <= h; ++i) {
			cout << names[i][1];
			for (int j = 2; j <= w; ++j)
				cout << " " << names[i][j];
			cout << endl;
		}
			

	}

	return 0;
}