#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream inFile("B-large.in");
	ofstream outFile("B-large.out");

	int C;
	inFile >> C;

	for (int nTestCase = 1; nTestCase <= C; nTestCase++)
	{
		int N, K, B, T;
		inFile >> N >> K >> B >> T;

		vector<int> x(N);
		vector<int> v(N);

		for (int i = 0; i < N; i++)
			inFile >> x[i];
		for (int i = 0; i < N; i++)
			inFile >> v[i];

		int swapCount = 0;
		int tooSlow = 0;
		int madeIt = 0;
		for (int i = N - 1; i >= 0 && madeIt < K; i--)
		{
			if (v[i] * T + x[i] >= B)
			{
				madeIt++;
				swapCount += tooSlow;
			}
			else
				tooSlow++;
		}

		outFile << "Case #" << nTestCase << ": ";
		if (madeIt == K)
			outFile << swapCount;
		else
			outFile << "IMPOSSIBLE";
		outFile << endl;
	}

	return 0;
}
