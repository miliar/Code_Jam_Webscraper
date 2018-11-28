#include <fstream>
#include <cmath>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	for(int t=0; t<T; t++)
	{
		int n, m;
		fin >> n >> m;
		char a[100][100];
		for(int i = 0; i<=n; i++)
			for(int j=0; j<=m; j++)
				a[i][j] = '.';
		for(int i = 0; i<n; i++)
			for(int j=0; j<m; j++)
				fin >> a[i][j];
		bool FAIL = false;
		for(int i=0; i<n; i++)
			for(int j=0; j<m; j++)
				if(a[i][j] == '#')
				{
					if(a[i+1][j] == '#' && a[i+1][j+1] == '#' && a[i][j+1] == '#')
					{	
						a[i][j] = '/';
						a[i+1][j] = '\\';
						a[i][j+1] = '\\';
						a[i+1][j+1] = '/';
					}
					else
						FAIL = true;
				}
		fout << "Case #" << t+1 << ": " << endl;
		if(!FAIL)
		for(int i = 0; i<n; i++)
			{
				for(int j=0; j<m; j++)
					fout << a[i][j];
				fout << endl;
			}
		else
		{
			fout << "Impossible" << endl;
		}
	}
	return 0;
}

