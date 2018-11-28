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
#include <numeric>

using namespace std;

#define ll          long long
#define VI          vector<int>
#define VS          vector<string>
#define ALL(a)      (a).begin(), (a).end()
#define SORT(a)     sort( ALL(a) )
#define PB          push_back
#define FOR(i,a,b)  for( int i = (a); i < (int)(b); i++ )
#define dump(x)     cout << #x << " = " << (x) << endl
#define dump_vec(x) FOR(i,0,x.size()) cout << x[i] << " "; cout << endl


template< typename type > type readOne()
{
    type res;
    char inp[5000];
    
    gets( inp );
    stringstream ss( inp );
    ss >> res;
    return res;
}

template< typename type > vector<type> readMulti()
{
    vector<type> res;
    char inp[5000];
    
    gets( inp );
    stringstream ss( inp );
    for ( type t; ss >> t; )
        res.push_back( t );
    return res;
}

//
//
// LET'S START
//
//

// mode = 1 for inside (), 0 otherwise
int good( string& word, string& dict, int mode, int pos1, int pos2 )
{
    if ( pos2 >= dict.size() )
        return 1;
        
    if ( pos1 >= word.size() )
        return 0;
    
    if ( word[pos1] == '(' )
        return good( word, dict, 1, pos1 + 1, pos2 );
    if ( word[pos1] == ')' )
        return 0;
    
    if ( mode == 1 )
    {
        if ( word[pos1] == dict[pos2] )
        {
            int np = pos1 + 1;
            for ( ; ; np ++ )
                if ( word[np] == ')' )
                    break;
            return good( word, dict, 0, np + 1, pos2 + 1 );
        }
        else
        {
            return good( word, dict, 1, pos1 + 1, pos2 );
        }
    }
    else
    {
        if ( word[pos1] != dict[pos2] )
            return 0;
        return good( word, dict, 0, pos1 + 1, pos2 + 1 );
    }
    
    return 0;
}

int doCase( int L, VS dict, string word )
{
    int res = 0;
    
    //
    // DOIT!
    //
    for ( int i = 0; i < dict.size(); i ++ )
    {
        if ( good( word, dict[i], 0, 0, 0 ) )
            res ++;
    }
    
    //
    // RESULT
    //
    
    
    return res;
}

int main()
{
    VI tmp = readMulti<int>();
    int L = tmp[0];
    int D = tmp[1];
    int N = tmp[2];
    VS dict;
    VS words;
    for ( int i = 0; i < D; i ++ )
        dict.push_back( readOne<string>() );
    for ( int i = 0; i < N; i ++ )
        words.push_back( readOne<string>() );
        
//    dump_vec( dict );
//    dump_vec( words );
        
	for (int caseno = 1; caseno <= N; caseno++)
    {
        cout << "Case #" << caseno << ": " << doCase( L, dict, words[caseno-1] ) << endl;
    }

	return 0;
}

