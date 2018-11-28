#include <fstream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
using namespace std;

bool a[512][512];
int big[512][512];
int result[513];
int M;
int N;

int getSize(int x, int y)
{
	bool base = a[x][y];
	int ret = 1;
	int maxSize = min(M-x, N-y);
	for (int z=1; z<maxSize; ++z)
	{
		if (a[x+z][y+z] != base) return ret;
		for (int i=0; i<z; ++i)
		{
			int dist = (z+i);
			bool exp = ((z+i)%2 > 0) ? (!base) : base;
			if (a[x+i][y+z] != exp || a[x+z][y+i] != exp) return ret;
		}

		++ret;
	}
	return ret;
}

void destroy(int x, int y, int m)
{
	for (int i=0; i<m; ++i)
	{
		for (int j=0; j<m; ++j)
		{
			big[x+i][y+j] = 0;
		}
	}


	for (int z=1; z<m; ++z)
	{
		for (int xb = x-z; xb<x+m; ++xb)
			if (xb>=0 && y-z >= 0)
				big[xb][y-z] = min(big[xb][y-z], z);

		for (int yb = y-z; yb<y+m; ++yb)
			if (yb>=0 && x-z >= 0)
				big[x-z][yb] = min(big[x-z][yb], z);
	}
}

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	int T;
	string s;
	fin >> T; 
	for (int z=1; z<=T; ++z)
	{
		memset(a, 0, sizeof(a));
		memset(result, 0, sizeof(result));
		memset(big, 0, sizeof(big));
		fin >> M >> N;

		for (int i=0; i<M; ++i)
		{
			fin >> s;

			for (int j=0; j<N; ++j)
			{
				char c = s[j/4];
				int bits = (c >= 'A') ? 10 + (c-'A') : (c-'0');
				int comp = 1 << (3-j%4);
				if ((bits & comp) > 0)
					a[i][j] = true;
			}
		}

		int maxSize = 0;
		for (int i=0; i<M; ++i)
		{
			for (int j=0; j<N; ++j)
			{
				big[i][j] = getSize(i,j);
				maxSize = max(maxSize, big[i][j]);
			}
		}

		int ans = 0;
		for (int m = maxSize; m>0; --m)
		{
			for (int i=0; i<M; ++i)
			{
				for (int j=0; j<N; ++j)
				{
					if (big[i][j] == m)
					{
						if (result[m] == 0) ++ans;
						++result[m];
						destroy(i, j, m);
					}
				}
			}
		}
		
		fout << "Case #" << z << ": " << ans << endl;

		int m = 512;
		while (m>0)
		{
			if (result[m] > 0)
				fout << m << " " << result[m] << endl;
			--m;
		}
	}

	return 0;
}