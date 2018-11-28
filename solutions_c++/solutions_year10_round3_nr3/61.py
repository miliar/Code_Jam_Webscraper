
#include <iostream>
#include <vector>

using namespace std;

int hex (char c)
{
	return
		c == '0' ? 0 :
		c == '1' ? 1 :
		c == '2' ? 2 :
		c == '3' ? 3 :
		c == '4' ? 4 :
		c == '5' ? 5 :
		c == '6' ? 6 :
		c == '7' ? 7 :
		c == '8' ? 8 :
		c == '9' ? 9 :
		c == 'A' ? 10 :
		c == 'B' ? 11 :
		c == 'C' ? 12 :
		c == 'D' ? 13 :
		c == 'E' ? 14 :
		c == 'F' ? 15 :
		-1;
}

void DoCase ()
{
	int M, N;
	cin >> M;
	cin >> N;

	int board [512][512];
	for (int m = 0; m < M; ++m)
		for (int n = 0; n < N; n += 4) {
			char c;
			cin >> c;
			int c2 = hex (c);
			board [m][n] = (c2 & 0x8) ? 1 : 0;
			board [m][n+1] = (c2 & 0x4) ? 1 : 0;
			board [m][n+2] = (c2 & 0x2) ? 1 : 0;
			board [m][n+3] = (c2 & 0x1) ? 1 : 0;
		}

	for (int i = 0; i < M; ++i)
		for (int j = 0; j < N; ++j)
			if ((i+j) % 2)
				board [i][j] = (board [i][j] + 1) % 2;

	int max = (M > N) ? M : N;

	vector<vector<vector<bool> > > acceptable;
	for (int i = 0; i < M; ++i) {
		acceptable.push_back (vector<vector<bool> > ());
		for (int j = 0; j < N; ++j) {
			acceptable [i].push_back (vector<bool> ());
			for (int k = 0; k < max; ++k)
				acceptable [i][j].push_back (false);
		}
	}


	for (int i = 0; i < M; ++i)
		for (int j = 0; j < N; ++j)
			acceptable [i][j][0] = true;
	for (int i = 0; i < M-1; ++i)
		for (int j = 0; j < N-1; ++j)
			acceptable [i][j][1] = ((board [i][j] == board [i][j+1]) && (board [i][j] == board [i+1][j]) && (board [i][j] == board [i+1][j+1])) ?
					true : false;
		
	for (int k = 2; k < max; ++k)
		for (int i = 0; i < M-k; ++i)
			for (int j = 0; j < N-k; ++j)
				acceptable [i][j][k] = (acceptable [i][j][k-1] && acceptable [i][j+1][k-1] && acceptable [i+1][j][k-1] && acceptable [i+1][j+1][k-1]);

	int result [512];
	for (int x = 0; x < 512; ++x)
		result [x] = 0;

	for (int k = max-1; k >= 0; --k)
		for (int i = 0; i < M-k; ++i)
			for (int j = 0; j < N-k; ++j)
				if (acceptable [i][j][k]) {
					++result [k];
					for (int k2 = k; k2 >= 0; --k2)
						for (int i2 = i - k2; i2 <= i + k; i2++)
							for (int j2 = j - k2; j2 <= j + k; j2++)
								if (i2 >= 0 && j2 >= 0 && i2 <= M-k2 && j2 <= N-k2)
									acceptable [i2][j2][k2] = false;
				}

	int count = 0;
	for (int x = 0; x < 512; ++x)
		if (result [x] > 0)
			++count;

	cout << count << endl;
	for (int x = 511; x >= 0; --x)
		if (result [x] > 0)
			cout << x+1 << ' ' << result [x] << endl;			
}

main ()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		cout << "Case #" << i << ": ";
		DoCase ();
	}
}
