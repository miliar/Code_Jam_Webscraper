#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	fin >> T;
	for(int t=1; t<=T; t++)
	{
		int n, l, h;
		int a[10000];
		fin >> n >> l >> h;
		for(int i = 0; i < n; i++)
			fin >> a[i];
		int ans = -1;
		for(int i=l; i<=h; i++)
		{
			bool b = false;
			for(int j = 0; j<n; j++)
				if(i % a[j] != 0 && a[j] % i != 0)
				{
					b = true;
					break;
				}
			if(!b)
			{
				ans = i;
				break;
			}
		}
		fout << "Case #" << t << ": ";
		if(ans == -1) 
			fout << "NO" << endl;
		else
			fout << ans << endl;
	}
	return 0;
}

