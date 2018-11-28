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
2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.

out << setiosflags(ios::fixed) << setprecision(7)
*/

struct Data 
{
	Data() : win(0), total(0)
	{
	}
	string str;
	int win;
	int total;
	double wp;
	double owp;
	double oowp;
	double score;
};
void calculate( istream& in, ostream& out )
{
	int N;
	in >> N;

	vector<Data> v;

	for (int i = 0; i < N; ++i)
	{
		Data d;
		in >> d.str;
		for (int j = 0; j < N; ++j)
		{
			if (d.str[j] == '1') d.win++;
			if (d.str[j] != '.') d.total++;
		}
		d.wp = double(d.win)/d.total;
		v.push_back(d);
	}

	for (int i = 0; i < N; ++i)
	{
		Data& d = v[i];
		double swp = 0.0;
		for (int j = 0; j < N; ++j)
		{
			if (d.str[j] == '0')
			{
				swp += double(v[j].win - 1)/(v[j].total - 1);
			}
			if ( d.str[j] == '1' )
			{
				swp += double(v[j].win)/(v[j].total - 1);
			}
		}
		d.owp = swp / d.total;
	}


    for (int i = 0; i < N; ++i)
	{
		Data& d = v[i];
		double sowp = 0.0;
		for (int j = 0; j < N; ++j)
		{
			if (d.str[j] != '.')
			{
				sowp += v[j].owp;
			}
		}
		d.oowp = sowp / d.total;
		d.score = 0.25 * d.wp + 0.50 * d.owp + 0.25 * d.oowp;

	    out << "\n" << setprecision(12) << d.score;
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
