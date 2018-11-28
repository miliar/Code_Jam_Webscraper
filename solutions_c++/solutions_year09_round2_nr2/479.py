#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>

using namespace std;

string res;

string solve( string a )
{
	if( next_permutation(a.begin(),a.end()) ) ; else
	{
		sort( a.begin(), a.end() );
		res = "";
		int z = 1;
		for( int i = 0; i < (int)a.size(); i++ )
		{
			if( a[i] == '0' )
			{
				z++;
			} else
			{
				res +=a[i];
			}
		}
		
		for(int i = 0; i < z; i++)	res = res.substr(0,1)+"0"+res.substr( 1,(int)res.length()-1 );
		a = res;
	}
	return a;
}


string s;

int main()
{
	int n;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	scanf( "%d",&n );
	for(int i=0; i < n; i++)
	{
		cin >> s;
		cout << "Case #" << i+1 << ": " << solve(s) << endl;
	}
	
	return 0;
}