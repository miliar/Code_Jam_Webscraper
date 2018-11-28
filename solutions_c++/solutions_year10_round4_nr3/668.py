#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("C.in", ios_base::in);
	ofstream fout("C.out", ios_base::out);

	int c;
	fin >> c;
	for (int count = 1; count <= c; ++count)
	{
		long result = 0;
		int r;
		fin >> r;
		bool map[2][101][101];
		int maxx = 0, maxy = 0;
		bool which = 0;

		for (int i = 0; i != 100; ++i)
		{
			for (int j = 0; j != 100; ++j)
				map[0][i][j] = map[1][i][j] = false;
		}
		for (int i = 0; i != r; ++i)
		{
			int x1, x2, y1, y2;
			fin >> x1 >> y1 >> x2 >> y2;
			maxx = (maxx > x2) ? maxx : x2;
			maxy = (maxy > y2) ? maxy : y2;
			for (int j = x1; j <= x2; ++j)
				for (int k = y1; k <= y2; ++k)
					map[which][j][k] = true;
		}


		while (true)
		{
			bool flag = false;
			++result;
			for (int i = 1; i <= maxx; ++i)
				for (int j = 1; j <= maxy; ++j)
				{
					map[!which][i][j] = map[which][i][j];
					if (map[which][i - 1][j] && map[which][i][j - 1])
						map[!which][i][j] = true;
					if (!map[which][i - 1][j] && !map[which][i][j - 1])
						map[!which][i][j] = false;
					if (map[!which][i][j]) flag = true;
				}
			if (!flag) break;
			which = !which;
		}
		fout << "Case #" << count << ": " << result << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
