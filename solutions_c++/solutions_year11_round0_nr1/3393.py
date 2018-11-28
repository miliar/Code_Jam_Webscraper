#include <iostream>
#include <fstream>
#include <vector>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <memory>
#include <sstream>

using namespace std;

int time[101];

int t, n, i, j, c, last1, last2, lastIndex1, lastIndex2;

char color;

int main()
{
	freopen("D://1.in", "rb", stdin);
	freopen("D://1.out", "wb", stdout);
	cin >> t;
	for(c = 1; c <= t; c++)
	{
		cin >> n;
		last1 = last2 = 1;
		lastIndex1 = lastIndex2 = 0;
		time[0] = 0;
		for(i = 1;i <= n;i++)
		{
			cin >> color >> j;
			if(color == 'O') 
			{
				time[i] = max(time[i - 1] + 1, time[lastIndex1] + abs(j - last1) + 1);
				last1 = j, lastIndex1 = i;
			}
			else{
				time[i] = max(time[i - 1] + 1, time[lastIndex2] + abs(j - last2) + 1);
				last2 = j, lastIndex2 = i;
			}
		}
		cout << "Case #" << c << ": " << time[n] << endl; 
	}
};


