#include <fstream>
using namespace std;

ifstream input("input.txt");
ofstream output("output.txt");

char field[52][52];
int r,c;

int main()
{
	int t;
	input >> t;
	for (int z=0;z<t;++z)
	{
		input >> r >> c;
		for (int i=0;i<r;++i)
			input >> field[i];
		bool possible = true;
		for (int i=0;i<r;++i)
		{
			for (int j=0;j<c;++j)
			{
				if (field[i][j] == '#' && i<r-1 && j<c-1 && field[i+1][j]=='#' && field[i][j+1] == '#' && field[i+1][j+1] == '#')
				{
					field[i][j]='/'; field[i][j+1]='\\'; field[i+1][j]='\\'; field[i+1][j+1]='/';
				}
				else if (field[i][j]=='#') possible = false;
			}
		}
		output << "Case #" << z+1 << ":" << endl;
		if (possible)
		{
			for (int i=0;i<r;++i) output << field[i] << endl;
		}
		else output << "Impossible" << endl;
	}
	return 0;
}