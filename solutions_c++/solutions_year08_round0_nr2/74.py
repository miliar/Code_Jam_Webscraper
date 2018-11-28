#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

typedef size_t s_t;

int read_n( std::istream& is )
{
        int N;
        is >> N;
        string dummy;
        getline( cin, dummy );
        return N;
}

int maketime( int h, int m)
{
        return h*60+m;
}

int main()
{
        string dummy;
        int N = read_n(cin);

        for( s_t i = 0 ; i < N ; i++ ) {
                int T = read_n( cin );
                int NA, NB;
                cin >> NA >> NB;
                getline( cin, dummy );
                //cerr << NA << "+" << NB << endl;
                
                map< int, vector< int > > q; // 0 Adep, 1 Aarr, 2 Bdep, 3 Barr

                for( int j = 0 ; j < NA ; j++ ) {
                        int dh, dm, ah, am;
                        string s;
                        getline( cin, s );
                        sscanf( s.c_str(), "%2d:%2d %2d:%2d", &dh, &dm, &ah, &am );
                        //cerr << dh << ":" << dm << ", " << ah << ":" << am << endl;
                        //cerr << maketime( dh, dm ) << "; " << maketime( ah, am ) << endl;
                        q[maketime( dh, dm )].push_back( 0 );
                        q[maketime( ah, am )+T].push_back( 1 );
                }
                
                for( int j = 0 ; j < NB ; j++ ) {
                        int dh, dm, ah, am;
                        string s;
                        getline( cin, s );
                        sscanf( s.c_str(), "%2d:%2d %2d:%2d", &dh, &dm, &ah, &am );
                        //cerr << dh << ":" << dm << ", " << ah << ":" << am << endl;
                        //cerr << maketime( dh, dm ) << "; " << maketime( ah, am ) << endl;
                        q[maketime( dh, dm )].push_back( 2 );
                        q[maketime( ah, am )+T].push_back( 3 );
                }

                int Aw = 0;
                int Bw = 0;
                int Ar = 0;
                int Br = 0;
                for( map<int,vector<int> >::const_iterator j = q.begin() ; j !=q.end(); ++j ) {
                        const vector<int>& v = (*j).second;

                        for( s_t k = 0 ; k < v.size() ; k++ ) {
                                switch( v[k] ) {
                                case 1:
                                        Bw++;
                                        //cerr << "event 1 " << Aw << " " << Bw << " " << Ar << " " << Br << endl;
                                        break;
                                case 3:
                                        Aw++;
                                        //cerr << "event 3 " << Aw << " " << Bw << " " << Ar << " " << Br << endl;
                                        break;
                                }
                        }

                        for( s_t k = 0 ; k < v.size() ; k++ ) {
                                switch( v[k] ) {
                                case 0:
                                        if( 0 < Aw ) { Aw--; } else { Ar++; }
                                        //cerr << "event 0 " << Aw << " " << Bw << " " << Ar << " " << Br << endl;
                                        break;
                                case 2:
                                        if( 0 < Bw ) { Bw--; } else { Br++; }
                                        //cerr << "event 2 " << Aw << " " << Bw << " " << Ar << " " << Br << endl;
                                        break;
                                }
                        }
                }

                cout << "Case #" << (i+1) << ": " << Ar << " " << Br << endl;
        }

        return 0;
}
