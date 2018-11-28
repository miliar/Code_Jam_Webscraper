#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;


int main()
{
	ifstream fin("e:\\fl\\in.in");
	ofstream fout("e:\\fl\\out.out");
	int t;
	fin>>t;
	for (int i=0;i<t;i++)
	{
		int n,m;
		fin>>n>>m;
		int res = 0;
		set< string > ss;
		ss.insert(string(""));
		for (int j=0;j<n;j++)
		{
			string s;
			fin>>s;
			for (int h=0;h<=s.size();h++)
				if (h==s.size()||s[h]=='/')
				{
					string q = s.substr(0,h);
					ss.insert(q);
				}
		}
		for (int j=0;j<m;j++)
		{
			string s;
			fin>>s;
			for (int h=0;h<=s.size();h++)
				if (h==s.size()||s[h]=='/')
				{
					string q = s.substr(0,h);
					if (ss.find(q)==ss.end())
					{
						res++;
						ss.insert(q);
					}
				}
		}
		fout<<"Case #"<<(i+1)<<": "<<res<<endl;
	}
	return 0;
}