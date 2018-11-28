#include <iostream>
#include <sstream>
#include <vector>
#include <fstream>
#include <string>

int main(int argc, char *argv[])
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

	int T, S, p, N;
	iFile >> T;
	std::string sline;
	getline(iFile, sline);
	for (int i = 0; i != T; ++i)
	{
		getline(iFile, sline);
		std::stringstream ssline(sline);
		ssline >> N >> S >> p;
		std::vector<int> scores(N);
		for (int j = 0; j != N; ++j)
			ssline >> scores[j];

		int max_result = 0;
		for (int j = 0; j != N; ++j)
		{
			int pm = p - 2 > 0 ? p - 2 : 0;
			pm = pm << 1;
			if (scores[j] >= p * 3 - 2)
				++max_result;
			else if (scores[j] >= p + pm && S > 0)
			{
				++max_result;
				--S;
			}
		}

		oFile << "Case #" << i + 1 << ": " << max_result << std::endl;
	}

	iFile.close();
	oFile.close();

	return 0;
}