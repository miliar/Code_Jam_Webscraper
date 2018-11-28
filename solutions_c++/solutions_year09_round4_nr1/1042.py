#include<iostream>
#include<string>

using namespace std;

int matrix[40][40], temp[40];

int main()
{
	int T;
	cin >> T;

	for(int X = 1; X <= T; ++X)
	{
		int N;
		cin >> N;

		string line;

		for(int i=0; i < N; ++i)
		{
			cin >> line;

			for(int j=0; j < N; ++j)
				matrix[i][j] = (line[j] == '1' ? 1 : 0);
		}

		int swaps = 0;

		for(int i=0; i < N; ++i)
			for(int j=i+1; j < N; ++j)
				if(matrix[i][j] == 1)
				{
					for(int k=i+1; k < N; ++k)
					{
						bool found = true;

						for(int l=i+1; l < N; ++l)
							if(matrix[k][l] == 1)
							{
								found = false;
								break;
							}

						if(found == true)
						{
							for(int m=k; m > i; --m)
								for(int l=0; l < N; ++l)
									matrix[m][l] = matrix[m-1][l];

							swaps += k - i;
							break;
						}
					}

					break;
				}

		cout << "Case #" << X << ": " << swaps << '\n';
	}

	return 0;
}