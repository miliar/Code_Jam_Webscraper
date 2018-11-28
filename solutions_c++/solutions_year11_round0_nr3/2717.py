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

#define sum(a,b)	 		((a)^(b))

void solve ( int testcase )
{
	int n, i , s1, s2, acum;
	cin >> n;
	
	int arr[n];
	for ( i = 0; i < n; ++i )
		cin >> arr[i];

	int best = -10;
	for ( int st = 1; st+1 < (1<<n); ++st )
	{
		s1 = 0, s2 = 0, acum = 0;
		for ( i = 0; i < n; ++i )
			if ( st & ( 1 << i ) ) s1 = sum ( s1 , arr[i] ), acum += arr[i];
			else s2 = sum ( s2 , arr[i] );
		
		if ( s1 == s2 )
			best = max ( best , acum );
	}
	
	if ( best == -10 ) cout << "Case #" << testcase << ": NO" << endl;
	else cout << "Case #" << testcase << ": " << best << endl;
}

int main ()
{
	//freopen ( "C.in", "r" , stdin );
	//freopen ( "C.out", "w" , stdout );
	
	int n;
	cin >> n;
	for ( int i = 1; i <= n; ++i )
		solve ( i );
	
	return 0;
}
