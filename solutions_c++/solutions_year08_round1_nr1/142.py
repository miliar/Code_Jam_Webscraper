#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream fin("c:\\codejam\\scalar1.txt");
	ofstream fout("c:\\codejam\\scalar_out.txt");
	int num_cases;
	fin >> num_cases;
	for (int p=0; p<num_cases; p++)
	{
		int n;
		fin >> n;
        int x[1000], y[1000];
        for (int i=0; i<n; i++)
		{
			fin >> x[i];
		}
        for (int i=0; i<n; i++)
		{
			fin >> y[i];
		}
		for (int i=0; i<n; i++)
		{
			for (int j=i+1; j<n; j++)
			{
				if (x[i] > x[j])
				{
					int tmp = x[i]; x[i] = x[j]; x[j] = tmp;
				}
			}
		}
		for (int i=0; i<n; i++)
		{
			for (int j=i+1; j<n; j++)
			{
				if (y[i] < y[j])
				{
					int tmp = y[i]; y[i] = y[j]; y[j] = tmp;
				}
			}
		}
		_int64 ans = 0;
		for (int i=0; i<n; i++)
		{
			ans = ans + x[i] * y[i];
		}

		fout << "Case #" << p + 1 << ": " << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}