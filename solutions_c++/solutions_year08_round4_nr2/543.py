#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin("c:\\codejam\\area1.txt");
	ofstream fout("c:\\codejam\\area_out.txt");
	int num_cases;
	fin >> num_cases;
	for (int p=0; p<num_cases; p++)
	{
		int n, m, a;
		fin >> n >> m >> a;

		bool o = false;
		for (int bx=0; bx<=n; bx++)
		{
			for (int cy=0; cy<=m; cy++)
			{
				for (int cx=0; cx<=n; cx++)
				{
					int s = bx * cy - a;
					if (s < 0)
					{
						continue;
					}
					if (cx == 0 && s != 0)
					{
						continue;
					}
					if (cx != 0 && s % cx != 0)
					{
						continue;
					}
					int by;
					if (cx == 0)
					{
						by = 1;
					}
					else
					{
						by = s / cx;
					}
					fout << "Case #" << p + 1 << ": " << "0 0 " << bx << " " << by << " " << cx << " " << cy << endl;
					o = true;
					break;
				}
				if (o) break;
			}
			if (o) break;
		}
		if (!o)
		{
			fout << "Case #" << p + 1 << ": " << "IMPOSSIBLE" << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}