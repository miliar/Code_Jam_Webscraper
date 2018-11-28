#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ofstream fout ("D-large.out");
	ifstream fin ("D-large.in");
	int tests;
	fin >> tests;
	for(int test = 0; test < tests; test++)
	{
		int n, m = 0;
		fin >> n;
		for(int i = 0; i < n; i++)
		{
			int a;
			fin >> a;
			if(a != i + 1)
				m++;
		}
		fout << "Case #" << test + 1 << ": " << m << ".000000" << endl;
	}
	return 0;
}
