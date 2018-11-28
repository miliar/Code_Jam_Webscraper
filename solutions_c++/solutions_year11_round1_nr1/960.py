#include <stdlib.h>
#include <vector>
#include <iostream>

using namespace std;

int getcommon( int a, int b )
{
        if( a == 0 || b == 0 )
                return 0;

        if( a < 0 )
                a = -a;
        if( b < 0 )
                b = -b;
        while( a!= b)
        {
                if( a > b )
                        a -= b;
                else
                        b -=a;
        }

        return a;
}

int main( int argc, char* argv[])
{
        int T, Pd, Pg, c;
        int64_t N;


        cin >> T;
        for( int i=1;i<=T; ++i )
        {
                cin >> N >> Pd >> Pg;
                if( Pd == 0 ) // D > 0
                {
                        if( Pg == 100 )
                                cout << "Case #" << i << ": Broken" << endl;
                        else
                                cout << "Case #" << i << ": Possible" << endl;
                }
                else if( Pd == 100 )
                {
                        if( Pg == 0 )
                                cout << "Case #" << i << ": Broken" << endl;
                        else
                                cout << "Case #" << i << ": Possible" << endl;
                }
                else if( Pg == 100 )
                {
                        if( Pd < 100 )
                                cout << "Case #" << i << ": Broken" << endl;
                        else
                                cout << "Case #" << i << ": Possible" << endl;
                }
                else if ( Pg == 0 )
                {
                        if( Pd > 0 )
                                cout << "Case #" << i << ": Broken" << endl;
                        else
                                cout << "Case #" << i << ": Possible" << endl;
                }
                else
                {
                        c = getcommon( 100, Pd );
                        if( 100/c > N ) // broken
                        {
                                cout << "Case #" << i << ": Broken" << endl;
                        }
                        else
                        {
                                cout << "Case #" << i << ": Possible" << endl;
                        }
                }
        }

        return 0;
}
