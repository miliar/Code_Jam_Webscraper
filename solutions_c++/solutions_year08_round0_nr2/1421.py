
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <conio.h>
#include <iomanip>
#using <mscorlib.dll>

using namespace std;

ifstream in("B-large.in.txt");
ofstream out("B-large.out.txt");

struct Eve
{
	int time;
	int type; //1: plus , 2: subtract
	Eve(int a, int b)
	{
		time = a;
		type = b;
	}
};

bool operator < (const Eve& a, const Eve& b)
{
	if (a.time != b.time)
	{
		return a.time < b.time;
	}
	return a.type < b.type;
}

int tonum(string s)
{
	stringstream ss(s);
	int a, b;
	char c;
	ss >> a >> c >> b;
	return a * 60 + b;
}

int _tmain()
{
	int n;
	in >> n;
	for (int i = 0; i < n; ++i)
	{
		int t;
		in >> t;
		int na, nb;
		in >> na >> nb;
		vector<int> astart;
		vector<int> aend;
		vector<int> bstart;
		vector<int> bend;
		for (int j = 0; j < na; ++j)
		{
			string s1, s2;
			in >> s1 >> s2;
			astart.push_back(tonum(s1));
			aend.push_back(tonum(s2));
		}
		for (int j = 0; j < nb; ++j)
		{
			string s1, s2;
			in >> s1 >> s2;
			bstart.push_back(tonum(s1));
			bend.push_back(tonum(s2));
		}

		vector<Eve> e;
		for (int j = 0; j < astart.size(); ++j)
		{
			e.push_back(Eve(astart[j], 2));
		}
		for (int j = 0; j < bstart.size(); ++j)
		{
			e.push_back(Eve(bend[j] + t, 1));
		}
		sort(e.begin(), e.end());
		int anow = 0;
		int aneed = 0;
		for (int j = 0; j < e.size(); ++j)
		{
			if (e[j].type == 1)
			{
				anow++;
			}
			else if (e[j].type == 2)
			{
				if (anow == 0)
				{
					aneed++;
				}
				else
				{
					anow--;
				}
			}
		}
		e.clear();

		for (int j = 0; j < astart.size(); ++j)
		{
			e.push_back(Eve(aend[j] + t, 1));
		}
		for (int j = 0; j < bstart.size(); ++j)
		{
			e.push_back(Eve(bstart[j], 2));
		}
		sort(e.begin(), e.end());
		int bnow = 0;
		int bneed = 0;
		for (int j = 0; j < e.size(); ++j)
		{
			if (e[j].type == 1)
			{
				bnow++;
			}
			else if (e[j].type == 2)
			{
				if (bnow == 0)
				{
					bneed++;
				}
				else
				{
					bnow--;
				}
			}
		}
		e.clear();
		out << "Case #" << i + 1 << ": "<< aneed << " " << bneed << endl;
	}
	return 0;
}