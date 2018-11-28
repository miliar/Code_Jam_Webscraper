#include <iostream>
#include <list>
#include <fstream>
#include <stack>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <ctime>
#include <set>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main(){
	int n;
	fin>>n;
	for (int m=0; m<n; m++)
	{
		int len;
		fin >> len;
		vector<long>v1;
		vector<long>v2;
		for (int i=0; i<len; i++)
		{
			int t ;
			fin >> t;
			v1.push_back(t);
		}
		for(int i=0; i<len; i++)
		{
			int t ;
			fin >> t;
			v2.push_back(t);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		long res = 0;
		for (int i=0; i<len; i++)
		{
			res += v1[i]*v2[len - 1 - i];
		}
		fout << "Case #" << m+1<<": "<<res<<endl;
	}
	return 0;
}