#include<iostream>
using namespace std;

int n;
char cd[ 26 ];
string s;

void init() {
     cd[ 'a' - 'a' ] = 'y';
     cd[ 'b' - 'a' ] = 'h';
     cd[ 'c' - 'a' ] = 'e';
     cd[ 'd' - 'a' ] = 's';
     cd[ 'e' - 'a' ] = 'o';
     cd[ 'f' - 'a' ] = 'c';
     cd[ 'g' - 'a' ] = 'v';
     cd[ 'h' - 'a' ] = 'x';
     cd[ 'i' - 'a' ] = 'd';
     cd[ 'j' - 'a' ] = 'u';
     cd[ 'k' - 'a' ] = 'i';
     cd[ 'l' - 'a' ] = 'g';
     cd[ 'm' - 'a' ] = 'l';
     cd[ 'n' - 'a' ] = 'b';
     cd[ 'o' - 'a' ] = 'k';
     cd[ 'p' - 'a' ] = 'r';
     cd[ 'q' - 'a' ] = 'z';
     cd[ 'r' - 'a' ] = 't';
     cd[ 's' - 'a' ] = 'n';
     cd[ 't' - 'a' ] = 'w';
     cd[ 'u' - 'a' ] = 'j';
     cd[ 'v' - 'a' ] = 'p';
     cd[ 'w' - 'a' ] = 'f';
     cd[ 'x' - 'a' ] = 'm';
     cd[ 'y' - 'a' ] = 'a';
     cd[ 'z' - 'a' ] = 'q';
}

inline char googl( char c ) { if( c == ' ' ) return ' '; else return cd[ c - 'a' ]; }

int main() {
    cin >> n;

    init();
    getline( cin, s );

    for( int c = 0; c < n; c++ ) {
         getline( cin, s );

         cout << "Case #" << ( c+1 ) << ": ";
         for( int i = 0; i < s.length(); i++ ) {
              cout << googl( s[i] );
         }
         cout << endl;
    }

    return 0;
}
