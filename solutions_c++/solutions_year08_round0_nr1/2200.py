#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <fstream>
#include <sstream>
#include <string>
#include <utility>
#include <set>

#include <iostream>

using namespace std;

ifstream in("A-large.in");
ofstream out("A-large.out");

vector <string> e, v;
int s, q;

int C;

void get_input()
{
	string t;

	e.clear();
	v.clear();
	C = 0;

	in >> s;
	in.ignore(1024, '\n');

	for (int i = 0; i < s; i++)
	{
		getline(in, t);
		e.push_back(t);
	}

	in >> q;
	in.ignore(1024, '\n');

	for (int i = 0; i < q; i++)
	{
		getline(in, t);
		v.push_back(t);
	}
}

int get_length(string s)
{
	for (int i = C; i < (int) v.size(); i++)
		if (v[i] == s)
			return i;

	return (int) v.size();
}

int process()
{
	int r = 0;

	while (C < (int) v.size())
	{
		int m = get_length(e[0]);
		for (int i = 0; i < (int) e.size(); i++)
			m = max(m, get_length(e[i]));

		if (m == (int) v.size())
			return r;

		C = m;

		r++;
	}

	return r;
}

int main()
{
	int n;

	in >> n;

	for (int i = 1; i <= n; i++)
	{
		get_input();
		out << "Case #" << i << ": " << process() << endl;
	}

	in.close();
	out.close();

	return 0;
}
