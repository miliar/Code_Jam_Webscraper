/*
ID: junwang1
LANG: C++
TASK: maze1
*/

#include <stdio.h>

#include <algorithm>

#include <sstream>

#include <memory.h>

#include <math.h>

#include <string>

#include <functional>

#include <iostream>

#include <set>

#include <vector>

#include <list>

#include <map>

#include <queue>

#include <stack>

using namespace std;

const int MAX_N =  256;

const int MAX_L = 200001;

int convert (int x, int b)
{
	int sum = 0;
	int d = 0;
	while (x)
	{
		d = x % b;
		x /= b;
		sum += d * d;
	}

	return sum;
}

set <int> s[11];
set <int> s1[11];

bool solve (int x, int base[], int n)
{
	int sum = 0;
	int b = 0;
	int y = x;

	int i = 0;
	for (i = 0; i < n; ++i)
	{
		b = base[i];
		y = x;
		set <int> r;
		bool ok = false;
		do
		{
			
			if (s1[b].find(y) != s1[b].end())
			{
				return false;
			}

			if (s[b].find(y) != s[b].end())
			{
				ok = true;
				break;
			}

			r.insert (y);
			y = convert(y, b);

			if (r.find(y) != r.end())
			{
				ok = false;
				break;
			}

		}while (y != 1);

		if (y == 1 || ok)
		{
			s[b].insert (r.begin(), r.end());
			
		}
		else
		{
			s1[b].insert (r.begin(), r.end());
			return false;
		}
		
		
	}

	return true; 

	

}

void Work ()
{
	// freopen ("data.in", "r", stdin);
	// freopen ("gcj.out", "w", stdout);

    

	int T = 0;
	int t = 0;
	int i = 0;
	int j = 0;

	scanf ("%d", &T);

	char temp[MAX_N];
	int base[MAX_N];
	int b = 0;
	gets(temp);

	for (t = 1; t <= T; ++t)
	{
		gets(temp);
		i = 0;
		int k = 0;
		istringstream ist (temp);
		while (ist >> b)
		{
			base[i++] = b;
		}
		

/*
		while ((k = sscanf (temp + k, "%d", &b)) != -1)
		{
			base[i++] = b;
		} */

		for (int x = 2; ; ++x)
		{
			if (solve (x, base, i))
			{
				printf ("Case #%d: %d\n", t, x);
				break;
			}
		}
	}
	
}

int main()
{
	Work ();

	return 0;
}

