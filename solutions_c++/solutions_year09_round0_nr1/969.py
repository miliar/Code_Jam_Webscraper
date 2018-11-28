// qualification aliens.cpp
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
int pattern[500][15][26] = {0};
vector<string> known;

int main()
{
    int L, D, N;
    scanf( "%d%d%d", &L, &D, &N );
    while( D-- )
    {
	string s;
	cin >> s;
	known.push_back( s );
    }
    getchar();
    for( int caseNo = 0; caseNo < N; caseNo++ )
    {    
	string s;
	getline( cin, s );
	int position = 0;
	for( int i = 0; i < s.size();  )
	{
	    if( s[i] == '(' )
	    {
		i++;
		for( ; s[i] != ')' && i < s.size(); i++ )
		{
		    pattern[caseNo][position][s[i] - 'a'] = 1;		    
		}
		position++;
		i++;
	    }
	    else
	    {
		pattern[caseNo][position][s[i] - 'a'] = 1;
		position++;
		i++;
	    }
	}
    }
    for( int caseNo = 0; caseNo < N; caseNo++ )
    {
	printf( "Case #%d: ", caseNo + 1 );
	int count = 0;
	for( int dict = 0; dict < known.size(); dict++ )
	{
	    bool matched = true;
	    for( int i = 0; i < known[dict].size(); i++ )
	    {
		if( pattern[caseNo][i][known[dict][i] - 'a'] == 0 )
		{
		    matched = false;
		    break;
		}
	    }
	    if( matched == true )
		count++;
	}
	printf( "%d\n", count );
    }
    return 0;
}
