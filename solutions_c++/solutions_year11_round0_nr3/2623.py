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

struct bin_chislo
{
	void clear(void)
	{
		for(int i = 1; i <= 24; i++)
			b[i] = 0;
		l = 0;
		z = 0;
	}
	ll b[25], l, z;
};
ll n, i, x, p, ans,t, mini;
list<bin_chislo> a;
bin_chislo j, res;
bool can;

void add(ll x)
{
	j.l = 0;
	j.z = x;
	while(x > 0)
	{
		j.l++;
		j.b[j.l] = x % 2;
		x /= 2;
	}
}

void res_plass(void)
{
	res.l = max(res.l, j.l);
	for(ll i = 1; i <= res.l; i++)
	{
		if(res.b[i] == 1)
		{
			if(j.b[i] == 1)
				res.b[i] = 0;
			else
				res.b[i] = 1;
		}
		else
			res.b[i] = j.b[i];
	}
	res.z += j.z;
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
		res.clear();
		cin >> n;
		for(i = 1; i <= n; i++)
		{
			cin >> x;
			if(i == 1)
				mini = x;
			if(x < mini)
				mini = x;
				
			j.clear();
			add(x);
			a.push_back(j);
			res_plass();
		}
		can = 0;
		for(i = 1; i <= res.l; i++)	
			if(res.b[i] == 1)
				can = 1;
		if(can)
			cout << "Case #" << p << ": NO" << endl;
		else
		{
			cout << "Case #" << p << ": " << res.z - mini << endl;
		}
	}
	
	return 0;
}