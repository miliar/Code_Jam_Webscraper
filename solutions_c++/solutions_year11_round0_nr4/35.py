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
	inputstream = freopen("D-large.in", "r", stdin);
	outputstream = freopen("D-large.out", "w", stdout);
}
#endif

int tonum_int(const string& str)
{
	int num;
	stringstream ss(str);
	ss>>num;
	return num;
}

int num[2000];

int main()
{
	init();
	int T;
	cin >> T;
	for (int ii = 1; ii <= T; ++ii)
	{
		int N;
		cin >> N;
		int diso = 0;
		for (int i = 1; i <= N; ++i)
		{
			cin >> num[i];
			if (num[i] != i)
			{
				++diso;
			}
		}
		cout << "Case #" << ii << ": " << diso << endl;
	}
	return 0;
}
