//Solution by Zhusupov Nurlan
#include <iostream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <stack>
#include <queue>
#include <ctime>

using namespace std;

typedef long long LL;
typedef map<string , int> MSI;
typedef vector<int> VI;

#define pb(x) push_back(x)
#define sqr(x) ((x) * (x))
#define F first
#define S second
#define SZ(t) ((int) t.size())
#define len(t) ((int) t.length())
#define base 10
#define fname ""
#define sz 1000 * 1000
#define EPS (1e-8)
#define INF ((int)1e9 + 9)
#define write(xx) printf("%d" , xx);
#define readln(xx) getline(cin , xx)
#define read(xx) scanf("%d" , &xx)
#define for(xx1 , yy1 , zz1) for(int zz1 = xx1 ; zz1 <= yy1 ; zz1++)

const double PI  = acos(-1.0);

char ch, a[10][10];
int t, c[1000];
bool f, ff;

bool check(int x, int y, int dx, int dy)
{
	c[a[x][y]]++;
	if (!a[x + dx][y + dy])
	{
		if ((c['O'] && c['X']) || c['.'])
		{
			c['O'] = c['X'] = c['.'] = c['T'] = 0;
			return false;
		}
		if (c['O'])
			ch = 'O';
	   	else
	   		ch = 'X';
		c['O'] = c['X'] = c['.'] = c['T'] = 0;
		return true;
  	}
  	return check(x + dx, y + dy, dx, dy);
}

int main(){
	freopen(fname"in", "r", stdin);
	freopen(fname"out", "w", stdout);

	cin >> t;

	for (1, t, test)
	{
		f = false;
		cout << "Case #" << test << ": ";
		for (1, 4, i)
			for (1, 4, j)
			{
				cin >> a[i][j];
				if (a[i][j] == '.')
					f = true;
			}
	   	ff = false;

   		for (1, 4, i)
   		{
   			if (!ff && check(i, 1, 0, 1))
   			{
   				ff = true;
   				cout << ch << " won";
   				break;
   			}
			if (!ff && check(1, i, 1, 0))
   			{
   				ff = true;
   				cout << ch << " won";
   				break;    
   			}
		}
		if (!ff && check(1, 1, 1, 1))
		{
			ff = true;
   			cout << ch << " won";
   		}
   		if (!ff && check(4, 1, -1, 1))
   		{
   			ff = true;
   			cout << ch << " won";
		}
		if (!ff)
		{
			if (!f)
				cout << "Draw";
	   		else
	   			cout << "Game has not completed";
	  	}
	  	cout << endl;
	}

    	return 0;
}
