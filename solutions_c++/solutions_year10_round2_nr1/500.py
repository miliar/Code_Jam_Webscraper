#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for(int cases=0;cases<t;cases++)
	{
		int n,m;
		fin >> n >> m;
		char a[103]={'.'};
		fin.getline(a,sizeof(a));
		map <string,bool> have;
		for(int i=0;i<n;i++)
		{
			char b[103]={'.'};
			fin.getline(b,sizeof(b));
			int j=1;
			string s="";
			s+=b[0];
			while (b[j]!=0)	
			{
				if (b[j]=='/')
				{
					if (have.find(s)==have.end())
						have.insert(make_pair(s,true));
				}
				s+=b[j];
				j++;
			}
			have.insert(make_pair(s,true));
		}
		map <string,bool> dont_have;
		int size=0;
		for(int i=0;i<m;i++)
		{
			char b[103]={'.'};
			fin.getline(b,sizeof(b));
			int j=1;
			string s="";
			s+=b[0];
			while (b[j]!=0)	
			{
				if (b[j]=='/')
				{
					if (dont_have.find(s)==dont_have.end())
					{
						dont_have.insert(make_pair(s,true));
						size++;
					}
				}
				s+=b[j];
				j++;
			}
			dont_have.insert(make_pair(s,true));
			size++;
		}
		string dir="";
		int count =0;
		for(map <string,bool> ::iterator it=dont_have.begin();it!=dont_have.end();it++)
		{
			dir=(*it).first;
			if (have.find(dir)==have.end())
				count++;
		}
		fout << "Case #" << cases+1 << ": " << count << endl;
	}
}