#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "B-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		int n;
		cin >> n;
		int s;
		cin >> s;
		int p;
		cin >> p;
		vector<int> v(n);
		for(int i = 0; i < n; ++i)
			cin >> v[i];
		int res = 0;
		for(int i = 0; i < n; ++i)
		{
			if(v[i] >= p + p - 1 + p - 1 && p - 1 >= 0)
				++res;
			else if(v[i] >= 3*p)
				++res;
			else if(s > 0 && v[i] >= p + p-2 + p-2 && p-2 >= 0)
			{
				++res;
				--s;
			}
		}
		cout << "Case #" << Case << ": ";
		cout << res << endl;
	}

	return 0;
}
