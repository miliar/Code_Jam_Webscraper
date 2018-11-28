#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt", ios::out | ios::trunc);

	int sizeOfTests = 0;
//read
	if (in == 0 || out == 0)
	{
		
		return 0;
	}
	in >> sizeOfTests;

	for (int k = 0; k < sizeOfTests; k++)
	{
		int mymin = 1000001, mysum = 0, xorsum = 0, mysize = 0;
		in >> mysize;
		for (int i = 0, a = 0; i < mysize; xorsum^=a, mysum+=a, i++)
		{
			in >> a;
			if (a < mymin)
			{
				mymin = a;
			}
		}
		if (xorsum == 0)
		{
			out << "Case #" << k+1 << ": " << mysum - mymin << "\n";
		}
		else
		{
			out << "Case #" << k+1 << ": " << "NO" << "\n";
		}
	}


	return 0;
}