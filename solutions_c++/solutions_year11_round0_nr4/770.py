#include <iostream>

using namespace std;

int N, T;

int main( int argc, char* argv[])
{
        cin >> T;
        for( int i=1; i<= T; ++i )
        {
                cin >> N;
                int nNotInPlace = 0, num;
                for ( int j=1; j<= N; ++j )
                {
                        cin >> num;
                        if( num != j )
                                ++ nNotInPlace;
                }
                cout << "Case #" << i << ": " << nNotInPlace << ".000000" << endl;
        }

        return 0;
}
