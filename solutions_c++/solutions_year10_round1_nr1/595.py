#include <fstream>
#include <algorithm>
using namespace std;

int T, K, N;
char data[50][51];

int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");

	cin >> T;
	
	for (int t = 1; t <= T; ++t)
	{
		cin >> N >> K;
		for (int i = 0; i != N; ++i)
			for (int j = 0; j != N; ++j)
				cin >> data[i][j];
		for (int i = 0; i != N; ++i)
			data[i][N] = 'N';
		for (int i = 0; i != N; ++i)
			for (int j = N - 1; j >= 0; --j)
				if (data[i][j] != '.')
				{
					for (int k = j; data[i][k + 1] == '.'; ++k)
						swap(data[i][k], data[i][k + 1]);
				}
		bool red = false, blue = false;
		for (int i = 0; i != N; ++i)
			for (int j = 0; j != N; ++j)
			{
				bool found = true;
				for (int k = 0; k != K; ++k)
					if (i + k == N || data[i + k][j] != data[i][j])
					{
						found = false;
						break;
					}
				if (found)
				{
					if (data[i][j] == 'R')
						red = true;
					else if (data[i][j] == 'B')
						blue = true;
				}

				found = true;
				for (int k = 0; k != K; ++k)
					if (j + k == N || data[i][j + k] != data[i][j])
					{
						found = false;
						break;
					}
				if (found)
				{
					if (data[i][j] == 'R')
						red = true;
					else if (data[i][j] == 'B')
						blue = true;
				}

				found = true;
				for (int k = 0; k != K; ++k)
					if (i + k == N || j + k == N || data[i + k][j + k] != data[i][j])
					{
						found = false;
						break;
					}
				if (found)
				{
					if (data[i][j] == 'R')
						red = true;
					else if (data[i][j] == 'B')
						blue = true;
				}

				found = true;
				for (int k = 0; k != K; ++k)
					if (i + k == N || j - k == -1 || data[i + k][j - k] != data[i][j])
					{
						found = false;
						break;
					}
				if (found)
				{
					if (data[i][j] == 'R')
						red = true;
					else if (data[i][j] == 'B')
						blue = true;
				}
			}
		if (red && blue)
			cout << "Case #" << t << ": Both" << endl;
		else if (red && !blue)
			cout << "Case #" << t << ": Red" << endl;
		else if (!red && blue)
			cout << "Case #" << t << ": Blue" << endl;
		else
			cout << "Case #" << t << ": Neither" << endl;
	}

	return 0;
}