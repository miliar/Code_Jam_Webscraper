//---------------------------------------------------------------------------
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int T, R, C;

char grid[ 100 ][ 100 ];
bool im;
//---------------------------------------------------------------------------
void calc( void )
{
    int i, j, k;
    im = true;

    for( i=0; i<R; i++ )
    for( j=0; j<C; j++ )    
    {
        if( grid[i][j] == '#' )
        {
            if( grid[i][j+1] == '#' &&
                grid[i+1][j] == '#' &&
                grid[i+1][j+1] == '#' )
            {
                grid[i][j]  = '/';
                grid[i][j+1] = '\\';
                grid[i+1][j] = '\\';
                grid[i+1][j+1] = '/';
            }
            else { im = false; return; }
        }
    }
}
//---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
    int i, j;

    ifstream in( "input.in" );
    ofstream out( "output.out" );

    in >> T;

    for( int t=1; t<=T; t++ )
    {
        in >> R >> C;

        for( i=0; i<R; i++ )
        for( j=0; j<C; j++ )
            in >> grid[ i ][ j ];

         calc();

            out << "Case #" << t << ":" << endl;
         if( !im )
         {
            out << "Impossible" << endl;
         }
         else
         {
               for( i=0; i<R; i++ )
               {
                for( j=0; j<C; j++ )
                    out << grid[ i ][ j ];

                out << endl;
                }
         }

    }

    out.close();
    in.close();

    return 0;
}
//---------------------------------------------------------------------------

