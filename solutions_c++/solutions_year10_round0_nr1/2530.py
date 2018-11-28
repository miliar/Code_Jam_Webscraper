#include <iostream>
#include <fstream>

using namespace std;

void main(void)
{
	ifstream inFile("A-large.in");
	ofstream outFile("a.out");

	int T = 0;
	inFile >> T;
	int N,K;


	for(int i=0; i<T; i++)
	{
		bool flag = false;
		inFile >> N >> K;
		N = 2 << (N-1);
		K = K % N;

		outFile << "Case #" << i+1 << ": ";
		if(K==N-1)
		{
			outFile << "ON" << std::endl;
		}
		else
		{
			outFile << "OFF" << std::endl;
		}
	}
}