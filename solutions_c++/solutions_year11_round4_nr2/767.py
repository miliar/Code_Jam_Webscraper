#include <iostream>

#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <complex>
#include <cmath>
#include <map>
#include <numeric>
#include <set>
#include <iterator>
#include <bitset>
#include <limits>
#include <cassert>

using namespace std;

typedef complex<int> coor;

int m[512][512];
vector<string> dat;
int R,C,D;

void parseCase(istream &inp)
{
	dat.clear();

	inp >> R >> C >> D;

	for (int j = 0; j < R; ++j)
	{
		string l;
		inp >> l;
		dat.push_back(l);
	}
}

void answer()
{
	for (int r = 0; r < R; ++r)
	for (int c = 0; c < C; ++c)
		m[r][c] = dat[r][c] - '0';

	for (int k = min(R,C); k > 2; --k)
	for (int r = 0; r+k-1 < R; ++r)
	for (int c = 0; c+k-1 < C; ++c)
	{
		coor tcom(r + r+k-1, c + c+k-1), acc(0,0);
		for (int r2 = r; r2 < r+k; ++r2)
		for (int c2 = c; c2 < c+k; ++c2)
		{
			if (
				(r2==r || r2==(r+k-1)) &&
				(c2==c || c2==(c+k-1) )
			   )	continue;
			acc += (2*coor(r2,c2)-tcom) * m[r2][c2];
		}

		if (acc == coor(0,0))
		{
			cout << k;
			return;
		}
	}

	cout << "IMPOSSIBLE";
}

#ifndef ANS_NOMAIN
int main()
{
	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; ++caseNum)
	{
		parseCase(cin);
		cout << "Case #" << caseNum << ": ";
		answer();
		cout << endl;
	}

	return 0;
}
#endif
