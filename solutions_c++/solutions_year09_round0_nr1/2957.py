#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;
typedef long long ll;
#define SET(a, n) memset(a, n, sizeof a);
template<class A, class B> void CONV(A& x, B& y) { stringstream s; s << x; s >> y; }


int l, d, n;
vector<string> dict;
vector< vector<char> > words; 
string cur;


int proc()
{
	int res = 0;
	for ( int i=0; i<dict.size(); ++i )
	{
		bool found = true;
		for ( int ix=0; ix<l && found; ++ix )
		{
			bool ok = false;
			for ( int iy=0; iy<words[ix].size(); ++iy )
			{
				if ( words[ix][iy] == dict[i][ix] )
				{
					ok = true;
				}
			}
			if ( !ok )
			{
				found = false;
			}
		}
		if ( found )
		{
			++res;
		}
	}

	return res;
}

int main()
{
	freopen( "d://A-small-attempt1.in", "r", stdin );
	freopen( "d://out.txt", "w", stdout );
	cin >> l >> d >> n;

	vector<char> vt;
	for ( int i=0; i<l; ++i )
	{
		words.push_back( vt );
	}
	for ( int i=0; i<d; ++i )
	{
		string tmp;
		cin >> tmp;
		dict.push_back( tmp );
	}

	for ( int i=0; i<n; ++i )
	{
		string tmp;
		cin >> tmp;
		int cnt = 0;
		bool stay = false;
		for ( int ix=0; ix<tmp.size(); ++ix )
		{
			if ( tmp[ix] == '(' )
			{
				stay = true;
			}
			else if ( tmp[ix] == ')' )
			{
				stay = false;
			}
			else
			{
				words[cnt].push_back( tmp[ix] );
			}
			if ( !stay )
			{
				++cnt;
			}
		}
		cout << "Case #" << i+1
			<< ": " << proc() << endl; 
		for ( int ix=0; ix<l; ++ix )
		{
			words[ix].clear();
		}
	}
	return 0;
}