#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> T;
	for(int ca=0;ca<T;ca++)
	{
		int n,sum=0,xor=0;
		fin >> n;
		vector <int> nrs;
		for(int i=0;i<n;i++)
		{
			int temp;
			fin >> temp;
			xor^=temp;
			sum+=temp;
			nrs.push_back(temp);
		}
		sort(nrs.begin(),nrs.end());
		fout << "Case #" << ca+1 << ": ";
		if (xor==0)
			fout << sum-nrs[0] << "\n";
		else
			fout << "NO\n";

	}
	return 0;
}