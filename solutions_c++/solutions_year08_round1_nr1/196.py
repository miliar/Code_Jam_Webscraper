#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out.txt");

int n;
int m;
__int64 ans;

int x[1024], y[1024];

int compare(const void *a, const void *b)
{
	if ((*(int *) a) > (*(int *) b)) return 1;
	if ((*(int *) a) < (*(int *) b)) return -1;
	return 0;
}

int main()
{
	fin >> n;
	for (int cases = 0; cases < n; cases++)
	{
		fin >> m;
		for (int i = 0; i < m; i++) fin >> x[i];
		for (int i = 0; i < m; i++) fin >> y[i];

		qsort((void *)x, m, sizeof(int), compare);
		qsort((void *)y, m, sizeof(int), compare);

		ans = 0;
		for (int i = 0; i < m; i++)
		{
			int j = m - i - 1;

			ans += ((__int64) x[i]) * ((__int64) y[j]);
		}


		fout << "Case #" << cases + 1 << ": " << ans << endl;
	}

	return 0;
}