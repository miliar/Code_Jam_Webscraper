# include <cstdio>
# include <iostream>
# include <cstring>
# include <vector>

using namespace std;

vector <int> orange, blue;
vector <char> which;

int M;


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
        int i = 0;
        sol = 0;
        int posO = 1;
        int posB = 1;
        int nextO, nextB;
        nextO = 0;
        nextB = 0;
        orange.clear();
        which.clear();
        blue.clear();
        while( i < M ){
            scanf( " %c %d", &c, &t );
            if( c == 'O' ) orange.push_back( t );
            if( c == 'B' ) blue.push_back( t );
            which.push_back( c );
            i++;
        }
        orange.push_back( 100000 );
        blue.push_back( 100000 );
        int naredba = 0;
        int sol = 0;
        while( naredba < M ){
            sol++;
            bool pritisnuo = false;
            if( posO != orange[ nextO ] ){
                if( posO > orange[ nextO ] )
                    posO--;
                else posO++;
            } else {
                if( which[ naredba ] != 'B' ){
                    naredba++;
                    nextO++;
                    pritisnuo = true;
                }
            }
            if( posB != blue[ nextB ] ){
                if( posB > blue[ nextB ] )
                    posB--;
                else posB++;
            } else if( ! pritisnuo ){
                if( which[ naredba ] != 'O' ){
                    naredba++;
                    nextB++;
                }
            }
        }
        printf( "Case #%d: %d\n", id, sol );
    }
    return 0;
}
