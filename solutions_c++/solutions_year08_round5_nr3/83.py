#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

ifstream fin;
ofstream fout;

string a[1024];
int cnt [2][1 << 21];
int n, m;

bool ok (int r, int i, int j)
{
	for (int q = 0; q < m; ++ q)
		if ((1 << q) & j)
		{
			if (a[r][q] == 'x') return false;
			if (q > 0 && ((1 << (q - 1)) & j) != 0) return false;
			if (q > 0 && ((1 << (q - 1)) & i) != 0) return false;
			if (((1 << (q + 1)) & i) != 0) return false;
			if (((1 << (q + 1)) & j) != 0) return false;
		}

	return true;
}

int getc (int k)
{
	int res = 0;
	while (k)
	{
		++ res;
		k &= k - 1;
	}
	return res;
}

int main (int argc, char * argv [])
{

	if (argc  == 1)  
	{
		fin.open("input.txt");
		fout.open("output.txt");
	}
	else 
	{
		fin.open(argv[1]);
		fout.open(argv[2]);
	}

	int tests = 0;
	fin >> tests;

	while (tests -- > 0)
	{


		fin >> n >> m;

		for (int i = 0; i < n; ++ i) fin >> a[i];

		memset (cnt, 0xff, sizeof (cnt));

		int curr = 0;
		cnt[0][0] = 0;

		for (int s = 0; s < n; ++ s)
		{
			for (int i = 0; i < (1 << m); ++ i)
				if (cnt [curr][i] != -1)
					for (int j = 0; j < (1 << m); ++ j)
						if (ok (s, i, j)) 
						{
							cnt [1 - curr][j] = max (cnt [1 - curr][j], cnt [curr][i] + getc (j));
							if (s == 1 && j == 5)
							{
								//cout << i << ' ' << cnt [1 - curr][j] << endl;
							}
						}
			memset (cnt [curr], 0xff, sizeof (cnt[curr]));
			curr = 1 - curr;
		}

		int res = 0;
		for (int i = 0; i < (1 << m); ++ i)  
		{
			//if (cnt [curr][i]  > res) cout << i << endl;
			res = max (res, cnt [curr][i]);
		}
		//cout << '-' << endl;

		static int caseNum = 0;
		fout << "Case #" <<  (++ caseNum) << ": " << res << endl;
	}

	return 0;
}