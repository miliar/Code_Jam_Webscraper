#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("B.in", ios_base::in);
	ofstream fout("B.out", ios_base::out);

	int c;
	fin >> c;
	for (int count = 0; count != c; ++count)
	{
		int result = 0;
		int n, k, t;
		long b;
		fin >> n >> k >> b >> t;
		long x[n], v[n];
		long time[n];

		for (int i = 0; i != n; ++i)
			fin >> x[i];
		for (int i = 0; i != n; ++i)
		{
			fin >> v[i];
			time[i] = ((b - x[i]) % v[i] == 0) ? ((b - x[i]) / v[i]) : ((b - x[i]) / v[i] + 1);
		}

		int chicken = 0, pos = -1;
		if (chicken < k)
		{
			for (int i = n - 1; i >= 0; --i)
			{
				if (time[i] <= t)
				{
					++chicken;
					if (pos != -1)
					{
						result += pos - i;
						--pos;
					}
					if (chicken >= k) break;
				}
				else
				{
					if (pos == -1) pos = i;
				}
			}
		}

		fout << "Case #" << (count + 1) << ": ";
		if (chicken >= k) fout << result;
		else fout << "IMPOSSIBLE";
		fout << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
