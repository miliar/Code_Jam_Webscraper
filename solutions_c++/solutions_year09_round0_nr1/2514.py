#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <fstream>
using namespace std;
int l,d,n,j,k,count;
string s,st;
vector<set<string> > dict;
vector<vector<string> > exs;
ifstream fin("input.txt");
ofstream fout("output.txt");
void input()
{
	int i;
	fin>>l>>d>>n;
	dict.resize(d);
	exs.resize(n);
	for (i=0;i<d;i++)
	{
		fin>>s;
		st="";
		for (j=0;j<l;j++)
		{
			st+=s[j];
			dict[j].insert(st);
		}
	}
	for (i=0;i<n;i++)
	{
		fin>>s;
		int i1=0;
		for (j=0;j<l;j++)
		{
			st="";
			if (s[i1]=='(')
			{
				i1++;
				while (s[i1]!=')')
				{
					st+=s[i1];
					i1++;
				}
				i1++;
				exs[i].push_back(st);
			}
			else
			{
				st+=s[i1];
				exs[i].push_back(st);
				i1++;
			}
		}
	}
}
void counting(int ni,int li,string s1)
{
	int i;
	if (li==l-1)
	{
		for (i=0;i<exs[ni][li].length();i++)
			if (dict[l-1].find(s1+exs[ni][li][i])!=dict[l-1].end())
				count++;
	}
	else
		for (i=0;i<exs[ni][li].length();i++)
			if (dict[li].find(s1+exs[ni][li][i])!=dict[li].end())
				counting(ni,li+1,s1+exs[ni][li][i]);
}
int main()
{
	input();	
	for (j=0;j<n;j++)
	{
		count=0;
		counting(j,0,"");
		fout<<"Case #"<<j+1<<": "<<count<<endl;
	}	
	return 0;
}