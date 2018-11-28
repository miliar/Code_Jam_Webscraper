#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <fstream>
#include <vector>
#include <set>
#include <complex>
#include <map>
#include <algorithm>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <bitset>
using namespace std;

ifstream fin("D.in");
ofstream fout("D.out");
const double EPS = 1e-10;
const int prime = 10007;
int obr[prime];
int W, H, R;

vector< vector<bool> > dark;

int main(void)
{
	int number_of_tests;
	fin >> number_of_tests;
	for (int test_case = 1; test_case <= number_of_tests; test_case++)
	{
		fin >> H >> W >> R;
		dark.clear();
		dark.resize(H, vector<bool>(W));
		for (int i = 0; i < R; i++)
		{
			int r, c;
			fin >> r >> c;
			dark[r-1][c-1] = true;
		}
		vector<vector<int> > res(H, vector<int>(W));
		res[0][0] = 1;
		if ((H > 1) && (W > 2)) res[1][2] = (dark[1][2])?0:1;
		if ((H > 2) && (W > 1)) res[2][1] = (dark[2][1])?0:1;
		for (int i = 2; i < H; i++)
		{
			for (int j = 2; j < W; j++)
			{
				if (!dark[i][j])
					res[i][j] = (res[i-1][j-2] + res[i-2][j-1]) % prime;
			}
		}
		fout << "Case #" << test_case << ": ";
		fout << res[H-1][W-1];
		fout << endl;
	}
	return 0;
}
