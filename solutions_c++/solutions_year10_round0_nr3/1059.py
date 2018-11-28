#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream inputFile;
	ofstream outputFile;

	inputFile.open("D:\\test_Google_Code_Jam\\C-large.in");
	outputFile.open("D:\\test_Google_Code_Jam\\C-large.out");
	__int64 T;
	inputFile >> T;
	for(__int64 cT = 1; cT <= T; cT++)
	{
		// 输入部分。
		__int64 R, k, N;
		inputFile >> R >> k >> N;

		// 我的数据结构。
		vector<__int64> vecG(N);
		__int64 cIndex = 0;
		__int64 nSumProfit = 0;	// 按欧元结算~~
		__int64 nTotalPeople = 0;
		for(__int64 i=0; i<N; i++)
		{
			__int64 n;
			inputFile >> n;
			vecG[i] = n;
			nTotalPeople += n;
		}

		if(nTotalPeople <= k)
		{
			nSumProfit = R * nTotalPeople;
		}
		else
		{
			for(__int64 cR = 0; cR < R; cR++)
			{
				__int64 nRemain = k;
				while(true)
				{
					__int64 nSizeOfGroup = vecG[cIndex];
					if(nRemain >= nSizeOfGroup)
					{
						nRemain -= nSizeOfGroup;
						nSumProfit += nSizeOfGroup;
						cIndex++;
						cIndex %= N;
					}
					else
					{
						break;
					}
				}
			}
		}

		outputFile << "Case #" << cT << ": " << nSumProfit << endl;		
		cout << "Case #" << cT << ": " << nSumProfit << endl;		
	}

	inputFile.close();
	outputFile.close();
	return 0;
}