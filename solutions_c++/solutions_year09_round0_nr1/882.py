#include <iostream>
#include <fstream>
using namespace std;

int l, d, n;
bool hash[550][20][30];
string list[5500];
string test[550];
int res[550];
ifstream ifs;
ofstream ofs;

void readdata()
{
	int i;
	
	ifs.open("qr1.in");
	ifs >> l >> d >> n;
	for (i = 0; i < d; ++i)
		ifs >> list[i];
	for (i = 0; i < n; ++i)
		ifs >> test[i];
	ifs.close();
}

void work()
{
	int i, j, k;
	bool pd;
	
	for (i = 0; i < n; ++i)
		for (j = 0; j < l; ++j)
			for (k = 0; k < 26; ++k)
				hash[i][j][k] = false;
	for (i = 0; i < n; ++i)
		res[i] = 0;
	
	for (i = 0; i < n; ++i)
	{
		j = 0;
		k = 0;
		while (k < test[i].length())
		{
			if (j >= l)
			{
				res[i] = -1;
				break;
			}
			if (test[i][k] == '(')
			{
				++k;
				while (test[i][k] != ')')
				{
					hash[i][j][test[i][k] - 'a'] = true;
					++k;
				}
				++k;
			}
			else 
			{
				hash[i][j][test[i][k] - 'a'] = true;
				++k;
			}
			++j;
		}
		if (j < l) 
			res[i] = -1;
	}
	
	for (i = 0; i < n; ++i)
	{
		if (res[i] != -1)
		{
			for (j = 0; j < d; ++j)
			{
				pd = true;
				for (k = 0; k < l; ++k)
					pd &= hash[i][k][list[j][k] - 'a'];
				if (pd) ++res[i];
			}
		}
	}
}

void print()
{
	int i;
	ofs.open("qr1.out");
	for (i = 0; i < n; ++i)
	{
		if (res[i] == -1) res[i] = 0;
		ofs << "Case #" << (i + 1) << ": " << res[i] << endl;
	}
	ofs.close();
}

int main()
{
	readdata();
	work();
	print();
}
