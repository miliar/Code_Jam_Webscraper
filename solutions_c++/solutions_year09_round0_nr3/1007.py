// qualification welcome.cpp
#include<iostream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<vector>
#include<string>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<cctype>
#include<climits>
#include<cfloat>

using namespace std;
void shape( int x );
int solve( int si, int ti );
int memo[500][19] = {0};

string t = "welcome to code jam";
string s;

int main()
{
    int N;
    scanf( "%d", &N );
    getchar();
    for( int caseNo = 1; caseNo <= N; caseNo++ )
    {
	memset( memo, -1, sizeof memo );
	printf( "Case #%d: ", caseNo );
	getline( cin, s );
	shape( solve( 0, 0 ) );
    }
    return 0;
}

void shape( int x )
{
    stringstream ss;
    ss << x;
    string q;
    ss >> q;
    while( q.size() != 4 ) 
	q = "0" + q;
    cout << q << endl;
}

int solve( int si, int ti )
{
    if( ti == 19 )
	return 1;
    if( si == s.size() )
	return 0;
    if( memo[si][ti] != -1 )
	return memo[si][ti];
    int count = 0;
    for( int i = si; i < s.size(); i++ )
    {
	if( s[i] == t[ti] )
	{
	    count = ( count + solve( i + 1, ti + 1 ) ) % 10000;
	}
    }
    return memo[si][ti] = count;
}
