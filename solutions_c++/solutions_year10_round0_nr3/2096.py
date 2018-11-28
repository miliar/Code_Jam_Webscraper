#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int a[10001];
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");

	int t;
	fin >> t;

	int i, j;
	int r, k, n, sum, total, begin, end, c, temp;

	for( i = 1; i <= t; i++)
	{
		fin >> r >> k >> n;
		for( j = 0; j < n; j++)
			fin >> a[j];
		begin = 0;
		end = n;
		sum = 0;
		total = 0;
		for( c = 1; c <= r; c++)
		{
			temp = end;
			while( sum <= k && begin < temp)
			{
				sum += a[begin];
				total += a[begin];
				a[end++] = a[begin++];
			}
			if( sum > k )
			{
				sum -= a[--end];
				total -= a[end];
				--begin;
			}
			sum = 0;
		}
		fout << "Case #" << i << ": " << total << endl;
	}
	return 0;
}

