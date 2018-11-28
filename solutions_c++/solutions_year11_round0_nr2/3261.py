# include <cstdio>
# include <iostream>
# include <cstring>
# include <set>
# include <vector>
# include <map>

using namespace std;

vector <char> rijec;
set < pair<char,char> > pretvorbeS;
map < pair<char,char>, char > pretvorbe;
set < pair<char,char> > nePodnose;

int M;

char query[ 110 ];

int main( void ){
    int N;
    char c;
    int t;
    scanf( "%d", &N );
    int sol;
    int id = 0;
    while( N-- ){
        id++;
        scanf( "%d", &M );
        char a,b,c;
        pretvorbeS.clear();
        pretvorbe.clear();
        nePodnose.clear();
        rijec.clear();
        for( int i = 0 ; i < M ; ++i ){
            scanf( " %c%c%c", &a, &b, &c );
            pretvorbeS.insert( make_pair( a, b ) );
            pretvorbeS.insert( make_pair( b, a ) );
            pretvorbe[ make_pair( a, b ) ] = c;
            pretvorbe[ make_pair( b, a ) ] = c;
        }
        scanf( "%d", &M );
        for( int i = 0 ; i < M ; ++i ){
            scanf( " %c%c", &a, &b );
            nePodnose.insert( make_pair( a, b ) );
            nePodnose.insert( make_pair( b, a ) );
        }
        scanf( "%d %s", &M, query );
        char last = 0;
        for( int i = 0; i < M ; ++i ){
            if( pretvorbeS.find( make_pair( last, query[ i ] ) ) != pretvorbeS.end() ){
                rijec.pop_back();
                rijec.push_back( pretvorbe[ make_pair( last, query[ i ] ) ] );
            } else {
                rijec.push_back( query[ i ] );
            }
            for( int j = 0 ; j < rijec.size() - 1 ; ++j ){
                if( nePodnose.find( make_pair( rijec[ j ], rijec.back() ) ) != nePodnose.end() ){
                    rijec.clear();
                    break;
                }
            }
            if( rijec.size() ){
                last = rijec.back();
            } else last = 0;
        }
        printf( "Case #%d: [", id );
        for( int i = 0 ; i < rijec.size() ; ++i ){
            printf( "%c%s", rijec[ i ], ( i + 1 != rijec.size() ) ? ", " : "" );
        }
        printf( "]\n" );
    }
    return 0;
}
