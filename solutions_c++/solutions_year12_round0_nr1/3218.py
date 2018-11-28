#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

char swp[] = { 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l',
               'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
string input;
int t;

int main(){

    FILE* out = fopen( "output.txt", "w" );

    scanf( "%d%*c", &t );

    for( int a = 1; a <= t; a++ ){
        getline( cin, input );

        if( a != 1 ) fprintf( out, "\n" );
        fprintf( out, "Case #%d: ", a );

        for( int b = 0; b < input.size(); b++ ){
            if( input.at( b ) == ' ' ) fprintf( out, " " );
            else fprintf( out, "%c", swp[ input.at( b ) - 'a' ] );
        }
    }

}
