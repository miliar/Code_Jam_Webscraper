#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <map>

using namespace std;

bool compare(char c1, char c2)
{
	return c1 == '.' && c2 != '.';
}

void update(char c, char &last, map<char, int> &len, map<char, bool> &wins, int K)
{
	if (c != last)
	{
		len[c] = 0;
		last = c;
	}
	len[last]++;
	if (len[last] == K)
		wins[last] = true;
}

int main()
{
	ifstream inFile("A-large.in");
	ofstream outFile("A-large.out");

	int T;
	inFile >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int N, K;
		inFile >> N >> K;
		vector<string> m(N);

		for (int i = 0; i < N; i++)
		{
			inFile >> m[i];
			stable_sort(m[i].begin(), m[i].end(), ptr_fun(compare));
		}

		map<char, int> len;
		map<char, bool> wins;
		char last;

		for (int i = 0; i < N; i++)
		{
			last = '.';
			for (int j = 0; j < N; j++)
				update(m[i][j], last, len, wins, K);
		}

		for (int i = 0; i < N; i++)
		{
			last = '.';
			for (int j = 0; j < N; j++)
				update(m[j][i], last, len, wins, K);
		}

		for (int l = -N + 1; l < N; l++)
		{
			last = '.';
			for (int i = 0; i < N; i++)
			{
				int j = i + l;
				if (j >= 0 && j < N)
					update(m[i][j], last, len, wins, K);
			}
		}

		for (int l = -N + 1; l < N; l++)
		{
			last = '.';
			for (int i = 0; i < N; i++)
			{
				int j = N - 1 -i + l;
				if (j >= 0 && j < N)
					update(m[i][j], last, len, wins, K);
			}
		}

		outFile << "Case #" << nTestCase << ": ";
		if (wins['R'] && wins['B'])
			outFile << "Both";
		else if (wins['R'])
			outFile << "Red";
		else if (wins['B'])
			outFile << "Blue";
		else
			outFile << "Neither";
		outFile << endl;
	}

	return 0;
}
