#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("B-small-attempt1.in.txt");
ofstream fout("B-small-attempt1.out.txt");


int c, n, m, a;
	
bool check(int x1, int y1, int x2, int y2, int x3, int y3)
{
	if (x1 > n || y1 > m || x2 > n || y2 > m || x3 > n || y3 > m)
		return false;
	if (x1 < 0 || y1 < 0 || x2 < 0 || y2 < 0 || x3 < 0 || y3 < 0)
		return false;

	if (labs(x1 * y2 - x2 * y1 + (y1 - y2)*x3 + (x2 - x1) * y3) == a)
		return true;
	return false;
}

int main()
{

	
	int ax, ay, bx, by, cx, cy;
	int x1, y1, x2, y2, x3, y3;

	fin >> c;

	for (int cases = 1; cases <= c; cases ++)
	{
		fin >> n >> m >> a;
		bool ok = false;

		for (x1 = 0; x1 <= n; x1++)
			if (ok == false)
			{
			for (y1 = 0; y1 <= m; y1++)
				if (ok == false)
				{
				for (x2 = x1; x2 <= n; x2++)
					if (ok == false)
					{
						for (y2 = 0; y2 <= m; y2++)
							if (ok == false)
							{
								if (x1 == x2 && y1 == y2) continue;

								if (x1 == x2)
								{
									y3 = 0;
									x3 = labs((a - x1* y2 + x2 * y1) / (y1 - y2));

									if (check(x1, y1, x2, y2, x3, y3) == true)
									{
										ok = true;
										ax = x1; ay = y1;
										bx = x2; by = y2;
										cx = x3; cy = y3;
										break;
									}
								}

								if (y1 == y2)
								{
									x3 = 0;
									y3 = labs( (a - x1 * y2 + x2 * y1) / (x2 - x1) );

									if (check(x1, y1, x2, y2, x3, y3) == true)
									{
										ok = true;
										ax = x1; ay = y1;
										bx = x2; by = y2;
										cx = x3; cy = y3;
										break;
									}
								}

								if (x1 != x2 && y1 != y2)
								{
									for (x3 = x1; x3 <= n; x3++)
									{
										y3 = labs( (a - x1 * y2 + x2 * y1 - (y1 - y2)*x3) / (x2 - x1) );
										if (check(x1, y1, x2, y2, x3, y3) == true)
										{
											ok = true;
											ax = x1; ay = y1;
											bx = x2; by = y2;
											cx = x3; cy = y3;
											break;
										}
									}
									if (ok == true) break;
								}
							}
					}
				}
			}

		if (ok == false)
			fout << "Case #" << cases << ": IMPOSSIBLE" << endl;
		else
			fout << "Case #" << cases << ": " << ax << " " << ay << " " << bx << " " << by << " " << cx << " " << cy << endl;

		cout << cases << endl;
		fout.flush();
	}


	return 0;
}
