#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <iostream>
#include <sstream>
#include <string>

#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>

#define foreach(iName, iBegin, iEnd) for (auto iName = (iBegin); iName != (iEnd); ++iName)

#define forever for (;;)

#define loop(counterName, times) for (decltype(times) counterName = 0; counterName < (times); ++counterName)

#if defined(_MSC_VER) && _MSC_VER >= 1600
#	define null __nullptr
#else
#	define null 0
#endif

using namespace std;

int N, K;
char board[50][50];

bool count(char c)
{
	loop (i, N)
	{
		loop (j, N)
		{
			// find to the right
			{
				bool found = true;
				int len = 0;
				for (int col = j; col < N && board[i][col] == c; ++col)
					++len;

				if (len >= K)
					return true;
			}

			// find to the bottom
			{
				bool found = true;
				int len = 0;
				for (int row = i; row < N && board[row][j] == c; ++row)
					++len;

				if (len >= K)
					return true;
			}

			// find 'backslash' side
			{
				bool found = true;
				int len = 0;
				for (int offset = 0; (i + offset < N && j + offset < N) && board[i + offset][j + offset] == c; ++offset)
					++len;

				if (len >= K)
					return true;
			}
			// find / side
			{
				int len = 0;
				for (int offset = 0; (i + offset < N && j - offset >= 0) && board[i + offset][j - offset] == c; ++offset)
					++len;

				if (len >= K)
					return true;
			}
		}
	}

	return false;
}

int main()
{
	int numCase;
	cin >> numCase;

	for (int caseCounter = 1; caseCounter <= numCase; ++caseCounter)
	{
		cin >> N >> K;

		loop (i, N)
		{
			string str;
			cin >> str;
			std::memcpy(board[i], str.c_str(), N);

			// shift each row to right
			int firstLetter = str.find_first_not_of('.');
			if (firstLetter == str.npos)
				continue;
			int firstDot = str.find_first_of('.', firstLetter);
			if (firstDot == str.npos)
				continue;

			for (int j = firstDot; j < N; ++j)
			{
				while (board[i][j] == '.')
				{
					std::memmove(board[i] + 1, board[i], j);
					board[i][0] = '.';
				}
			}
		}

		bool r = count('R');
		bool b = count('B');

		string output;
		if (r && b)
			output = "Both";
		else if (r)
			output = "Red";
		else if (b)
			output = "Blue";
		else
			output = "Neither";

		cout << "Case #" << caseCounter << ": " << output << endl;
	}

	return 0;
}
