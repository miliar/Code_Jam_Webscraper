#include<iostream>
#include<fstream>
#include<sstream>
#include<iomanip>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;

string A_FILE_NAME = "A-small-attempt0";

void sort(int* a, const int b)
{
	for(int i=b-1; i>=0; --i)
	{
		for(int j=i;j<b-1; ++j)
		{
			if(a[j] > a[j+1])
			{
				int temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}
		}
	}
}

int fa(int* a, int* b, int m)
{
	int res = 0;
	sort(a, m);
	sort(b, m);
	for(int i=0; i<m; ++i)
	{
		res += a[i] * b[m-i-1];
	}
	return res;
}

int main()
{
	string FileIn = "D:/" + A_FILE_NAME + ".in";
	string FileOut = "D:/" + A_FILE_NAME + ".out";
	ifstream infile(FileIn.c_str());
	int n;
	infile >> n;

	ofstream outfile(FileOut.c_str());
	for(int i=0; i<n; ++i)
	{
		int m;
		infile >> m;
		int *a = new int[m];
		for(int j=0; j<m; ++j)
		{
			infile>>a[j];
		}
		int *b = new int[m];
		for(int j=0; j<m; ++j)
		{
			infile >>b[j];
		}
		int out = fa(a,b,m);

		outfile << "Case #" << (i+1) << ": " << out << endl;
//		outfile << setiosflags(ios::fixed) << setprecision(6) << "Case #" << (i+1) << ": " << out << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
