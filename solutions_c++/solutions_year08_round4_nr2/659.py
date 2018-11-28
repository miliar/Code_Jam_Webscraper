#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;

ifstream fin("B-small.in");
ofstream fout("B-small.out");


int m,n,a;

void solve()
{
	fin >> n >> m >> a;
	for (int x1=0; x1<=n; ++x1)
		for (int y1=0; y1<=m; ++y1)
			for (int x2=0; x2<=n; ++x2)
				for (int y2=0; y2<=m; ++y2)
				    if (abs(x1*y2-y1*x2)==a)
				    {
						fout << "0 0 " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
						return;
					}
	fout << "IMPOSSIBLE" << endl;
}

int main()
{
	int tc;
	fin >> tc;
	for (int i = 1; i <= tc; ++i)
	{
		fout << "Case #" << i << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}
