#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

int M,V;
int val[34];
bool G[34];
bool C[34];
int res;
int restmp;

void solve(int n)
{
	int i,j;
	if (n == 1)
	{
		if (val[n] == V && res > restmp)
		{
			res = restmp;
		}
		return;
	}
	int ind = (n-1)/2;
	if (C[ind] == 0)
	{
		if (G[ind] == 1)
			val[ind] = val[n] & val[n-1];
		else
			val[ind] = val[n] | val[n-1];
			solve(n-2);
	}
	else
	{
		if (G[ind] == 1)
		{
			val[ind] = val[n] & val[n-1];
			solve(n-2);
			val[ind] = val[n] | val[n-1];
			restmp++;
			solve(n-2);
			restmp--;
		}
		else
		{
			val[ind] = val[n] | val[n-1];
			solve(n-2);
			val[ind] = val[n] & val[n-1];
			restmp++;
			solve(n-2);
			restmp--;
		}
	}
}
 int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("out.txt","w",stdout);
	int ncase,m;
	cin >> ncase;
	m = 0;
	while (ncase--)
	{
		m++;
		cin >> M >> V;
		int i;
		for (i = 1 ; i <= (M-1)/2 ; i++)
			cin >> G[i] >> C[i];			
		for (i = (M-1) / 2 + 1; i <= M ; i++)
			cin >> val[i];
		restmp = 0;
		res = 1000000;
		solve(M);
		cout << "Case #" << m << ": " ;
		if (res !=1000000 )
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
		
		
		//printf("Case #%d: ",m);
	}
}
