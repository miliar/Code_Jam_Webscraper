#include <stdio.h>
#include <set>
#include <vector>
#include <string>

const int MAXL = 20;
const int MAXD = 5002;

int L, D, N;

typedef std::set< char > CCharSet;
typedef std::vector< CCharSet > CPattern;
typedef std::set< std::string > CWords;

CWords words;

int main()
{
   // freopen( "in.txt", "rt", stdin );

    scanf( "%d %d %d\n", &L, &D, &N );
    for( int i = 0; i != D; ++ i )
    {
        char str[ MAXL + 10 ];
        gets( str );
        std::string w = str;
        words.insert( w );
    }
    for( int test = 1; test <= N; ++ test )
    {
        char str[ 10000 ];
        gets( str );

        CPattern pattern;
        int pos = 0;
        for( int i = 0; i != L; ++ i )
        {
            CCharSet cur;
            if( str[ pos ] == '(' )
            {
                ++ pos;
                for( ; str[ pos ] != ')'; ++ pos )
                {
                    cur.insert( str[ pos ] );
                }
            }
            else
                cur.insert( str[ pos ] );
            ++ pos;
            pattern.push_back( cur );
        }

        CWords tmp = words;
        for( int i = 0; i != L; ++ i )
        {
            for( CWords::iterator j = tmp.begin(); j != tmp.end(); )
            {
                if( pattern[i].find( (*j)[ i ] ) == pattern[i].end() )
                    j = tmp.erase( j );
                else
                    ++ j;
            }
        }

        int count = tmp.size();
        printf( "Case #%d: %d\n", test, count );
    }
    return 0;
}