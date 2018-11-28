
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

ifstream in("C-large.in.txt");
ofstream out("C-large.out.txt");
string str;
string wel = "welcome to code jam";
int memo[512][20];

string tostr(int num)
{
	stringstream ss;
	ss << num;
	string res = ss.str();
	while(res.size() < 4)
	{
		res = "0" + res;
	}
	return res;
}

int go(int p1, int p2)
{
	if (p2 == 18)
	{
		return 1;
	}
	int& ref = memo[p1][p2];
	if (ref != -1)
	{
		return ref;
	}
	ref = 0;
	for (int i = p1 + 1; i < (int) str.size(); ++i)
	{
		if (str[i] == wel[p2 + 1])
		{
			ref += go(i, p2 + 1);
			ref %= 10000;
		}
	}
	return ref;
}

int _tmain()
{
	int N;
	in >> N;
	getline(in, str);
	for (int i = 1; i <= N; ++i)
	{
		getline(in, str);
		int res = 0;
		memset(memo, -1, sizeof(memo));
		for (int j = 0; j < (int) str.size(); ++j)
		{
			if (str[j] == 'w')
			{
				res += go(j, 0);
				res %= 10000;
			}
		}
		out << "Case #" << i << ": " << tostr(res) << endl;
	}
    return 0;
}
