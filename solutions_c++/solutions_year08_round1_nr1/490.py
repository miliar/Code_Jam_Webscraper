#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream fin ("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");

	int i,j;
	int n,cases;
	vector<int> x,y;
	int s,t;
	fin>>n;
	for(cases = 1; cases <= n; cases++)
	{
		x.clear();
		y.clear();
		fin>>s;
		for(i=0;i<s;i++)
		{			
			fin>>t;
			x.push_back(t);
		}
		for(i=0;i<s;i++)
		{			
			fin>>t;
			y.push_back(t);
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		reverse(y.begin(),y.end());
		int re = 0;
		for(i=0;i<x.size();i++)
			re += x[i]*y[i];
		fout<<"Case #"<<cases<<": "<<re<<endl;
	}
}
