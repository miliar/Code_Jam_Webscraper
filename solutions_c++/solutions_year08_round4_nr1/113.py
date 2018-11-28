#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <cmath>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifs("a.in");
	ofstream ofs("a.out");
	
	int t;
	ifs >> t;
	for (int l = 0; l < t; ++l)
	{
		
		int f[65536][2];
		memset(f, -1, sizeof(f));
		int m, v;
		ifs >> m >> v;
		vector<int> g(m), c(m);
		for (int i = 0; i < (m-1)/2; ++i)
		{
			ifs >> g[i] >> c[i];
		}
		for (int i = 0; i < (m+1)/2; ++i)
		{
			int value;
			ifs >> value;
			f[(m-1)/2+i][value] = 0;
		}
		for (int i = (m-1)/2-1; i >= 0; --i)
		{
			for (int j = 0; j < 2; ++j)
				for (int k = 0; k < 2; ++k)
				{
					int v1 = f[i*2+1][j];
					int v2 = f[i*2+2][k];
					if (v1 != -1 && v2 != -1)
					{
						if (g[i] == 1)
						{
							if (f[i][j & k] == -1 || f[i][j & k] > v1+v2)
							{
								f[i][j&k] = v1+v2;
							}
							if ((f[i][j | k] == -1 || f[i][j | k] > v1+v2+1) && c[i] == 1)
							{
								f[i][j|k] = v1+v2+1;
							}
						}
						else 
						{
							if (f[i][j | k] == -1 || f[i][j | k] > v1+v2)
							{
								f[i][j|k] = v1+v2;
							}
							if ((f[i][j & k] == -1 || f[i][j & k] > v1+v2+1) && c[i] == 1)
							{
								f[i][j&k] = v1+v2+1;
							}

						}
					}
				}
		}
		ofs << "Case #" << l+1 << ": "; 
		if (f[0][v] == -1) ofs << "IMPOSSIBLE\n";
		else ofs << f[0][v] << endl;
	}
  	return 0;
}
