#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <stack>
using namespace std;

int main()
{
	ifstream ifile("D:\\A-large.in");
	ofstream ofile("D:\\A-large.out");
	int T;
	ifile >> T;
	for(int num = 0; num < T; num++)
	{
		int N,K;
		ifile >> N >> K;
		int all = 1 << N;
		
		if ((K+1)%all == 0)
		{
			ofile << "Case #" << num+1 << ": ON" << endl;
		}
		else
			ofile << "Case #" << num+1 << ": OFF" << endl;
	}

	ifile.close();
	ofile.close();
	return 0;
}