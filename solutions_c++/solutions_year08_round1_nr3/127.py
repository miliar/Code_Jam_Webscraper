#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
	ifstream fin("c:\\codejam\\numbers1.txt");
	ofstream fout("c:\\codejam\\number_out.txt");
	int num_cases;
	fin >> num_cases;

	const int x[29] = {
27,
143,
751,
935,
607,
903,
991,
335,
47,
943,
471,
55,
447,
463,
991,
95,
607,
263,
151,
855,
527,
743,
351,
135,
407,
903,
791,
135,
647};

	for (int p=0; p<num_cases; p++)
	{
		int n;
		fin >> n;
				
		int ans = x[n - 2];
		fout << "Case #" << p + 1 << ": ";
		if (ans < 10)
		{
			fout << "00";
		}
		else if (ans < 100)
		{
			fout << "0";
		}
		fout << ans << endl;
	}
	fin.close();
	fout.close();
	return 0;
}