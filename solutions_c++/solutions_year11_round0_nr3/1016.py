#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int MAX = 1000 * 1000 + 10;

int main()
{
	ofstream fout ("C-large.out");
	ifstream fin ("C-large.in");
	int tests;
	fin >> tests;
	for(int test = 0; test < tests; test++)
	{
		int n, m = MAX, s = 0, xs = 0;
		fin >> n;
		for(int i = 0, a; i < n; i++)
			fin >> a, 
			s += a, 
			xs ^= a, 
			m = min(m, a);
		if(xs)
			fout << "Case #" << test + 1 << ": NO"<< endl;
		else
			fout << "Case #" << test + 1 << ": " << s - m << endl;
	}
	return 0;
}
