#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const int MAX = 10000;

int T, M, V;
vector<int> value, change;

int main()
{
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("A-large.out");

	input >> T;
	for (int c = 0; c < T; c++)
	{
		input >> M >> V;
		value.resize(M);
		change.resize((M-1)/2);

		for (int i = 0; i < (M-1)/2; i++)
			input >> value[i] >> change[i];
		for (int i = (M-1)/2; i < M; i++)
			input >> value[i];
		
		int ans[MAX][2];
		for (int i = (M-1)/2; i < M; i++)
		{
			ans[i][value[i]] = 0;
			ans[i][1-value[i]] = MAX;
		}
		for (int i = (M-3)/2; i >= 0; i--)
			for (int j = 0; j < 2; j++)
			{
				ans[i][j] = MAX;
				for (int x = 0; x < 2; x++)
					for (int y = 0; y < 2; y++)
						if ((value[i] == 0 && ((x | y) == j)) || (value[i] == 1 && ((x & y) == j)))
						{
							if (ans[2*i+1][x] + ans[2*i+2][y] < ans[i][j])
								ans[i][j] = ans[2*i+1][x] + ans[2*i+2][y];
						}
						else
							if ((change[i] == 1) && ((value[i] == 1 && ((x | y) == j)) || (value[i] == 0 && ((x & y) == j))))
							{
								if (ans[2*i+1][x] + ans[2*i+2][y] + 1 < ans[i][j])
									ans[i][j] = ans[2*i+1][x] + ans[2*i+2][y] + 1;
							}
			}
		
		output << "Case #" << c + 1 << ": ";
		if (ans[0][V] == MAX)
			output << "IMPOSSIBLE" << endl;
		else
			output << ans[0][V] << endl;
	}

	input.close();
	output.close();
}
