#include<iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
using namespace std;

bool cmp(int a, int b)
{
	return a<b;
}
int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int t;
	int l;
	int cut;
	int lowi;
	int a[25];
	char s[25];

	fin >> t;
	fin.get();
	for (int z=1; z<=t; z++)
	{
		fin.getline(s, 25);
		l = strlen(s);
		for (int i=1; i<=l; i++)
		{
			a[i] = s[i-1] - '0';
		}
		a[0] = 0;
		for (i=l; i>0; i--)
			if (a[i] > a[i-1])
			{
				cut = i;
				break;
			}
		lowi = cut;
		for (i=cut + 1; i<=l; i++)
			if ((a[i] > a[cut - 1])&&(a[i] < a[lowi]))
				lowi = i;

		swap(a[cut-1], a[lowi]);
		sort(a+cut, a+l+1, cmp);

		fout << "Case #" << z << ": ";
		if (a[0] != 0)
			fout << a[0];
		for (i=1; i<=l; i++)
			fout << a[i];
		fout << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
