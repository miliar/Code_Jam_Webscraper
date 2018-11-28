#include <stdio.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <iomanip>

using namespace std;

typedef long long ll;

struct but
{
	char c;
	ll x;
};

ll n, i, j, k, t, x, ans, op, bp, to, tb, p;
char c, spis[200];
list<but> lo, lb;
but help;

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
	#endif
	cin >> t;
	for(p = 1; p <= t; p++)
	{
		cin >> n;
		for(i = 1; i <= n; i++)
		{
			cin >> c >> x;
			help.c = c;
			help.x = x;
			spis[i] = c;
			if(c == 'O')
				lo.push_back(help);
			else
				lb.push_back(help);
		}
		ans = 0;
		op = 1;
		bp = 1;
		to = 1;
		tb = 1;
		j = 1;
		while(j <= n)
		{
			if(spis[j] == 'O')
			{
				if(lo.front().x != op)
				{
					if(op > lo.front().x)
						op--;
					else
						op++;
					if(lb.size() > 0)
					{
						if(bp > lb.front().x)
							bp--;
						if(bp < lb.front().x)
							bp++;
					}
				}
				else
				{
					j++;
					lo.pop_front();
					if(lb.size() > 0)
					{
						if(bp > lb.front().x)
							bp--;
						if(bp < lb.front().x)
							bp++;
					}
				}
			}
			else
			{
				if(lb.front().x != bp)
				{
					if(bp > lb.front().x)
						bp--;
					else
						bp++;
					if(lo.size() > 0)
					{
						if(op > lo.front().x)
							op--;
						if(op < lo.front().x)
							op++;
					}
				}
				else
				{
					j++;
					lb.pop_front();
					if(lo.size() > 0)
					{
						if(op > lo.front().x)
							op--;
						if(op < lo.front().x)
							op++;
					}
				}
			}
			ans++;
		}		
		cout << "Case #" << p << ": " << ans << endl;
	}
	
	return 0;
}