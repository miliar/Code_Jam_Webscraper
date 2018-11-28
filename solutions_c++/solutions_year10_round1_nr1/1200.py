
#include <iostream>

using namespace std;

void DoCase ()
{
	int N, K;
	cin >> N;
	cin >> K;
	char board [50][50];
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
			cin >> board [j][i];

	for (int row = 0; row < N; ++row) {
		int blanks = 0;
		int col = N-1;
		while (col >= 0) {
			if (board [col][row] == '.')
				++blanks;
			else {
				if (blanks > 0) {
					board [col + blanks][row] = board [col][row];
					board [col][row] = '.';
				}
			}
			--col;
		}
	}

	bool red = false;
	bool blue = false;

	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j) {
			if (i <= N - K) {
				bool redOK = true;
				bool blueOK = true;
				for (int x = 0; x < K; ++x) {
					redOK = redOK && (board [i+x][j] == 'R');
					blueOK = blueOK && (board [i+x][j] == 'B');					
				}
				red = red || redOK;
				blue = blue || blueOK;
			}
			if (j <= N - K) {
				bool redOK = true;
				bool blueOK = true;
				for (int x = 0; x < K; ++x) {
					redOK = redOK && (board [i][j+x] == 'R');
					blueOK = blueOK && (board [i][j+x] == 'B');					
				}
				red = red || redOK;
				blue = blue || blueOK;
			}
			if (j <= N - K && i <= N - K) {
				bool redOK = true;
				bool blueOK = true;
				for (int x = 0; x < K; ++x) {
					redOK = redOK && (board [i+x][j+x] == 'R');
					blueOK = blueOK && (board [i+x][j+x] == 'B');					
				}
				red = red || redOK;
				blue = blue || blueOK;
			}
			if (j <= N - K && i >= N - K) {
				bool redOK = true;
				bool blueOK = true;
				for (int x = 0; x < K; ++x) {
					redOK = redOK && (board [i-x][j+x] == 'R');
					blueOK = blueOK && (board [i-x][j+x] == 'B');					
				}
				red = red || redOK;
				blue = blue || blueOK;
			}
		}
	if (red) {
		if (blue)
			cout << "Both";
		else
			cout << "Red";
	} else {
		if (blue)
			cout << "Blue";
		else
			cout << "Neither";
	}
}

main ()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		cout << "Case #" << i << ": ";
		DoCase ();
		cout << endl;
	}
}
