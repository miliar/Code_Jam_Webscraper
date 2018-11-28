#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		std::cerr << "The input parameter error!" << std::endl;
		return -1;
	}

	std::ifstream iFile(argv[1]);
	std::ofstream oFile(argv[2]);

	if (!iFile.is_open())
	{
		std::cerr << "Can not open input file!" << std::endl;
		return -1;
	}

	oFile.setf(std::ios::fixed, std::ios::floatfield);
	oFile.precision(6);

	int T;
	iFile >> T;
	std::string sline;
	getline(iFile, sline);
	for (int i = 0; i != T; ++i)
	{
		int A, B;
		iFile >> A >> B;
		getline(iFile, sline);
		std::vector<float> vPro(A);
		for (int j = 0; j != A; ++j)
		{
			iFile >> vPro[j];
		}
		getline(iFile, sline);

		float allRight  = 1.0f;
		for (int j = 0; j != A; ++j)
		{
			allRight *= vPro[j];
		}

		std::vector<float> BackNum(A, 1.0);
		for (int j = 0; j != A; ++j)
		{
			int k;
			for (k = 0; k != A - j - 1; ++k)
			{
				BackNum[j] *= vPro[k];
			}
			for (k; k != A; ++k)
			{
				BackNum[j] *= 1 - vPro[k];
			}
		}

		float minType;
		float tempType;
		
		// for strategy one
		minType = (B - A + 1) * allRight + (B + B - A + 2) * (1 - allRight);

		// for strategy tree
		tempType = B + 2;
		minType = std::min(minType, tempType);

		// for strategy two
		for (int j = 0; j != A; ++j)
		{
			tempType = (j + 1 + B - A + j + 1 + 1) * (allRight + BackNum[j]) 
				+ (B + B - A + j + j + 4) * (1 - allRight - BackNum[j]);
			minType = std::min(minType, tempType);
		}

		oFile << "Case #" << i + 1 << ": " << minType << std::endl;
	}

	return 0;
}