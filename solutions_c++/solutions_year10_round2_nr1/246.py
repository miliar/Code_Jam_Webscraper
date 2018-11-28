#include<set>
#include<cstdio>
#include<vector>
#include<string>
#include<fstream>
#include<iostream>
using namespace std;

ifstream in("plik.in");
ofstream out("plik.out");
int N, M;

set<string> zbior;

vector<string> rozbij(string s)
{
	vector<string> ret;

	string akt = "/";

	if (s.size() && s[s.size() - 1] != '/') s += '/';

	for(int i = 1; i < s.size(); ++i)
	{
		akt += s[i];
		if(s[i] == '/')
		{
			ret.push_back(akt);
			//cout << akt << "\n";
		}
	}
	return ret;
}

int lecim()
{
	zbior.clear();
	string akt;
		
	in >> N >> M;
	for(int i = 0; i < N; ++i)
	{
		in >> akt;
		vector<string> ziom = rozbij(akt);
		for(int j = 0; j < ziom.size(); ++j) zbior.insert(ziom[j]);
	}
	int ret = 0;
	for(int i = 0; i < M; ++i)
	{
		in >> akt;
		vector<string> ziom = rozbij(akt);
		for(int j = 0; j < ziom.size(); ++j)
			if(!zbior.count(ziom[j]))
			{
					zbior.insert(ziom[j]);
					++ret;
			}
	}
	return ret;
}
	
int main()
{
	int t;
	in >> t;
	for(int i = 1; i <= t; ++i)
	{
		out << "Case #" << i << ": " << lecim() << "\n";
	}
	in.close();
	out.close();
	return 0;
}