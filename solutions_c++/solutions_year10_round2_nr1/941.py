#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;

int N,M;
set<string> S;

int main()
{
	int test,i,j,k;
	string s;
	ofstream fout ("A-large.out");
	ifstream fin ("A-large.in");
	fin >> test;
	for (i=0;i<test;i++)
	{
		fin >> N >> M;
		S.clear();
		S.insert("");
		for (j=0;j<N;j++)
		{
			fin >> s;
			s=s+'/';
			for (k=0;k<s.size();k++)
				if (s[k]=='/')
				{
					string s2;
					s2=s.substr(0,k);
					S.insert(s2);
				}
		}
		int result=0;
		for (j=0;j<M;j++)
		{
			fin >> s;
			s=s+'/';
			for (k=0;k<s.size();k++)
				if (s[k]=='/')
				{
					string s2;
					s2=s.substr(0,k);
					if (!S.count(s2))
					{
						result++;
						S.insert(s2);
					}
				}
		}
		fout << "Case #" << i+1 <<": " << result << endl;
	}
	return 0;
}