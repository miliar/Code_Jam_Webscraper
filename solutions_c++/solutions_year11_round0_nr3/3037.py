#include <iostream>
#include <vector>
#include <set>
#include <fstream>
using namespace std;

ifstream fin("file\\input.txt");
ofstream fout("file\\output.txt");

int main()
{
	int nCases = 0;
	fin >> nCases;
	for(int i = 0; i < nCases; ++ i)
	{
		int n, t, total = 0, diff = 0, minNum = 1e9;
		fin >> n;
		for(int i = 0; i < n; ++ i){
			fin >> t;
			total += t;
			diff ^= t;
			if(minNum > t) minNum = t;
		}
		if(diff){
			fout << "Case #" << i+1 << ": NO" << endl;
		}
		else{
			fout << "Case #" << i+1 << ": "<< total-minNum << endl;
		}
	}
	return 0;
}