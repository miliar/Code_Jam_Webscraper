#include <iostream>

using namespace std;

int T, N;
int val[2000];

int main( int argc, char* argv[])
{
        cin >> T;
        for( int i=1; i< T+1; ++i )
        {
                cin >> N;
                for( int j=0; j< N; ++j )
                        cin >> val[j];
                sort(val, val+N);

                int rlt = val[1];
                for( int j=2; j< N; ++j )
                        rlt = rlt ^ val[j];

                if( rlt != val[0] )
                {
                        cout << "Case #" << i << ": NO" << endl;
                }
                else
                {
                        rlt = 0;
                        for( int j=1; j< N; ++j )
                                rlt += val[j];
                        cout << "Case #" << i << ": " << rlt << endl;
                }
        }

        return 0;
}
