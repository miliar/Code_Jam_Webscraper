#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <vector>
#include <string>
#include <utility>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <ctype.h>
#include <sstream>
#include <bitset>
#include <deque>

using namespace std;

map <string, char> comb;
bool opposed[270][270];
string cad;

void read_data ( ) {
	memset ( opposed , 0 , sizeof ( opposed ) );
	comb.clear();
	
	int n;
	string str;
	
	cin >> n;
	for ( int i = 0; i < n; ++i ) {
		cin >> str;
		comb.insert ( make_pair ( str.substr ( 0 , 2 ) , str[2] ) );
		reverse ( str.begin(), str.end() );
		comb.insert ( make_pair ( str.substr ( 1 , 2 ) , str[0] ) );
	}
	
	cin >> n;
	for ( int i = 0; i < n; ++i ) {
		cin >> str;
		opposed[(int)str[0]][(int)str[1]] = opposed[(int)str[1]][(int)str[0]] = true;
	}
	
	cin >> n >> cad;
}

void solve ( int testcase )
{
	read_data();
	
	string ans = "";
	for ( int i = 0; i < (int)cad.size(); ++i ) {
		ans.push_back ( cad[i] );
		if ( ans.size() >= 2 )
			if ( comb.count ( ans.substr ( ans.size()-2 , 2 ) ) > 0 ) {
				ans.push_back ( comb[ ans.substr ( ans.size()-2 , 2 ) ] );
				ans.erase ( ans.end()-3 , ans.end()-1 );
			}
		for ( int j = 0; j+1 < (int)ans.size(); ++j )
			if ( opposed[(int)ans[j]][(int)(*ans.rbegin())] )
				ans.clear();
	}
	
	cout << "Case #" << testcase << ": [";
	for ( int i = 0; i+1 < (int)ans.size(); ++i )
		cout << ans[i] << ", ";
	if ( ans.empty() ) cout << "]\n";
	else cout << (*ans.rbegin()) << "]\n";
}

int main ()
{
	//freopen ( "B.in", "r" , stdin );
	//freopen ( "B.out", "w" , stdout );
	
	int ntestcases;
	cin >> ntestcases;
	for ( int i = 1; i <= ntestcases; ++i )
		solve ( i );

	return 0;
}
