/*
Language:C++
*/

#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
	ofstream fout("A-small.out");
	ifstream fin("A-small-attempt1.in");

	int t;
	fin>>t;

	for(int i=0;i!=t;i++)
	{
		int n;
		fin>>n;

		vector<int> x(n,0);
		vector<int> y(n,0);

		for(int j=0;j!=n;j++)
		{
			int xn;
			fin>>xn;

			x[j]=xn;
		}

		for(int k=0;k!=n;k++)
		{
			int yn;
			fin>>yn;

			y[k]=yn;
		}

		sort(x.begin(),x.end());
		sort(y.begin(),y.end());

		int result=0;

		for(int m=0;m!=n;m++)
		{
			int product=x[m]*y[n-m-1];
			result+=product;
		}

		fout<<"Case #"<<i+1<<": "<<result<<endl;
	}

	return 0;
}