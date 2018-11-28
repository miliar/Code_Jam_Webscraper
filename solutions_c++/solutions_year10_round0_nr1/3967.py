#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;

	fin.open("A-large.in", ios::in);
	fout.open("A-large.out", ios::out);

	int T;

	fin >> T;

	for(int i = 0; i < T; i++)
	{
		long int K;
		int N;

		fin >> N >> K;

		int maxInBase = pow(2.0, N);

		if((K + 1) % maxInBase == 0)
		{
			fout << "Case #" << i + 1 << ": " << "ON" << endl;
		}

		else
		{
			fout << "Case #" << i + 1 << ": " << "OFF" << endl;
		}
	}
}