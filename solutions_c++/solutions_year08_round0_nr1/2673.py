#include <fstream>
#include <iostream>
#include <cstring>
#include <deque>
using namespace std;

int main()
{
    ifstream infile( "input" );
    deque<char*> engines;
    deque<int> cnt;
    char temp[101];
    unsigned int n, s, q;
    unsigned int i, j, k, l;
    unsigned int shifts;

    infile>>n;

    for( i = 0; i < n; ++i )
    {
        shifts = 0;

        infile>>s;
        infile.getline( temp, 101 );
        //cout<<"Engines: "<<s<<endl;

        cnt.resize( s );

        for( j = 0; j < s; ++j )
        {
            infile.getline( temp, 101 );
            engines.push_back( new char[101] );
            strncpy( engines.back(), temp, 101 );
            cnt[ j ] = -1;
            //cout<<"Finished reading: "<<temp<<endl;
        }

        infile>>q;
        infile.getline( temp, 101 );
        //cout<<"Queries: "<<q<<endl;

        for( j = 0; j < q; ++j )
        {
            infile.getline( temp, 101 );
            //cout<<"Finished reading: "<<temp<<endl;

            for( k = 0; k < s; ++k )
            {
                if( strncmp( temp, engines[ k ], 100 ) == 0 )
                {
                    if( cnt[ k ] == -1 )
                    {
                        cnt[ k ] = j;
                        if( *( min_element( cnt.begin(), cnt.end() ) ) != -1 )
                        {
                            //cout<<"Switch! Element: "<<j<<", "<<temp<<endl;
                            ++shifts;

                            for( l = 0; l < s; ++l )
                            {
                                cnt[ l ] = -1;
                            }
                            cnt[ k ] = j;
                        }
                    }
                    break;
                }
            }
        }

        cout<<"Case #"<<i+1<<": "<<shifts<<endl;

        for( j = 0; j < s; ++j )
        {
            delete[] engines[ j ];
        }
        engines.clear();
    }

    infile.close();

    return 0;
}
