#include <fstream>

using namespace::std;
int T, R, C;
	int i, j, k;
	int Map[51][51];
	char tmp;
	ifstream input("D:\\a.txt", ifstream::in);
	ofstream output("D:\\b.txt", ofstream::out);
bool xxx()
{
	for (j = 0; j < R; j++)
		{
			for (k = 0; k < C; k++)
			{
				if (Map[j][k] == 1)
				{
					if (k + 1 == C || j + 1 == R)
					{
						output << "Impossible" << endl;
						return false;
					}

					if (Map[j][k + 1] == 1  &&	(Map[j + 1][k] == 1 && Map[j + 1][k + 1] == 1))
					{
						Map[j][k] = 2;//'/'
						Map[j][k + 1] = 3;//'\'
						Map[j + 1][k] = 4;//'\'
						Map[j + 1][k + 1] = 5;//'/'
						k++;
					}
					else
					{
						output << "Impossible" << endl;
						return false;
					}
				}

				
			}
		}

	return true;
}
int main()
{
	

	input >> T;
	for (i = 0; i < T; i++)
	{
		output << "Case #" << i + 1 << ":" << endl;
		memset(Map, 0, sizeof Map);
		input >> R >> C;
		for (j = 0; j < R; j++)
		{
			for (k = 0; k < C; k++)
			{
				input >> tmp;
				if (tmp == '#')
				{
					Map[j][k] = 1;
				}
			}
		}

		if (!xxx())
		{
			continue;
		}

		for (j = 0; j < R; j++)
		{
			for (k = 0; k < C; k++)
			{
				if (Map[j][k] == 0)
				{
					output << '.';
				}
				else if (Map[j][k] == 2)
				{
					output << '/';
				}
				else if (Map[j][k] == 3)
				{
					output << '\\';
				}
				else if (Map[j][k] == 4)
				{
					output << '\\';
				}
				else
				{
					output << '/';
				}

				if (k == C - 1)
				{
					output << endl;
				}
			}
		}
	}
	return 0;
}