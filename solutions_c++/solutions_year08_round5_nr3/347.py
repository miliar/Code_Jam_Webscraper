#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int T, M, N;
vector<string> seats;
vector<int> num;
vector<bool> ok;
int maxcap[10][1024];

void recalculate(int r)
{
	for (int i = 1; i < (1 << N); i++)
		for (int j = 0; j < N; j++)
			if ((i & (1 << j)) > 0 && maxcap[r][i - (1 << j)] > maxcap[r][i])
				maxcap[r][i] = maxcap[r][i - (1 << j)];
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("C-small.in");
	output.open("C-small.out");

	ok.resize(1024);
	for (int i = 0; i < 1024; i++)
	{
		ok[i] = true;
		for (int j = 0; j < 9; j++)
			if ((i & (1 << j)) > 0 && (i & (1 << (j + 1))) > 0)
				ok[i] = false;
	}

	num.resize(1024);
	for (int i = 0; i < 1024; i++)
	{
		num[i] = 0;
		for (int j = 0; j < 10; j++)
			if ((i & (1 << j)) > 0)
				num[i]++;
	}

	input >> T;
	for (int c = 0; c < T; c++)
	{
		input >> M >> N;

		seats.resize(M);
		for (int i = 0; i < M; i++) input >> seats[i];

		vector<int> extreme(M);
		for (int i = 0; i < M; i++)
		{
			extreme[i] = 0;
			for (int j = 0; j < N; j++)
				if (seats[i][j] == '.')
					extreme[i] += (1 << j);
		}

		for (int i = 0; i < (1 << N); i++)
			if ((i & extreme[0]) == i && ok[i])
				maxcap[0][i] = num[i];
		recalculate(0);

		for (int i = 1; i < M; i++)
		{
			for (int j = 0; j < (1 << N); j++)
			{
				maxcap[i][j] = 0;
				if ((j & extreme[i]) == j && ok[j])
				{
					int last = extreme[i-1];
					for (int k = 0; k < N; k++)
						if ((last & (1 << k)) > 0 && ((k > 0 && (j & (1 << (k - 1))) > 0) || (k < N - 1 && (j & (1 << (k + 1))) > 0)))
							last -= (1 << k);
					if (maxcap[i-1][last] + num[j] > maxcap[i][j])
						maxcap[i][j] = maxcap[i-1][last] + num[j];
				}
			}
			recalculate(i);
		}

		output << "Case #" << c + 1 << ": " << maxcap[M-1][extreme[M-1]] << endl;
	}

	input.close();
	output.close();
}
