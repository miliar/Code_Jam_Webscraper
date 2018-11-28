#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("A.in");
	ofstream fout ("A.out");
	int cases;
	fin >> cases;
	for (unsigned int cas = 0; cas < cases; cas++)
	{
		unsigned int n;
		fin >> n;
		vector <int> x(n), y(n);
		for (int i = 0; i < n; i++)
		{
			fin >> x[i];
		};
		for (int i = 0; i < n; i++)
		{
			fin >> y[i];
		};
		sort(x.begin(), x.end());
		sort(y.begin(), y.end());
		int sum = 0;
		for (int i = 0; i < n; i++)
		{;
			sum+= x[i]*y[n-1-i];
		};
		fout << "Case #" << cas + 1<< ": " << sum << endl;
	}
	return 0;
}
		
		
			  
