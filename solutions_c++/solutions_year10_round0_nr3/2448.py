#include <iostream>
#include <fstream>

int g[1010];

using namespace std;

void main(void)
{
	int T;
	int R, k, N;
	ifstream inFile("b.in");
	ofstream outFile("b.out");

	inFile >> T;

	for (int i=1; i<=T; i++)
	{
		long long money=0;

		inFile >> R >> k >> N;
		for (int m=0; m<N; m++)
		{
			inFile >> g[m];
		}
		int idx = 0;
		for (int j=1; j<=R; j++)
		{
			int sumNum = 0;

			for (int n=0; n<N; n++)
			{
				sumNum += g[idx];
				if (sumNum > k)
				{
					sumNum -= g[idx];
					break;
				}
				idx++;
				idx %= N;
			}
			money += sumNum;
			
		}
		outFile << "Case #" << i << ": " << money << std::endl;

	}

}