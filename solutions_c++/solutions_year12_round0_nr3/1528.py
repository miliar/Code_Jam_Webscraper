#include <iostream>
#include <fstream>
#include <set>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int a, b, k;
set<int> st;

int len(int n)
{
	int l =0;
	while(n>0)
	{
		l++;
		n/=10;
	}
	return l;
}

int count(int n)
{
	int i,l;
	int d=1;
	st.clear();
	for(i=0; i<k; ++i)
		d*=10;

	for(i=1,l=10; i<k; ++i, l*=10)
	{
		int m = n;
		int mnac = m%l;
		if(mnac < l/10)
			continue;

		m/=l;
		m = mnac * (d/l) + m;
		if(m>n && m<=b)
			st.insert(m);
	}
	return st.size();
}

int main()
{
	int t, i, j,s;
	fin>>t;
	for(j=1; j<=t; ++j)
	{
		fout<<"Case #"<<j<<": ";
		s=0;
		fin>>a>>b;
		k = len(a);
		for(i=a; i<b; ++i)
			s+=count(i);
		fout<<s<<endl;
	}
	return 0;
}