#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	ifstream fin("D://A-small-attempt0.in");
	ofstream fout("D://gcj.txt");
	unsigned T,N,K;
	fin >> T;
	for (int i=1;i<=T;i++)
	{
		fin >> N >> K;
		unsigned k=K+1;
		unsigned z=(1 << N);
		fout << "Case #" << i << ": ";
		if (k % z == 0)
		{
			fout << "ON\n";
		}
		else
			fout << "OFF\n";
	}
	fout.close();
	return 0;
}