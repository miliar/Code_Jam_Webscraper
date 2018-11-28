#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

bool compareInt(const int &i1, const int &i2)
{
	return i1 > i2;  //reverse order
}

int main(int argc, char *argv[])
{
	if (argc < 2)
	{
		cout << "Missing arguments!" << endl;
		return -1;
	}

	ifstream inputFile = ifstream(argv[1]);
	string outputFileName = string(argv[1]) + ".out";
	ofstream outputFile = ofstream(outputFileName.c_str());
	if (!inputFile || !outputFile)
	{
		cout << "Open file error" << endl;
		return -2;
	}
	
	int caseNum;
	inputFile >> caseNum;
	int i = 0, count;
	int dancerNum, surpNum, bestScore, score;
	vector<int> scores;
	while (i < caseNum)
	{
		scores.clear();
		count = 0;
		inputFile >> dancerNum >> surpNum >> bestScore;
		for (int j = 0; j != dancerNum; ++j)
		{
			inputFile >> score;
			scores.push_back(score);
		}
		sort(scores.begin(), scores.end(), compareInt);
		for (vector<int>::iterator iter = scores.begin(); iter != scores.end(); ++iter)
		{
			if (*iter >= 3 * bestScore - 2)	++count; //not surprising
			else if (*iter >= 2 && *iter <= 28 && *iter >= 3 * bestScore - 4 && surpNum > 0) //surprising
			{
				++count;
				--surpNum;
			}
		}
		outputFile << "Case #" << ++i << ": " << count << endl;
	}
	outputFile.flush();
	inputFile.close();
	outputFile.close();
	return 0;
}