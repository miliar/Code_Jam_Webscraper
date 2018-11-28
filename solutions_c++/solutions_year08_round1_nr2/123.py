#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int white[3000][3000];

int main()
{
	ifstream fin("c:\\codejam\\milk2.txt");
	ofstream fout("c:\\codejam\\milk_out.txt");
	int num_cases;
	fin >> num_cases;

	for (int p=0; p<num_cases; p++)
	{
		int n, m;
		fin >> m;
		fin >> n;
		int nw[3000];
		int black[3000];
		bool good[3000];
		for (int i=0; i<n; i++)
		{
			good[i] = false;
			int c;
			fin >> c;
			black[i] = -1;
			nw[i] = 0;
			for (int j=0; j<c; j++)
			{
				int a, b;
				fin >> a >> b;
				a = a - 1;
				if (b == 0)
				{
					white[i][nw[i]] = a;
					nw[i]++;
				}
				else
				{
					black[i] = a;
				}
			}
			for (int j=0; j<nw[i]; j++)
			{
				if (white[i][j] == black[i])
				{
					good[i] = true;
				}
			}
		}

		int r[3000];
		for (int i=0; i<m; i++)
		{
			r[i] = 0;
		}

		bool impossible = false;
		bool done = false;
		do
		{
			done = true;
			for (int i=0; i<n; i++)
			{
				if (!good[i])
				{
					bool v = false;
					for (int j=0; j<nw[i]; j++)
					{
						int k = white[i][j];
						if (r[k] == 0)
						{
							v = true;
						}
					}
					if (!v)
					{
						if (black[i] == -1)
						{
							impossible = true;
							break;
						}
						r[black[i]] = 1;
						good[i] = true;
						done = false;
					}
				}
			}
			if (impossible)
			{
				break;
			}
		} while (!done);
				
		fout << "Case #" << p + 1 << ":";
		if (impossible)
		{
			fout << " IMPOSSIBLE" << endl;
		}
		else
		{
			for (int i=0; i<m; i++)
			{
				fout << " " << r[i];
			}
			fout << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}