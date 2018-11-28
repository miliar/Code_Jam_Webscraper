#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
using namespace std;

#define INBOARD(X,Y) (((X) >= 0) && ((Y) >= 0) && ((X) < h) && ((Y) < w))

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int imap[100][100];
	char cmap[100][100];
	int h,w;
	int n;

	int directions[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

	fin >> n;
	for (int order = 1; order <= n; order++)
	{
		fin >> h >> w;

		for (int i = 0; i != h; i++)
		{
			for (int j = 0; j != w; j++)
			{
				fin >> imap[i][j];
				cmap[i][j] = ' ';
			}
		}

		char nextc = 'a';
		for (int i = 0; i != h; i++)
		{
			for (int j = 0; j != w; j++)
			{
				if (cmap[i][j] == ' ') // not calculate
				{
					int row = i,col = j;
					bool not_paint = true,not_basin = true;
					vector<int> rlist,clist;

					while (not_paint && not_basin)
					{
						rlist.push_back(row);
						clist.push_back(col);

						int d = -1,low = 20000000;

						for (int k = 0; k < 4; k++)
						{
							if (INBOARD(row + directions[k][0],col + directions[k][1]) && (imap[row + directions[k][0]][col + directions[k][1]] < low) && (imap[row + directions[k][0]][col + directions[k][1]] < imap[row][col]))
							{
								d = k;
								low = imap[row + directions[k][0]][col + directions[k][1]];
							}
						}

						if (d >= 0 && low < 20000000)
						{
							row = row + directions[d][0];
							col = col + directions[d][1];
						}
						else
						{
							not_basin = false;
						}

						if (cmap[row][col] != ' ')
						{
							not_paint = false;
						}
					}

					if (!not_basin) // x and y basin
					{
						cmap[row][col] = nextc++;
					}

					for (int l = 0; l != rlist.size(); l++)
					{
						cmap[rlist[l]][clist[l]] = cmap[row][col];
					}
				}
			}
		}

		fout << "Case #" << order << ":" << endl;
		for (int i = 0; i < h; i++)
		{
			for (int j = 0; j < w - 1; j++)
			{
				fout << cmap[i][j] << " ";
			}
			fout << cmap[i][w - 1] << endl;
		}
	}

	fout.close();
	fin.close();

	return 0;
}