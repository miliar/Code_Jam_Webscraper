#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ofstream fout ("B-large.out");
	ifstream fin ("B-large.in");
	int tests;
	fin >> tests;
	for(int test = 0; test < tests; test++)
	{
		bool d[256][256] = {0};
		int c[256][256] = {0};
		int n, m, l;
		string s;
		char t;
		fin >> n;
		for(int i = 0; i < n; i++)
		{	string a; fin >> a; c[a[0]][a[1]] = c[a[1]][a[0]] = a[2];	}
		fin >> m;
		for(int i = 0; i < m; i++)
		{	string a; fin >> a; d[a[0]][a[1]] = d[a[1]][a[0]] = 1;	}
		fin >> l;
		for(int i = 0; i < l; i++)
		{
			fin >> t;
			bool b = true;
			if(s.empty())
			{	s += t; continue;	}
			if(c[t][s[s.size() - 1]])
			{	s[s.size() - 1] = c[t][s[s.size() - 1]]; continue;	}
			for(int j = 0; j < s.size(); j++)
				if(d[t][s[j]])
				{	s = ""; b = false; break;	}
			if(b)
				s += t;
		}
		fout << "Case #" << test + 1 << ": [";
		for(int i = 0; i < int(s.size() - 1); i++)
			fout << s[i] << ", ";
		if(!s.empty())
			fout << s[s.size() - 1] << ']' << endl;
		else
			fout << ']' << endl;
	}
	return 0;
}
