#include <fstream>
#include <cstdlib>
#include <cstring>

using namespace std;

ifstream in("square.in");
ofstream out("square.out");

const int N = 60;

int n, m;
bool td[N][N];
int c[N][N];

bool GTG(int i, int j)
{
	if (!td[i][j] || !td[i][j+1] || !td[i+1][j] || !td[i+1][j+1] || i + 1 > n || j + 1 > m)
		return 0;
	if (c[i][j] || c[i][j+1] || c[i+1][j] || c[i+1][j+1])
		return 0;

	return 1;
}

bool Check()
{
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			if (td[i][j] && !c[i][j])
				return 0;

	return 1;
}

void TryDo()
{
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			if (GTG(i, j))
			{
				c[i][j] = c[i+1][j+1] = 1;
				c[i][j+1] = c[i+1][j] = 2;
			}

	if (Check())
	{
		for (int i = 1; i <= n; ++i, out << "\n")
			for (int j = 1; j <= m; ++j)
			{
				if (c[i][j] == 0)
					out << ".";
				else if (c[i][j] == 1)
					out << "/";
				else
					out << "\\";
			}
	}
	else
		out << "Impossible\n";
}

void SolveCase(int test)
{
	out << "Case #" << test << ":\n";

	in >> n >> m;
	memset(c, 0, sizeof(c));
	memset(td, 0, sizeof(td));

	char ch;
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
		{
			in >> ch;

			if (ch == '#')
				td[i][j] = 1;
			else
				td[i][j] = 0;
		}

	TryDo();
}

int main()
{
	int t;
	in >> t;

	for (int i = 1; i <= t; ++i)
		SolveCase(i);

	return 0;
}
