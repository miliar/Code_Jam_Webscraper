#include<fstream>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<functional>
#include<numeric>
using namespace std;
typedef long long ll;

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");

	int dX[256][2], dY[256][2];
	int num[4][4];

	memset(dX, 0, sizeof(dX));
	memset(dY, 0, sizeof(dY));

	dY['|'][0] = -1; dY['|'][1] = 1;
	dX['-'][0] = -1; dX['-'][1] = 1;

	dX['/'][0] = dY['/'][1] = -1;
	dX['/'][1] = dY['/'][0] = 1;

	dX['\\'][0] = dY['\\'][0] = -1;
	dX['\\'][1] = dY['\\'][1] = 1;

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int R,C;
	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> R >> C;
		vector<string> v(R);
		for (int i=0; i<R; ++i)
			fin >> v[i];

		int result = 0;
		int numTries = (1<<(R*C));
		for (int mask=0; mask < numTries; ++mask)
		{
			memset(num,0,sizeof(num));
			for (int y=0; y<R; ++y)
			{
				for (int x=0; x<C; ++x)
				{
					char c = v[y][x];
					int shift = y*C + x;
					int idx = ((1<<shift) & mask) == 0 ? 0 : 1;
					int newX = (x + C + dX[c][idx]) % C;
					int newY = (y + R + dY[c][idx]) % R;

					++num[newY][newX];
				}
			}

			bool OK = true;
			for (int y=0; y<R; ++y)
			{
				for (int x=0; x<C; ++x)
				{
					if (num[y][x] != 1)
						OK = false;
				}
			}
			if (OK) ++result;
		}

		fout << "Case #" << zz << ": " << result << endl;
	}

	return 0;
}