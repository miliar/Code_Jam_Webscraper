#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int t;
	ifstream fin("A-large.in", ios::in);
	ofstream fout("A-large.out", ios::out);
	fin >> t;

	for (int count = 0; count != t; ++count)
	{
		unsigned long k, n, bit = 1, mask = 0;
		fin >> n >> k;
		bit <<= n;
		k %= bit;
		--mask;
		mask %= bit;
		fout << "Case #" << (count + 1) << ": " << ((k == mask) ? "ON" : "OFF") << endl;
	}
	return 0;
}
