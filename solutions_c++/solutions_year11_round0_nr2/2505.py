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

ll n, i, t, c, d, j, p, x, y, z;
bool tabb[100][100];
list<char> a;
string ans, s;
char tabc[100][100];
list<char>::iterator it;

void add(char c)
{
	bool can = 1;
	while(can)
	{
		can = 0;
		if(a.size() > 0)
			if(tabc[(ll)a.back()- (ll)'A'][(ll)c- (ll)'A'] != '+')
			{
				c = tabc[(ll)a.back() - (ll)'A'][(ll)c - (ll)'A'];
				a.pop_back();
				can = 1;
			}
	}
	can = 0;
	for(it = a.begin(); it != a.end(); it++)
	{
		if(tabb[(ll)c - (ll)'A'][(ll)(*it) - (ll)'A'] == 1)
			can = 1;
	}
	if(can)
		a.clear();
	else
		a.push_back(c);	
}

void out(void)
{
	bool can = 0;
	for(it = a.begin(); it != a.end(); it++)
	{
		if(can)
			cout << ", ";
		cout << *it;
		can = 1;
	}

}

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
	#endif
	cin >> t;
	for(p = 1; p <= t; p++)
	{
		for(i = 0; i < 100; i++)
			for(j = 0; j < 100; j++)
			{
				tabb[i][j] = 0;
				tabc[i][j] = '+';
			}
		cin >> c;
		for(i = 1; i <= c; i++)
		{
			cin >> s;
			x = (ll)s[0] - (ll)'A';
			y = (ll)s[1] - (ll)'A';
			tabc[x][y] = s[2];
			tabc[y][x] = s[2];
		}
		cin >> d;
		for(i = 1; i <= d; i++)
		{
			cin >> s;
			x = (ll)s[0] - (ll)'A';
			y = (ll)s[1] - (ll)'A';
			tabb[y][x] = 1;
			tabb[x][y] = 1;
		}
		cin >> n;
		cin >> s;
		a.clear();
		for(i = 0; i < n; i++)		
			add(s[i]);
		cout << "Case #" << p << ": [";
		out();
		cout << ']' << endl;
	}
	
	return 0;
}