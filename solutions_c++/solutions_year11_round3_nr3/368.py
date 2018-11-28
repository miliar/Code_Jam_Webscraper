#include <iostream>
#include <fstream>
#include <string>

using namespace std;

const int MAX = 10 * 1000;;

int a[MAX];

int main()
{
	ofstream fout ("C-small-attempt0.out");
	ifstream fin ("C-small-attempt0.in");

	int t, tt;
	fin >> t;
	tt = t;
	while(t --> 0)
	{
		bool c = true;
		int n, l, h;
		fin >> n >> l >> h;
		for(int i = 0; i < n; i++)
			fin >> a[i];
		for(int i = l; i <= h; i++)
		{
			bool b = true;
			for(int j = 0; j < n && b; j++)
				if(i % a[j] && a[j] % i)
					b = false;
			if(!b)
				continue;
			fout << "Case #" << tt - t << ": " << i << endl;
			c = false;
			break;
		}
		if(c)
			fout << "Case #" << tt - t << ": NO" << endl;

	}
	return 0;
}
