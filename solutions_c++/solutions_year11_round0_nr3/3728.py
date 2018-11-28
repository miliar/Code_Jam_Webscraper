//---------------------------------------------------------------------------
#include <iostream>
#include <fstream>

using namespace std;

int T, N;
long int mmin, num, sum;
long int result;
//---------------------------------------------------------------------------
int main( void )
{
    int i,j , n, k, t;

    ifstream  in( "candysplit.in" );
    ofstream out( "candysplit.out" );

    in >> T;

    for( t=0; t<T; t++ )
    {
        in >> N;
        mmin = 99999999;
        result = 0;
        sum = 0;

        for( n=0; n<N; n++ )
        {
            in >> num;

            if( mmin > num ) mmin = num;
            sum += num;

            result = result ^ num;
        }

        out << "Case #" << t+1 << ": ";

        if( result != 0 ) out << "NO" << endl;
        else out << sum - mmin << endl;
    }

    in.close();
    out.close();

    return 0;
}
//---------------------------------------------------------------------------
 