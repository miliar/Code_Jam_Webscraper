#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

//5.5 9.5 3 3

double
solve(int d, std::vector<int> &conf)
{
	double begin_orig = 0;
	double begin = 0;

	double end_orig = 0;
	double end = 0;

	std::vector<int> diff;

	for (auto iter = conf.begin();
	     iter != conf.end();
	     ++iter)
	{
		int p = *iter;

		if (iter == conf.begin())
		{
			begin_orig = end_orig = p;
			begin = end = p;
			continue;
		}

		if (end + d <= p) /* enough space */
		{
			end_orig = p;
			end = p;
		}
		else
		{
			end_orig = p;
			end = end + d;

			/* calib */
			double diff = ((end - end_orig) + (begin - begin_orig)) / 2.0;
			end -= diff;
			begin -= diff;
		}
	}

	cout << begin << " " << end << " " << begin_orig << " " << end_orig << endl;
	//
	if (fabs(begin - begin_orig) - fabs(end - end_orig) >= 0.0001)
		cout << "error" << endl;

	return fabs(begin - begin_orig);
}

typedef std::vector<std::vector<char>> tilemap;

tilemap &
solve(int rows, int columns, tilemap &in)
{
	for (int i = 0; i+1 < rows; ++i)
		for (int j = 0; j+1 < columns; ++j)
		{
			if (in[i][j] == '#' && in[i+1][j] == '#'
			    && in[i][j+1] == '#' && in[i+1][j+1] == '#')
			{
				in[i][j] = '/';
				in[i+1][j] = '\\';
				in[i][j+1] = '\\';
				in[i+1][j+1] = '/';
			}
		}

	return in;
}

bool
check(int rows, int columns, tilemap &in)
{
	for (int i = 0; i < rows; ++i)
		for (int j = 0; j < columns; ++j)
			if (in[i][j] == '#')
				return false;
	return true;
}

void
run_test(int test_id)
{
	int rows, columns;
	scanf("%d", &rows);
	scanf("%d", &columns);

	tilemap tm;

	for (int i = 0; i < rows; ++i)
	{
		tm.push_back(std::vector<char>());
		for (int j = 0; j < columns; ++j)
		{
			while (1)
			{
				int ch = getchar();
				if (ch == '.' || ch == '#')
				{
					tm[i].push_back(ch);
					break;
				}
			}
		}
	}

	solve(rows, columns, tm);

	printf("Case #%d:\n", test_id);

	if (!check(rows, columns, tm))
	{
		printf("Impossible\n");
	}
	else
	{
		/* print result */
		for (int i = 0; i < rows; ++i)
		{
			for (int j = 0; j < columns; ++j)
			{
				printf("%c", tm[i][j]);
			}
			printf("\n");
		}
	}

	/* do not free result, its ok, it will freed by process termination. */
}


int
main(int argc, char **argv)
{
	int n_tests = 0;
	scanf("%d", &n_tests);
	for (int i = 0; i < n_tests; ++i)
		run_test(i+1);
	return 0;
}

