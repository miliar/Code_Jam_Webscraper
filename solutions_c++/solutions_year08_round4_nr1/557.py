#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin("c:\\codejam\\gate4.txt");
	ofstream fout("c:\\codejam\\gate_out.txt");
	int num_cases;
	fin >> num_cases;
	for (int p=0; p<num_cases; p++)
	{
		int m, goal;
		fin >> m >> goal;
		int g[50000], ch[50000];
		int x[50000][2];

		for (int i=0; i<(m - 1) / 2; i++)
		{
			fin >> g[i] >> ch[i];
		}
		for (int i=(m-1)/2; i<m; i++)
		{
			fin >> ch[i];
			if (ch[i] == 0)
			{
				x[i][0] = 0;
				x[i][1] = 1000000;
			}
			else
			{
				x[i][0] = 1000000;
				x[i][1] = 0;
			}
		}

		for (int i=(m-1)/2 - 1; i>=0; i--)
		{
			x[i][0] = 1000000;
			x[i][1] = 1000000;
			int p = i * 2 + 1;
			int q = i * 2 + 2;
			{
				int a = x[p][1] + x[q][1];
				int b = x[p][0] + x[q][0];
				int c = x[p][1] + x[q][0];
				int d = x[p][0] + x[q][1];

				int a1 = b;
				if (c < a1) a1 = c;
				if (d < a1) a1 = d;
				int b1 = a;
				int c1 = b;
				int d1 = a;
				if (c < d1) d1 = c;
				if (d < d1) d1 = d;

				if (g[i] == 1)
					if (a1 < x[i][0]) x[i][0] = a1;
				if (g[i] == 1)
					if (b1 < x[i][1]) x[i][1] = b1;
				if (g[i] == 0)
					if (c1 < x[i][0]) x[i][0] = c1;
				if (g[i] == 0)
					if (d1 < x[i][1]) x[i][1] = d1;

				if (g[i] == 0 && ch[i] == 1)
					if (a1 + 1< x[i][0]) x[i][0] = a1 + 1;
				if (g[i] == 0 && ch[i] == 1)
					if (b1 + 1< x[i][1]) x[i][1] = b1 + 1;
				if (g[i] == 1 && ch[i] == 1)
					if (c1 + 1< x[i][0]) x[i][0] = c1 + 1;
				if (g[i] == 1 && ch[i] == 1)
					if (d1 + 1 < x[i][1]) x[i][1] = d1 + 1;
			}
		}

		int ans = x[0][goal];
		if (ans >= 1000000)
		{
			fout << "Case #" << p + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			fout << "Case #" << p + 1 << ": " << ans << endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}