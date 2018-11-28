#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
	int m,t,c,i,j,n,a,b;
	vector<int> n1,n2;
	ifstream fin("A-large(2).in");
	ofstream fout("o2.out");
	fin>>t;
	for(m=1;m<=t;m++)
	{
		c=0;
		fin>>n;
		for(i=0;i<n;i++)
		{
			fin>>a>>b;
			n1.push_back(a);
			n2.push_back(b);
		}
		for(i=0;i<n1.size();i++)
		{
			for(j=0;j<n1.size();j++)
			{
				if(i==j) break;
				if((n1[i]<n1[j])&&(n2[i]>n2[j]))
					c++;
				else if((n1[i]>n1[j])&&(n2[i]<n2[j]))
					c++;
			}
		}
		n1.clear();
		n2.clear();
		fout<<"Case #"<<m<<": "<<c<<"\n";
	}
}
