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
using namespace std;

ifstream fin("B.in");
ofstream fout("B.out");
const double EPS = 1e-10;

int main(void)
{
	int C;
	fin >> C;
	for (int tc = 1; tc <= C; tc++)
	{
		int N, M, A;
		fin >> N >> M >> A;
		fout << "Case #" << tc << ": ";
		for (int x1 = 0; x1 <= N; x1++)
		{
			for (int x2 = 0; x2 <= N; x2++)
			{
				for (int y1 = 0; y1 <= M; y1++)
				{
					for (int y2 = 0; y2 <= M; y2++)
					{
						if (x1*y2-x2*y1 == A)
						{
							fout << "0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
							goto qq;
						}
					}
				}
			}
		}
		fout << "IMPOSSIBLE" << endl;
qq:;
	}
	return 0;
}
