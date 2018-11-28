#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;

ifstream fin( "C-small-attempt2.in" );
ofstream fout( "C-small-attempt2.out" );

#define int64 long long
#define pii pair< int, int >

#define cin fin
#define cout fout

int t, n, test = 1;
bool seen[4000];
int64 h[4000], idx[4000];
bool bad;

int main() {
	for( cin >> t; t--; ) {
		cin >> n;
		bad = false;
		memset( h, 0, sizeof h );
		memset( idx, 0, sizeof idx );
		for( int i = 0; i < n - 1; i++ )	{
			cin >> idx[i];
			if( idx[i] <= i || idx[i] > n )	bad = true;
			idx[i]--;
			for( int j = 0; j < i; j++ ) {
				if( idx[j] > i && idx[j] < idx[i] )	bad = true;
			}
		}
		cout << "Case #" << test++ << ": ";
		if( bad ) {
			cout << "Impossible" << endl;
			continue;
		}
		memset( seen, false, sizeof seen );
		int c = 0;
		while( true ) {
			seen[c] = true;
			h[c] = 1000000000;
			if( c == n - 1 )	break;
			c = idx[c];
		}
		bool change = true;
		while( change ) {
			change = false;
			for( int i = 0; i < n; i++ ) {
				int j = idx[i];
				if( !seen[i] && seen[j] ) {
					seen[i] = true;
					change = true;
					h[i] = (h[j] - h[idx[j]]) * (i - j) / (j - idx[j]) + h[j] - (2000 - (j - i));
				}
			}
		}
		for( int i = 0; i < n - 1; i++ ) {
			for( int j = i + 1; j < n; j++ ) {
				//if( j == idx[i] )	continue;
				if( j < idx[i] && (h[idx[i]] - h[i]) * (j - i) <= (h[j] - h[i]) * (idx[i] - i) )	{
					//cout << "bad at " << i << ' ' << idx[i] << ' ' << j << endl;
					bad = true;
				}
				if( j > idx[i] && (h[idx[i]] - h[i]) * (j - i) < (h[j] - h[i]) * (idx[i] - i) )		{
					//cout << "bad at " << i << ' ' << idx[i] << ' ' << j << endl;
					bad = true;
				}
			}
		}
		if( bad ) {
			cout << "Impossible" << endl;
			continue;
		}
		for( int i = 0; i < n; i++ ) {
			if( i )	cout << ' ';
			cout << h[i];
		}
		cout << endl;
	}
	return 0;
}
