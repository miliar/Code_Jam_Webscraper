#include <iostream>
#include <fstream>
using namespace std;

#define INPUT "C-large.in"

int main()
{
	ofstream fout("1.txt");
	ifstream fin(INPUT);
	int n;
	fin >> n;
	int total;
	int min;
	int sum = 0;
	int asum = 0;
	for ( int cc = 1; cc <= n; cc++)
	{
		sum = 0;
		asum = 0;
		fin >> total;
		fin >> min;
		sum += min;
		asum = asum^min;
		int tmp;
		for (int i = 1; i < total; i++)
		{
			fin >> tmp;
			sum += tmp;
			asum = asum ^ tmp;
			if (tmp < min)
				min = tmp;
		}
		if (asum == 0)
		{
			fout << "Case #" << cc << ": "<< sum - min << endl;
		}
		else
			fout << "Case #" << cc << ": " << "NO" << endl;
	}
	fin.close();
	fout.close();
}
