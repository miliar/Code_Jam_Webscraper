#include <cstdio>
#include <vector>
#include <utility>
#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <limits.h>
#include <time.h>
#include <iomanip>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <list>
using namespace std;
typedef int LL;


int Solve()
{
	int n;
	cin >> n;
	
	int time_s = 0;
	int prev_r = -1; //b0 o1
	int pos[] = {1, 1};
	int res = 0;
	
	for (int i = 0; i < n; i++)
	{
		char c, d;
		int x;
		cin >> c >> x;
		int cur_r = (c == 'O');
		if (cur_r == prev_r)
		{
			time_s += abs(pos[cur_r] - x) + 1;
			res += abs(pos[cur_r] - x) + 1;
			pos[cur_r] = x;
		}
		else
		{
			int dis = abs(pos[cur_r] - x);
			dis = max(dis - time_s, 0);
			
			time_s = dis + 1;
			res += dis + 1;
			prev_r = cur_r;
			pos[cur_r] = x;
		}
	}
	return res;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	cin >> t; 
	for (int i = 0; i < t; i++)
	{
		cout << "Case #" << i+1 << ": " << Solve() << endl;
	}

	return 0;
}