//---------------------------------------------------------------------------
#include <iostream>
#include <fstream>

using namespace std;

int T, N;

struct job {
    int bp, q;
};

job B[ 100 ], O[ 100 ];
int b, o;
long int m;
int Bpos, Opos;
//---------------------------------------------------------------------------
void find_moves()
{
    int cb=0, co=0, cm=0;
    bool push;

    Bpos = 1; Opos = 1;
    for( m=0; (cb<b)||(co<o); m++ )
    {
        push = false;

        if( cb < b )
        {
            if( Bpos < B[ cb ].bp ) Bpos++;
            else if( Bpos > B[ cb ].bp ) Bpos--;
            else
            {
                if( cm == B[ cb ].q ) { cb++; cm++; push=true; }
            }
        }

        if( co < o )
        {
            if( Opos < O[ co ].bp ) Opos++;
            else if( Opos > O[ co ].bp ) Opos--;
            else
            {
                if( !push && cm == O[ co ].q ) { co++; cm++; }
            }
        }

    }
}
//---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
    int i, j, k, p , t;
    char r;

    ifstream in ( "bottrust.in" );
    ofstream out( "bottrust.out" );

    in >> T;

    for( t=0; t<T; t++ )
    {
        b = 0; o = 0;

        in >> N;
        for( i=0; i<N; i++)
        {
            in >> r >> p;

            switch( r )
            {
                case 'O': O[o].bp = p; O[o].q = i; o++; break;
                case 'B': B[b].bp = p; B[b].q = i; b++; break;
                default: cout << "ERROR!!" << endl;
            }
        }

        find_moves();

        out << "Case #" << t+1 << ": " << m << endl;

    }

    out.close();
    in.close();

    return 0;
}
//---------------------------------------------------------------------------
