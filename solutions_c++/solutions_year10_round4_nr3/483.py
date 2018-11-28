#include <iostream>
#include <vector>

using namespace std;

const int sz = 110;

typedef vector<int> vint;
vector<vint> mat, amat;

int main()
{
	for (int j = 0; j < sz; ++j)
	{
		mat.push_back(vint(sz));
		amat.push_back(vint(sz));
	}

	
	int tc;
	cin >> tc;
	for (int cn = 1; cn <= tc; ++cn)
	{
		int r;
		cin >> r;

		for (int x = 0; x < sz; ++x)
		for (int y = 0; y < sz; ++y)
			mat[x][y] = amat[x][y] = 0;

		for (int j = 0; j < r; ++j)
		{
			int x1, y1, x2, y2;

			cin >> x1 >> y1 >> x2 >> y2;

			for (int x = x1; x <= x2; ++x)
			for (int y = y1; y <= y2; ++y)
				mat[x][y] = 1;
		}

		int ret = 0;
		while (1)
		{
			for (int x = 0; x < sz; ++x)
			for (int y = 0; y < sz; ++y)
				amat[x][y] = 0;

			int cnt = 0;
			for (int x = 0; x < sz; ++x)
			for (int y = 0; y < sz; ++y)
			{
				int nx = ((x-1) + sz) % sz;
				int ny = ((y-1) + sz) % sz;

				if (mat[x][y] == 0)
				{
					if (mat[x][ny] == 1 && mat[nx][y] == 1)
					{
						++cnt;
						amat[x][y] = 1;
					}
				}
				else
				{
					if (mat[x][ny] == 1 || mat[nx][y] == 1)
					{
						++cnt;
						amat[x][y] = 1;
					}
				}
			}

			++ret;
			if (cnt == 0) break;
			swap(mat,amat);
		}

		cout << "Case #" << cn << ": " << ret << endl;
	}

	return 0;
}
