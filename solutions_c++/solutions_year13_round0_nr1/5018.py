#include <iostream>
#include <string>
#include <cassert>

using namespace std;

enum Cell { Empty = 0, X, O, T };

int main()
{
	int N;
	cin >> N;

	Cell m[4][4];

	for (int nTestCase = 1; nTestCase <= N; nTestCase++)
	{
		cin.get();
		for (int i = 0; i < 4; i++)
		{
			string line;
			getline(cin, line);

			for (int c = 0; c < 4; c++)
				switch (line[c])
				{
					case '.':
						m[i][c] = Empty;
						break;
					case 'O':
						m[i][c] = O;
						break;
					case 'X':
						m[i][c] = X;
						break;
					case 'T':
						m[i][c] = T;
						break;
					default:
						assert(false);
						break;
				}
		}

		bool complete = true;
		int count[] = {0, 0, 0, 0};

		auto evaluate = [&complete, &count]() {
			if (count[Empty])
				complete = false;
			if (count[O] == 4 || (count[O] == 3 && count[T] == 1))
				return O;
			if (count[X] == 4 || (count[X] == 3 && count[T] == 1))
				return X;
			return Empty;
		};

		Cell winner = Empty;

		for (int r = 0; r < 4 && winner == Empty; r++)
		{
			memset(count, 0, sizeof(count));
			for (int c = 0; c < 4; c++)
				count[m[r][c]]++;
			winner = evaluate();
		}
		for (int r = 0; r < 4 && winner == Empty; r++)
		{
			memset(count, 0, sizeof(count));
			for (int c = 0; c < 4; c++)
				count[m[c][r]]++;
			winner = evaluate();
		}
		
		if (winner == Empty)
		{
			memset(count, 0, sizeof(count));
			for (int r = 0, c = 0; r < 4 && c < 4; r++, c++)
				count[m[c][r]]++;
			winner = evaluate();
		}

		if (winner == Empty)
		{
			memset(count, 0, sizeof(count));
			for (int r = 0, c = 3; r < 4 && c >= 0; r++, c--)
				count[m[c][r]]++;
			winner = evaluate();
		}

		cout << "Case #" << nTestCase << ": ";
		switch (winner)
		{
		case Empty:
			if (complete)
				cout << "Draw";
			else
				cout << "Game has not completed";
			break;
		case X:
			cout << "X won";
			break;
		case O:
			cout << "O won";
			break;
		default:
			assert(false);
			break;
		}

		cout << endl;
	}
}
