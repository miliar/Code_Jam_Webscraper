#include<iostream>
#include<vector>
#include<fstream>
#include<cstdlib>
#include<algorithm>

using namespace std;

long long int scalar_prod(vector<long long int> a, vector<long long int> b);

int main()
{
	int T;
	ifstream fin("A-large.in",ifstream::in);
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		int n;
		fin>>n;
		vector<long long int> a;	
		vector<long long int> b;	
		for(int j=0;j<n;j++)
		{
			long long int num;
			fin>>num;
			a.push_back(num);
		}
		for(int j=0;j<n;j++)
		{
			long long int num;
			fin>>num;
			b.push_back(num);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());

		long long int prod = scalar_prod(a,b);

		cout<<"Case #"<<i<<": "<<prod<<endl;
	}
}

long long int scalar_prod(vector<long long int> a, vector<long long int> b)
{
	long long int prod = 0;
	int index = a.size()-1;
	for(int i=0;i<a.size();i++)
		prod = prod + a[i]*b[index--];
	return prod;
}
