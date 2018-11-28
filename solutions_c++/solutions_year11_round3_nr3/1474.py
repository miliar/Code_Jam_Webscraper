//---------------------------------------------------------------------------
#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int N, L, H;
int fr[ 100000 ];

bool im;
int freq;
//---------------------------------------------------------------------------
void calc( void )
{
    int i, f, j, k, m;

    im = false;

/*   for( i=0; i<N; i++ )
    for( j=i+1; j<N; j++ )
    {
        if( ( fr[i] % fr[j]) &&
            ( fr[j] % fr[i]) )
        {
            im = false; return;
        }
    }

                */
    for( f=L; f<=H; f++ )
    {
        for( i=0; i<N; i++ )
        {
            if( fr[i] % f != 0 &&
                f % fr[i] != 0 )
            {
                break;
            }
        }

        if( i == N )
        {
            freq = f;
            im = true;
            break;
        }
    }



}
//---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
    int T, i, j;

    ifstream in( "C-small-attempt0.in" );
    ofstream out( "output2.out" );

    in >> T;

    for( int t=1; t<=T; t++ )
    {
        in >> N >> L >> H;

        for( i=0; i<N; i++ ) in >> fr[ i ];

        calc();

        out << "Case #" << t << ": ";
        if( !im ) out << "NO" << endl;
        else
        {
            out << freq << endl;

        }

        asm nop;
    }

    out.close();
    in.close();

    return 0;
}
//---------------------------------------------------------------------------

