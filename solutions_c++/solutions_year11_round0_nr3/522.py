#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

ifstream inf;
ofstream outf;
	

int main(void){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;
	for (int test = 0; test < tests; test++)
	{		
		int n;
		int mn = 100000000;
		int sum = 0, xsum = 0;
		inf >> n;
		for (int i = 0; i < n; i ++)
		{
			int a;
			inf >> a;
			mn = min(a, mn);
			sum +=a;
			xsum ^= a;
		}
		outf << "Case #" << test+1 << ": ";
		if (xsum)
			outf << "NO\n";
		else
			outf << sum - mn << endl;
	}

	outf.close();
	return 0;
}
