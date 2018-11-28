#include <fstream>
#include <vector>
#include <string>

using namespace std;

/*
The first line of the input gives the number of test cases, T. T test cases follow.
Each one starts with a line containing 3 integers: R, C and D — the dimensions of the grid and 
the mass you expected each cell to have. The next R lines each contain C digits wij each, 
giving the differences between the actual and the expected mass of the grid cells. Each cell has a uniform density,
but could have an integer mass between D + 0 and D + 9, inclusive.
*/

int g[600][600];
int m[600][600];
int iM[600][600];
int jM[600][600];
int r, c, d;

int findK(int kM) {
	for (int k = kM; k >= 2; --k)
	{
		for (int i = 0; i < c - k + 1; ++i)
		{
			for (int j = 0; j < c - k + 1; ++j)
			{
				int mas = m[i + k][j + k] + m[i][j] - m[i + k][j] - m[i][j + k];
				mas -= (g[i][j] + g[i+k-1][j] + g[i][j + k-1] + g[i+k-1][j+k-1]); 

				int masI = iM[i + k][j + k] + iM[i][j] - iM[i + k][j] - iM[i][j + k];
				masI -= (g[i][j] * i + g[i+k-1][j] *(i+k-1) + g[i][j + k-1]*i + g[i+k-1][j+k-1]*(i+k-1)); 

				int masJ = jM[i + k][j + k] + jM[i][j] - jM[i + k][j] - jM[i][j + k];
				masJ -= (g[i][j] * j + g[i+k-1][j] *j + g[i][j + k-1]*(j + k - 1) + g[i+k-1][j+k-1]*(j+k-1)); 

				if(2 * masI == 2 * i*mas + mas * (k-1) && 2 * masJ == 2* j*mas + mas * (k-1)) {
					return k;
				}
			}
		}
	}

	return 0;
}

int main() {

	ifstream in("B-small-attempt1.in");
	ofstream out("out.txt");

	int t;
	in >> t;
	for (int tc = 1; tc <= t; ++tc) {
		
		in >> r >> c >> d;
		string s;
		for (int i = 0; i < r; ++i)
		{
			in >> s;
			for (int j = 0; j < c; ++j)
			{
				g[i][j] = s[j] - '0';
			}
		}
		memset(m, 0, sizeof(m));
		memset(iM, 0, sizeof(iM));
		memset(jM, 0, sizeof(jM));

		for (int i = 0; i < c; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				m[i+1][j+1] = g[i][j] + m[i][j+1] + m[i+1][j] - m[i][j];
				iM[i+1][j+1] = g[i][j] * i + iM[i][j+1] + iM[i+1][j] - iM[i][j];
				jM[i+1][j+1] = g[i][j] * j + jM[i][j+1] + jM[i+1][j] - jM[i][j];
			}
		}

		int kM = min(r, c);
		int k = findK(kM);
		if (k > 2)
		{

			out << "Case #" << tc <<": " << k <<  endl;
		}
		else
			out << "Case #" << tc <<": " << "IMPOSSIBLE" <<  endl;

	}
	return 0;
}