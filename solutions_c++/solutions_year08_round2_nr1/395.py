#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int white[3000][3000];

int main()
{
	ifstream fin("c:\\codejam\\crop3.txt");
	ofstream fout("c:\\codejam\\crop_out.txt");
	int num_cases;
	fin >> num_cases;

	for (int p=0; p<num_cases; p++)
	{
		_int64 n, a, b, c, d, x, y, m;
		fin >> n >> a >> b >> c >> d >> x >> y >> m;

		a = a % m;
		b = b % m;
		c = c % m;
		d = d % m;

		_int64 t[3][3];
		memset(t, 0, sizeof(t));

		for (int i=0; i<n; i++)
		{
			x = x % m;
			y = y % m;
			
			t[x % 3][y % 3]++;

			x = a * x + b;
			y = c * y + d;
		}

		_int64 ans = 0;
		for (int i0=0; i0<3; i0++)
			for (int j0=0; j0<3; j0++)
		for (int i1=0; i1<3; i1++)
			for (int j1=0; j1<3; j1++)
		for (int i2=0; i2<3; i2++)
			for (int j2=0; j2<3; j2++)
			{
				if ((i0 + i1 + i2) % 3 == 0 && (j0 + j1 + j2) % 3 == 0)
				{
					if (i0 == i1 && j0 == j1)
					{
						if (i0 == i2 && j0 == j2)
						{
							ans = ans + t[i0][j0] * (t[i1][j1] - 1) * (t[i2][j2] - 2);
						}
						else
						{
							ans = ans + t[i0][j0] * (t[i1][j1] - 1) * t[i2][j2];
						}
					}
					else if (i0 == i2 && j0 == j2)
					{
						ans = ans + t[i0][j0] * (t[i2][j2] - 1) * t[i1][j1];
					}
					else if (i1 == i2 && j1 == j2)
					{
						ans = ans + t[i1][j1] * (t[i2][j2] - 1) * t[i0][j0];
					}
					else
					{
						ans = ans + t[i0][j0] * t[i2][j2] * t[i1][j1];
					}
				}
			}
	
		fout << "Case #" << p + 1 << ": " << ans / 6 << endl;
	}
	fin.close();
	fout.close();
	return 0;
}