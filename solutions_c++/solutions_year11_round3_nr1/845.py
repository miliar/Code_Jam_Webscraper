#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <hash_map>
#include <hash_set>
#include <algorithm>
#include <climits>
#include <stdlib.h>

using stdext::hash_map;
using stdext::hash_set;
using namespace std;

int gcd (int m, int n) { 
	while (n!=0) { int t = m % n; m=n; n=t; } 
	return m; 
} 


/* 
3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##..


out << setiosflags(ios::fixed) << setprecision(7)
*/

void calculate( istream& in, ostream& out )
{
	int l,c;
	in >> l >> c;


	bool ok = true;
	vector<string> data;
	for (int i = 0; i < l; ++i)
	{
		data.push_back(string());
		in >> data.back();
	}

	for (int i = 0; i < l; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			if (data[i][j] == '.' || data[i][j] == '\\' || data[i][j] == '/')
			{
				continue;
			}
			if (data[i][j] == '#')
			{
				if (j + 1 < c && data[i][j+1] == '#' 
					&& i + 1 < l && data[i+1][j] == '#' && data[i+1][j+1] == '#')
				{
					data[i][j] = '/';
					data[i][j+1] = '\\';
					data[i+1][j] = '\\';
					data[i+1][j+1] = '/';
				}
				else
				{
					ok = false;
					break;
				}
			}
		}
	}

	if (ok)
	{
		for (int i = 0; i < l; ++i)
		{
			out << "\n" << data[i];
		}
	}
	else
	{
		out << "\nImpossible";
	}

}

int main( int argc, char *argv[] )
{
	unsigned cases;
	cin >> cases;
	for ( unsigned i = 1; i <= cases; ++i )
	{
		cout << "Case #" << i << ": "; 
		calculate( cin, cout );
		cout << endl;
	}

	return EXIT_SUCCESS;
}
