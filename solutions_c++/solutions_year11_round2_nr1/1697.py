#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int MAX = 100;

int a[MAX][MAX];
double wp[MAX];
double owp[MAX];
double oowp[MAX];

int main()
{
	ofstream fout ("A-large.out");
	ifstream fin ("A-large.in");
	int t, tt;
	fin >> t;
	tt = t;
	while(t --> 0)
	{
		int n;
		fin >> n;
		for(int i = 0; i < n; i++)
		{
			string s; fin >> s;
			for(int j = 0; j < n; j++)
				a[i][j] = (s[j] == '.'?0:(s[j] - '0'?1:-1));
		}
		for(int i = 0; i < n; i++)
		{
			int w = 0, l = 0;
			for(int j = 0; j < n; j++)
			{
				if(a[i][j] == 1)
					w++;
				else if(a[i][j] == -1)
					l++;
			}
			wp[i] = double(w) / double(w + l);
		}
		for(int i = 0; i < n; i++)
		{
			double s = 0, c = 0;
			for(int j = 0; j < n; j++)
				if(a[i][j])
				{
					int w = 0, l = 0;
					for(int k = 0; k < n; k++)
						if(a[j][k] && k != i)
						{
							if(a[j][k] == 1)
								w++;
							else if(a[j][k] == -1)
								l++;
						}
					s += double(w) / double(w + l), c++;
				}
			owp[i] = s / c;
		}
		for(int i = 0; i < n; i++)
		{
			double s = 0, c = 0;
			for(int j = 0; j < n; j++)
				if(a[i][j])
					s += owp[j], c++;
			oowp[i] = s / c;
		}
		fout << "Case #" << tt - t << ":" << endl;
		for(int i = 0; i < n; i++)
//			cerr << owp[i] << endl;
			fout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
	}
	return 0;
}
