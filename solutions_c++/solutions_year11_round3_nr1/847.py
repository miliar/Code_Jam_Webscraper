
#include <iostream>

using namespace std;

void DoCase ()
{
	char tiles [51][51];
	int R; cin >> R;
	int C; cin >> C;
	for (int r = 0; r < R; ++r)
		for (int c = 0; c < C; ++c)
			cin >> tiles [r][c];
	for (int r = 0; r < R; ++r)
		tiles [r][C] = 'X';
	for (int c = 0; c < C; ++c)
		tiles [R][c] = 'X';
	tiles [R][C] = 'X';
	bool failure = false;
	for (int r = 0; r < R; ++r)
		for (int c = 0; c < C; ++c)
			if (tiles [r][c] == '#') {
				if (tiles [r][c+1] == '#' && tiles [r+1][c+1] == '#' && tiles [r+1][c] == '#') {
					tiles [r][c] = '/';
					tiles [r+1][c] = '\\';
					tiles [r+1][c+1] = '/';
					tiles [r][c+1] = '\\';
				}
				else failure = true;
			}
	if (failure)
		cout << "Impossible" << endl;
	else
		for (int r = 0; r < R; ++r) {
			for (int c = 0; c < C; ++c)
				cout << tiles [r][c];
			cout << endl;
		}
}

main ()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		cout << "Case #" << i << ":" << endl;
		DoCase ();
	}
}
