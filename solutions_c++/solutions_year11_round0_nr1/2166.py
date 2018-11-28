//#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <utility>

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;
using namespace std;


int main()
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;

	for (int tst = 1; tst <= t; ++tst)
	{
		int n;
		cin >> n;

		int b_pos = 1, o_pos = 1;
        int b_time = 0, o_time = 0;

        for (int i = 0; i < n; ++i)
        {
        	char c; int p;
        	cin >> c >> p;
        	if (c == 'O')
        	{
        		o_time = max(b_time, o_time + abs(p - o_pos)) + 1;
        		o_pos = p;
        	}
        	else
        	{
        		b_time = max(o_time, b_time + abs(p - b_pos)) + 1;
        		b_pos = p;
        	}	
        }
        cout << "Case #" << tst << ": " << max(o_time, b_time) << '\n';
	}

	return 0;
}
