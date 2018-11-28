#include <fstream>
using namespace std;

void main()
{
	ifstream fin;
	ofstream fout;

	fin.open("A.in");
	fout.open("A.out");

	int test;
	fin >> test;

	int input, index;
	int pow2;

	for(int i = 1; i <= test; i++)
	{
		fin >> index >> input;

		pow2 = 1;
		for(int j = 0; j < index; j++)
		{
			pow2 *= 2;
		}

		fout << "Case #" << i << ": ";
		if(input % pow2 == pow2 - 1) fout << "ON" << endl;
		else fout << "OFF" << endl;
	}
}