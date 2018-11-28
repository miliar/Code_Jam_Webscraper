#include <fstream>

typedef unsigned long long ull;
typedef long long ll;

#define FN "gcj1a"

using namespace std;

int main()
{
	ifstream in(FN ".in");
	ofstream out(FN ".out");

	int t;
	in >> t;

	char field[16];

	for(int i = 0; i < t; i++)
	{
		int dc = 0;
		for(int j = 0; j < 16; j++)
		{
			in >> field[j];
			if(field[j] == '.')
				dc++;
		}

		for(int j = 0; j < 4; j++)
		{
			int zs = 0, xs = 0;
			for(int k = 0; k < 4; k++)
			{
				if(field[j+k*4] == 'X')
					xs++;
				else if(field[j+k*4] == 'O')
					zs++;
				else if(field[j+k*4] == 'T')
				{
					xs++;
					zs++;
				}
			}
			if(zs == 4)
			{
				out << "Case #" << i+1 << ": O won";
				goto yes;
			} else if(xs == 4)
			{
				out << "Case #" << i+1 << ": X won";
				goto yes; //because I like GOTOZ;
			}
		}

		for(int j = 0; j < 4; j++)
		{
			int zs = 0, xs = 0;
			for(int k = 0; k < 4; k++)
			{
				if(field[j*4+k] == 'X')
					xs++;
				else if(field[j*4+k] == 'O')
					zs++;
				else if(field[j*4+k] == 'T')
				{
					xs++;
					zs++;
				}
			}
			if(zs == 4)
			{
				out << "Case #" << i+1 << ": O won";
				goto yes;
			} else if(xs == 4)
			{
				out << "Case #" << i+1 << ": X won";
				goto yes; //because I like GOTOZ;
			}
		}

		{
			int zs = 0, xs = 0;
			for(int k = 0; k < 4; k++)
			{
				if(field[k+k*4] == 'X')
					xs++;
				else if(field[k+k*4] == 'O')
					zs++;
				else if(field[k+k*4] == 'T')
				{
					xs++;
					zs++;
				}
			}
			if(zs == 4)
			{
				out << "Case #" << i+1 << ": O won";
				goto yes;
			} else if(xs == 4)
			{
				out << "Case #" << i+1 << ": X won";
				goto yes; //because I like GOTOZ;
			}
		}

		{
			int zs = 0, xs = 0;
			for(int k = 0; k < 4; k++)
			{
				if(field[3-k+k*4] == 'X')
					xs++;
				else if(field[3-k+k*4] == 'O')
					zs++;
				else if(field[3-k+k*4] == 'T')
				{
					xs++;
					zs++;
				}
			}
			if(zs == 4)
			{
				out << "Case #" << i+1 << ": O won";
				goto yes;
			} else if(xs == 4)
			{
				out << "Case #" << i+1 << ": X won";
				goto yes; //because I like GOTOZ;
			}
		}

		out << "Case #" << i+1 << (dc == 0 ? ": Draw": ": Game has not completed");
yes:
		out << "\n";
	}

	out.close();
	return 0;
}