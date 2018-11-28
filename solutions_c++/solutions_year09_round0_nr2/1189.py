#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

char label;

char floodFill(vector< vector<int> >& m, vector< vector<char> >& b, int r, int c)
{
	if (b[r][c] != 'M')
	{
		return b[r][c];
	}
	int nwesL[4] = {100000, 100000, 100000, 100000};
	int nwesR[4] = {-1, 0, 0, +1};
	int nwesC[4] = {0, -1, +1, 0};
	if(r > 0)
	{
		nwesL[0] = m[r-1][c];
	}
	if (c > 0)
	{
		nwesL[1] = m[r][c-1];
	}
	if (c < m[0].size() - 1)
	{
		nwesL[2] = m[r][c+1];
	}
	if (r < m.size() - 1)
	{
		nwesL[3] = m[r+1][c];
	}

int minL = 100000;
int nr, nc;
	for (int i = 0; i < 4; ++i)
	{
		if (nwesL[i] < minL)
		{
			minL = nwesL[i];
			nr = r + nwesR[i];
			nc = c + nwesC[i];
		}
	}

	if (m[r][c] > minL)
	{
			b[r][c] = floodFill(m, b, nr, nc);
	}
	else
	{
			b[r][c] = label;
			++label;
	}

	return b[r][c];
}

int main()
{
	fstream fin("1.txt", fstream::in);
	fstream fout("1.out.txt", fstream::out);

	int T,H,W;
	fin>>T;
	for (int i = 0; i < T; ++i)
	{
		fin>>H>>W;
		vector< vector<int> > mp(H, vector<int> (W, 0));
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
			{
				fin>>mp[j][k];
			}
		}

		vector< vector<char> > basin(H, vector<char> (W, 'M'));
		label = 'a';
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
			{
				if (basin[j][k] == 'M')
				{
					floodFill(mp, basin, j, k);
				}
			}
		}
		
		fout<<"Case #"<<i+1<<":"<<endl;
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
			{
				fout<<basin[j][k]<<" ";
			}
			fout<<endl;
		}
	}

	return 0;
}