#include <iostream>
#include <string>
#include <fstream>
#include <map>

using namespace std;

const int INF = 987654321;
int S, Q;
map<string, int> se;
int D[1001][100];

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");

	int ncase;
	fin >> ncase;
	for (int ni = 1; ni <= ncase; ni++)
	{
		se.clear();
		string str;

		fin >> S;
		getline(fin, str);
		for (int i = 0; i < S; i++)
		{
			getline(fin, str);
			se[str] = i;
		}

		fin >> Q;
		getline(fin, str);

		for (int i = 0; i <= Q; i++)
		{
			for (int j = 0; j < S; j++)
			{
				D[i][j] = INF;
			}
		}
		for (int j = 0; j < S; j++)
		{
			D[0][j] = 0;
		}

		for (int i = 1; i <= Q; i++)
		{
			getline(fin, str);
			int skip = se[str];
			for (int j = 0; j < S; j++)
			{
				if (j != skip)
				{
					if (D[i-1][j] == INF)
					{
						for (int k = 0; k < S; k++)
						{
							if (D[i-1][k] != INF && D[i][j] > D[i-1][k] + 1)
							{
								D[i][j] = D[i-1][k] + 1;
							}
						}
					}
					else
					{
						D[i][j] = D[i-1][j];
					}
				}
			}
		}

		int ans = INF;
		for (int j = 0; j < S; j++)
		{
			if (ans > D[Q][j])
			{
				ans = D[Q][j];
			}
		}

		fout << "Case #" << ni << ": " << ans << endl;
	}
}
