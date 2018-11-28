#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ofstream outf;
	outf.open("1c1.out",ios::out);
	int t;
	int k;
	cin >> t;
	int i,j;
	for (k = 1;k <= t;k++)
	{
		int r, c;
		cin >> r >> c;
		char m[50][50];
		for (i = 0;i < r;i++)
		{
			for (j = 0;j < c;j++)
			{
				cin >> m[i][j];
			}
		}

		for (i = 0;i < r;i++)
		{
			for (j = 0;j < c;j++)
			{
				if (m[i][j] == '#')
				{
					if (m[i+1][j] == '#' && m[i][j+1] == '#' && m[i+1][j+1] == '#')
					{
						m[i][j] = m[i+1][j+1] = '/';
						m[i+1][j] = m[i][j+1] = '\\';
					}
				}
			}
		}

		bool flag = true;
		for (i = 0;i < r;i++)
		{
			for (j = 0;j < c;j++)
			{
				if (m[i][j] == '#')
					flag = false;
			}
		}
		outf <<"Case #"<< k << ":" << endl;
		if (flag)
		{
			for (i = 0;i < r;i++)
			{
				for (j = 0;j < c;j++)
				{
					outf << m[i][j];
				}
				outf << endl;
			}
		}
		else
			outf << "Impossible"<<endl;
	}
	return 0;
}



