#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream inputFile;
	ofstream outputFile;

	//inputFile.open("C:\\Documents and Settings\\Administrator\\桌面\\test_Google_Code_Jam\\A.in");
	inputFile.open("D:\\test_Google_Code_Jam\\A-large.in");	// 日，不能带中文。
	outputFile.open("D:\\test_Google_Code_Jam\\A-large.out");
	int T;
	inputFile >> T;
	for(int cT = 1; cT <= T; cT++)
	{
		int N, K;
		inputFile >> N >> K;
		int _K = K + 1;
		int _N = 1 << N;
		if(_K % _N == 0)
			outputFile << "Case #" << cT << ": ON" << endl;
		else
			outputFile << "Case #" << cT << ": OFF" << endl;
	}

	inputFile.close();
	outputFile.close();
	return 0;
}