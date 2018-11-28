#include <iostream>
#include <string.h>
using namespace std;

const string req = "welcome to code jam";

const int mlen = 32 , mn = 512 , mod = 10000;

int dp[mlen][mn];
string inp;
int go ( int pos , int ptr ) 
{
	if ( ptr == inp.length() )
		return pos == req.length();
	if ( pos == req.length() )
		return 1;

	int & res = dp[pos][ptr];
	if ( res != -1 )
		return res;
	
	res = go ( pos , ptr + 1 );
	if ( req[pos] == inp[ptr] )
		res += go ( pos + 1 , ptr + 1 );
	res %= mod;
	return res;
}

int main()
{
	int t;
	cin >> t;
	for ( int kase = 1; kase <= t; kase ++ )
	{
		memset ( dp , -1 , sizeof ( dp ) );
		while ( cin.peek() == '\n' ) 
			cin.get();
		getline ( cin , inp );
		int res = go (0,0);
		char buf[10];
		sprintf ( buf , "%d",res );
		string result = buf;
		while ( result.length() != 4 )
			result = "0" + result;
		cout << "Case #" << kase <<": "<< result << endl;
	}
	return 0;
}
