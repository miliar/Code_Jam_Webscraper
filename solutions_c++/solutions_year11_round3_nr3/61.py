#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

ifstream fin("C-small-attempt0 (1).in");
ofstream fout("1c_c.out");

//#define fout cout

int a[20000];

int main()
{
	int T;
	fin >> T;
	for (int cases =0; cases<T; cases++)
	{
		int N;
		long long L, H;
		fin >> N >> L >> H;
		for (int i=0; i<N; i++) fin >> a[i];
		fout << "Case #" << cases+1 << ": ";
		bool success;
		for (long long x=L; x<=H; x++)
		{
			success = true;
			for (int j=0; j<N; j++)
				if (!(a[j] % x == 0 || x % a[j] == 0))
				{
					success = false;
					break;
				}
			if (success)
			{
				fout << x << '\n';
				break;
			}
		}
		if (!success) fout << "NO\n";
	}
	return 0;
}
