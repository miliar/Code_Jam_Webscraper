//---------------------------------------------------------------------------

#pragma hdrstop

#include <tchar.h>
//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>
#include <stdlib>
#include <string>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C.out");
	fin >> t;
	int p = 1;

	//p = p;

	

	for (int i=0; i<t;i++)
	{
		long p = 1;
		int n;
		fin >> n;
		long a[16];
		for (long y= 0 ;y<n; y++) {
			p *= 2;
			fin >> a[y];
		}

		long max = 0;
		for (int y=1; y<p-1; y++) {
			long sum1 = 0; long sum2 = 0;
			long xsum1 = 0; long xsum2 = 0;
			long u = y;
			long j = 0;
			while (j < n) {
				if ((u | 1) == u) {
					sum1 += a[j];
					xsum1 ^= a[j];
				} else {
					sum2 += a[j];
					xsum2 ^= a[j];
				}
				j++;
				u = u >> 1;

			}

			if (xsum1 == xsum2) {
				if (max < sum1) max = sum1;
				if (max < sum2) max = sum2;
            }
		}


		fout << "Case #" << (i+1) << ": ";
		if (max > 0)
			fout << max << endl;
		else
			fout << "NO" << endl;






	}

	fin.close();

	return 0;
}
//---------------------------------------------------------------------------
