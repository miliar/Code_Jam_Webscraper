#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream f("a.in");
	ofstream f2("a.out");

	int T;
	f>>T;

	for(int testcase = 1; testcase <= T; ++testcase)
	{
		f2<<"Case #" << testcase << ":\n";
		int rows, cols;
		f>>rows>>cols;

		int matrix[51][51];
		for(int i = 0; i<51; ++i)
			memset(matrix[i],0,sizeof(matrix[i]));

		for(int r = 0; r<rows; ++r)
		{
			string s;
			f>>s;
			for(int c = 0; c<cols; ++c)
				matrix[r][c] = s[c];
		}

		bool possible = true;
		for(int r = 0; r<rows && possible; ++r)
			for(int c = 0; c<cols && possible; ++c)
			{
				if(matrix[r][c] == '#')
				{
					if(r == rows-1 || c == cols-1)
					{
						possible = false;
						continue;
					}
					if(matrix[r][c+1] != '#' ||
						matrix[r+1][c] != '#' ||
						matrix[r+1][c+1] != '#')
					{
						possible = false;
						continue;
					}
					matrix[r][c] = matrix[r+1][c+1] = '/';
					matrix[r][c+1] = matrix[r+1][c] = '\\';

				}
			}
		if(!possible)
			f2<<"Impossible\n";
		else
		{
			for(int r = 0; r<rows; ++r)
			{
				for(int c = 0; c<cols; ++c)
					f2<<(char)(matrix[r][c]);
				f2<<"\n";
			}
		}
	}

	return 0;
}