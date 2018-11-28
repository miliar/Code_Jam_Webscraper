#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;
int main()
{
	int t,n,s,p,k,S,C,q,r;
	vector <int> a;
	ifstream fin("input.in");
	ofstream fout("output.out");
	fin>>t;
	for(int i =0;i<t;i++)
	{
		C = 0;
		S = 0;
		fin>>n;
		fin>>s;
		fin>>p;
		for(int j =0;j<n;j++)
		{
			fin>>k;
			if(k>27)
				C++;
			else if(k<2)
			{	
				if(k>=p)
					C++;
			}
			else
			{
				q = k/3;
				r = k%3;
				if(r==0)
				{
					if(q >= p)
						C++;
					else if(q+1 == p)
						S++;
				}
				if(r==1)
				{
					if(q+1 >= p)
						C++;
				}
				if(r==2)
				{
					if(q+1 >= p)
						C++;
					else if(q+2 == p)
						S++;
				}
			}
		}
		C = C+min(s,S);
		fout<<"Case #"<<i+1<<": "<<C<<endl;
	}
	return 0;

}




