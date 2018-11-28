#include <stdio.h>
#include <stdlib.h>
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
#include <ctime>
#include <iomanip>
#include <time.h>
#include <string.h>

using namespace std;

#ifdef ONLINE_JUDGE
void init()
{
}
#else
FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("A-large.in", "r", stdin);
	outputstream = freopen("A-large.out", "w", stdout);
}
#endif

int tonum_int(const string& str)
{
	int num;
	stringstream ss(str);
	ss>>num;
	return num;
}

int main()
{
	init();
	int cases;
	cin >> cases;
	long long n, pd, pg;
	for (int i = 1; i <= cases; ++i)
	{
		cout << "Case #" << i << ": ";
		cin >> n >> pd >> pg;
		if (pd != 100 && pg == 100)
		{
			cout << "Broken" << endl;
			continue;
		}
		if (pd != 0 && pg == 0)
		{
			cout << "Broken" << endl;
			continue;
		}
		int p2 = 0;
		int p5 = 0;
		while(pd % 2 == 0 && p2 < 2)
		{
			pd /= 2;
			++p2;
		}
		while(pd % 5 == 0 && p5 < 2)
		{
			pd /= 5;
			++p5;
		}
		int minn = 1;
		if (p2 < 2) minn *= 2;
		if (p2 < 1) minn *= 2;
		if (p5 < 2) minn *= 5;
		if (p5 < 1) minn *= 5;
		if (minn > n)
		{
			cout << "Broken" << endl;
			continue;
		}
		cout << "Possible" << endl;
	}
		
	return 0;
}
