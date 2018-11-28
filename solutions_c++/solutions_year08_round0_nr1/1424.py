
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

ifstream in("large0.in.txt");
ofstream out("large0.out.txt");
set<string> engine;

int _tmain()
{
	int n;
	in >> n;
	for (int i = 0; i < n; ++i)
	{
		engine.clear();
		int s, q;
		in >> s;
		string str;
		getline(in, str);
		for (int j = 0; j < s; ++j)
		{
			getline(in, str);
			engine.insert(str);
		}
		in >> q;
		getline(in, str);
		set<string> cur;
		int res = 0;
		for (int j = 0; j < q; ++j)
		{
			getline(in, str);
			if (cur.size() + 1 == engine.size() && cur.count(str) == 0)
			{
				++res;
				cur.clear();
				cur.insert(str);
			}
			else
			{
				cur.insert(str);
			}
		}
		out << "Case #" << i + 1 << ": " << res << endl;
	}
	return 0;
0;
}