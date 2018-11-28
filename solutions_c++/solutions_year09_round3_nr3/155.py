#include <iostream>
#include <fstream>
using namespace std;

int list[200];
int f[200][200];
int t, tt;
int p, q;

ifstream ifs;
ofstream ofs;

int min(int a, int b)
{
	if (a <= b) return a; else return b;
}
void work()
{
	int i, j, k;
	
	ifs >> p >> q;
	list[0] = 0;
	for (i = 1; i <= q; ++i)
		ifs >> list[i];
	list[q + 1] = p + 1;
	
	for (i = 0; i < 200; ++i)
		for (j = 0; j < 200; ++j)
			if (i <= j) f[i][j] = 100000000; else f[i][j] = 0;
	for (i = 1; i <= q; ++i)
		f[i][i] = list[i + 1] - list[i - 1] - 2;
	
	for (i = 2; i <= q; ++i)
		for (j = 1; j <= q - i + 1; ++j)
			for (k = 1; k <= i; ++k)
				f[j][j + i - 1] = min(f[j][j + i - 1], f[j][j + k - 2] + f[j + k][j + i - 1] + list[j + i] - list[j - 1] - 2);
	
	ofs << "Case #" << (tt + 1) << ": " << f[1][q] << endl;
}

int main()
{
	ifs.open("r13.in");
	ofs.open("r13.out");
	ifs >> t;
	for (tt = 0; tt < t; ++tt)
		work();
	ifs.close();
	ofs.close();
}