#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

string s[200];

int main()
{
     freopen("input.txt", "r", stdin);
     freopen("output.txt", "w", stdout);

     int NTests;
     cin >> NTests;

     for (int test = 0; test < NTests; test++)
     {
          int n, m;
		  cin >> n >> m;

		  for (int i = 0; i < n; i++)
			  cin >> s[i];

		  bool q = true;

		  for (int i = 0; i < n-1; i++)
			  for (int j = 0; j < m-1; j++)
				  if (s[i][j] == '#')
				  {
					  if (s[i][j+1] != '#' || s[i+1][j] != '#' || s[i+1][j+1] != '#')
						  q = false;

					  s[i][j] = '/';
					  s[i][j+1] = '\\';
					  s[i+1][j] = '\\';
					  s[i+1][j+1] = '/';
				  }

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (s[i][j] == '#')
					q = false;

		cout << "Case #" << test+1 << ": " << endl;
		if (!q)
			cout << "Impossible" << endl;
		else
		{
			for (int i = 0; i < n; i++)
				cout << s[i] << endl;
		}

     }

     return 0;
}