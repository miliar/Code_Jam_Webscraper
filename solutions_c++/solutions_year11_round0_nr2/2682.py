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
	ifstream fin("B-large.in");
	ofstream fout("B.out");
	fin >> t;

	for (int i=0; i<t;i++)
	{
		long count = 0;

		//string[10] cArr;
		int c;
		static int cArr[32][32];
		static int dArr[32][32];
		for (int u = 0; u < 32; u++) {
			for (int uu = 0; uu< 32; uu++) {
				cArr[u][uu] = 0;
				dArr[u][uu] = 0;
			}
		}
		fin >> c;
		for (int j = 0; j< c; j++)
		{
			char c1, c2, c3;
			fin >> c1 >> c2 >> c3;
			cArr[c1 - 'A' + 1][c2 - 'A' + 1] = c3 - 'A' + 1;
			cArr[c2 - 'A' + 1][c1 - 'A' + 1] = c3 - 'A' + 1;
		}

		int d;


		fin >> d;
		for (int j = 0; j< d; j++)
		{
			char c1, c2;
			fin >> c1 >> c2;
			dArr[c1 - 'A' + 1][c2 - 'A' +1] = 1;
			dArr[c2 - 'A' + 1][c1 - 'A' + 1] = 1;
		}

		int n;
		fin >> n;
		char c1;
		char res[100];
		char kRes = 0;
		for (int j=0; j< n; j++) {
			fin >> c1;
			int flag = 1;
			if (kRes > 0) {
				int p = c1 - 'A' + 1;
				if (cArr[p][res[kRes-1] - 'A' + 1] != 0) {
					res[kRes-1] = cArr[p][res[kRes-1] - 'A' + 1] + 'A' - 1;
					flag = 0;
				}
				else
					for (int jj = 0; jj < kRes; jj++)
					{
						if (dArr[res[jj] - 'A' + 1][p] == 1) { kRes = 0;
                        flag = 0;
						break;}
					}
			}
			if (flag) {
				res[kRes++] = c1;

            }

		}

        fout << "Case #" << (i+1) << ": [";

        for (int jj = 0; jj < kRes-1; jj++)
		{
			fout << res[jj] << ", ";
		}

		if (kRes > 0) {
			fout << res[kRes - 1];

		}

		fout << "]" << endl;


	}

	fin.close();

	return 0;
}
//---------------------------------------------------------------------------
