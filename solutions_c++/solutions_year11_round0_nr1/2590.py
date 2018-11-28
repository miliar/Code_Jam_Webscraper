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



int Solve(istream &in)
{
	int n;
	in >> n;

	deque< pair< int, int > > o, b;
	for (int i = 0; i < n; ++i)
	{
		char c;
		int p;
		in >> c >> p;
		if (c == 'O')
			o.push_back(make_pair(i, p));
		else
			b.push_back(make_pair(i, p));
	}

	int res = 0;
	int cur_o = 1, cur_b = 1;
	while (!o.empty() && !b.empty())
	{
		char cur = o.front().first < b.front().first ? 'o' : 'b';

		if (o.front().second == cur_o && cur == 'o')
			o.pop_front();
		else if (o.front().second > cur_o)
			++cur_o;
		else if (o.front().second < cur_o)
			--cur_o;
		
		if (b.front().second == cur_b && cur == 'b')
			b.pop_front();
		else if (b.front().second > cur_b)
			++cur_b;
		else if (b.front().second < cur_b)
			--cur_b;

		++res;
	}

	int &cur_d = o.empty() ? cur_b : cur_o;
	deque< pair< int, int > > &d = o.empty() ? b : o;
	while (!d.empty())
	{
		if (d.front().second == cur_d)
			d.pop_front();
		else if (d.front().second > cur_d)
			++cur_d;
		else
			--cur_d;
		++res;
	}

	return res;
}


int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t;
	fin >> t;
	for (int cnt = 1; cnt <= t; ++cnt)
	{
		fout << "Case #" << cnt << ": " << Solve(fin) << endl;
	}

	return 0;
}