#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cmath>
#include <fstream>
#include <time.h>
#include <sstream>
#include <stdio.h>
#include <cstring>

using namespace std;

#define ll long long
#define ul unsigned long long
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define REP(i, n) for (int (i) = 0; (i) < (n); (i) ++)

int main()
{
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int n, t;
	in>>t;
	char a[4][4];
	for (int q = 1; q <= t; q++)
	{
		if (q == 5)
			cout<<q<<'\n';
		REP(i, 4)
			REP(j, 4)
				in>>a[i][j];
		map<char, int> k;
		char w = 'd';
		REP(i, 4)
		{
			//k.clear();
			k['X'] = 0;
			k['O'] = 0;
			REP(j,4)
			{
				if (a[i][j] == 'X')
					k['X'] ++;
				if (a[i][j] == 'O')
					k['O'] ++;
				if (a[i][j] == 'T')
				{
					k['X'] ++;
					k['O'] ++;
				}

			}
			if (k['X'] == 4) 
			{
				out<<"Case #"<<q<<": X won\n";
				w = 'X';
				break;
			}
			if (k['O'] == 4) 
			{
				out<<"Case #"<<q<<": O won\n";
				w = 'O';
				break;
			}

		}
		if (w != 'd') continue;
		REP(i, 4)
		{
			//k.clear();
			k['X'] = 0;
			k['O'] = 0;
			REP(j,4)
			{
				if (a[j][i] == 'X')
					k['X'] ++;
				if (a[j][i] == 'O')
					k['O'] ++;
				if (a[j][i] == 'T')
				{
					k['X'] ++;
					k['O'] ++;
				}

			}
			if (k['X'] == 4) 
			{
				out<<"Case #"<<q<<": X won\n";
				w = 'X';
				break;
			}
			if (k['O'] == 4) 
			{
				out<<"Case #"<<q<<": O won\n";
				w = 'O';
				break;
			}

		}
		if ( w!= 'd') continue;
		k['X'] = 0;
		k['O'] = 0;
		REP(i , 4)
		{
			if (a[i][i] == 'X')
					k['X'] ++;
			if (a[i][i] == 'O')
					k['O'] ++;
			if (a[i][i] == 'T')
			{
				k['X'] ++;
				k['O'] ++;
			}
		}
		if (k['X'] == 4) 
		{
			out<<"Case #"<<q<<": X won\n";
			w = 'X';
			continue;
		}
		if (k['O'] == 4) 
		{
			out<<"Case #"<<q<<": O won\n";
			w = 'O';
			continue;
		}
		/*k['X'] = 0;
		k['O'] = 0;
		for (int i = 3; i >= 0; i--)
		{
			if (a[i][i] == 'X')
					k['X'] ++;
			if (a[i][i] == 'O')
					k['O'] ++;
			if (a[i][i] == 'T')
			{
				k['X'] ++;
				k['O'] ++;
			}
		}
		if (k['X'] == 4) 
		{
			out<<"Case #"<<q<<": X won\n";
			w = 'X';
			continue;
		}
		if (k['O'] == 4) 
		{
			out<<"Case #"<<q<<": O won\n";
			w = 'O';
			continue;
		}*/

		k['X'] = 0;
		k['O'] = 0;
		REP(i, 4)
		{
			if (a[i][3-i] == 'X')
					k['X'] ++;
			if (a[i][3-i] == 'O')
					k['O'] ++;
			if (a[i][3-i] == 'T')
			{
				k['X'] ++;
				k['O'] ++;
			}
		}
		if (k['X'] == 4) 
		{
			out<<"Case #"<<q<<": X won\n";
			w = 'X';
			continue;
		}
		if (k['O'] == 4) 
		{
			out<<"Case #"<<q<<": O won\n";
			w = 'O';
			continue;
		}
		int r = 0;
		REP(i, 4)
			REP(j , 4)
			if (a[i][j] == '.') r++;
		if ( r == 0)
			out<<"Case #"<<q<<": Draw\n";
		else 
			out<<"Case #"<<q<<": Game has not completed\n";
	}
	in.close();
	out.close();
	return 0;
}