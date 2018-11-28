
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

ifstream in("A-large.in.txt");
ofstream out("A-large.out.txt");

int _tmain()
{
	int t;
	in >> t;
	for (int i = 0; i < t; ++i)
	{
		long long n;
		in >> n;
		vector<long long> v1;
		vector<long long> v2;
		long temp = 0;
		for (int j = 0; j < n; ++j)
		{
			in >> temp;
			v1.push_back(temp);
		}
		for (int j = 0; j < n; ++j)
		{
			in >> temp;
			v2.push_back(temp);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		reverse(v1.begin(), v1.end());
		long long res = 0;
		for (int j = 0; j < n; ++j)
		{
			res += v1[j] * v2[j];
		}
		out << "Case #" << i + 1 << ": " << res << endl;
	}
	return 0;
}