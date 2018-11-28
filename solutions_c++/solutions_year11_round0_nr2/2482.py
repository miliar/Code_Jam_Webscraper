#include <algorithm>
#include <iterator>
#include <iostream>
#include <fstream>
#include <sstream>
#include <bitset>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>

#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <ctime>

using namespace std;



class Comb
{
	map< pair< char, char >, char > mas;

public:
	void Insert(char u, char v, char w)
	{
		if (u > v) swap(u, v);
		mas[make_pair(u, v)] = w;
	}

	char Find(char u, char v)
	{
		if (u > v) swap(u, v);
		return mas[make_pair(u, v)];
	}
};


class Opp
{
	map< char, set< char > > mas;

public:
	void Insert(char u, char v)
	{
		mas[u].insert(v);
		mas[v].insert(u);
	}

	bool Find(const string &s, char u)
	{
		set< char > &p = mas[u];
		for (size_t i = 0; i < s.length(); ++i)
		{
			if (p.find(s[i]) != p.end())
				return true;
		}
		return false;
	}
};


void Solve(istream &in, ostream &out)
{
	int c;
	in >> c;
	Comb comb;
	while (c--)
	{
		char u, v, w;
		in >> u >> v >> w;
		comb.Insert(u, v, w);
	}

	int d;
	in >> d;
	Opp opp;
	while (d--)
	{
		char u, v;
		in >> u >> v;
		opp.Insert(u, v);
	}

	int n;
	in >> n;
	string res;
	while (n--)
	{
		char tmp;
		in >> tmp;

		char u = 0;
		if (!res.empty() && (u = comb.Find(tmp, res.back())))
			res.back() = u;
		else if (opp.Find(res, tmp))
			res.clear();
		else
			res += tmp;
	}

	out << '[';
	for (size_t i = 0; i + 1 < res.length(); ++i)
	{
		out << res[i] << ", ";
	}
	if (!res.empty())
		out << res.back();
	out << ']';
}


int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t;
	fin >> t;
	for (int cnt = 1; cnt <= t; ++cnt)
	{
		fout << "Case #" << cnt << ": ";
		Solve(fin, fout);
		fout << endl;
	}

	return 0;
}