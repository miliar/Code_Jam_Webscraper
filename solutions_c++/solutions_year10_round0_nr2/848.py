#include <fstream>
using namespace std;

int abs(int n)
{
	if(n > 0) return n;
	else return -n;
}

int gcd(int m, int n)
{
	while(m > 0 && n > 0)
	{
		if(m > n) m %= n;
		else n %= m;
	}
	return m + n;
}

void main()
{
	ifstream fin;
	ofstream fout;

	fin.open("A.in");
	fout.open("A.out");

	int test;
	fin >> test;
	int cases;
	int times[3];

	for(int i = 1; i <= test; i++)
	{
		fin >> cases;
		for(int j = 0; j < cases; j++)
		{
			fin >> times[j];
		}
		
		for(int j = 1; j < cases; j++)
		{
			times[j-1] = abs(times[j] - times[j-1]);
		}
		
		for(int j = cases - 1; j > 1; j--)
		{
			times[j-2] = gcd(times[j-2], times[j-1]);
		}
		times[cases-1] %= times[0];
		if(times[cases-1] > 0) times[cases-1] = times[0] - times[cases-1];
		fout << "Case #" << i << ": " << times[cases-1] << endl;
	}
}