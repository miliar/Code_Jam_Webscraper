#include <iostream>
#include <bitset>
#include <vector>
using namespace std;

bitset<11>  B,  MN;

vector<pair<int, bool> > V[100];

int main() {
    
    freopen( "B-small-attempt0.in", "r", stdin );
    freopen( "ans.txt", "w", stdout );
    
    int     T,  M,  N,  x,  y,  z;
    cin >> T;
    
    for( int t = 1; t <= T; t++ ) {
        
        cin >> N >> M;
        for( int i = 0; i < M; ++i ) {
            cin >> x;
            V[i].resize( x );
            for( int j = 0; j < x; ++j ) {
                cin >> y >> z;
                V[i][j] = make_pair( y, z );
            }
        }
        
        MN.set();
        bool    found = false;
        
        for( int i = 0; i < 1 << N; ++i ) {
            B = i<<1;
            if( B.count() >= MN.count() )
                continue;
            bool    yes = true;
            for( int k = 0; k < M; ++k ) {
                bool    fit = false;
                for( int j = 0; j < V[k].size(); ++j ) {
                    if( B[V[k][j].first] == V[k][j].second ) {
                        fit = true;
                        break;
                    }
                }
                if( !fit ) {
                    yes = false;
                    break;
                }
            }
                if( yes ) {
                    if( B.count() < MN.count() ) {
                        MN = B;
                        found = true;
                    }
                }
        }
        
        cout << "Case #" << t << ": ";
        
        if( !found )    puts( "IMPOSSIBLE" );
        else  {
            for( int i = 1; i <= N; ++i )
                cout << MN[i] << ' ';
        }   puts( "" );
    
    }
    
}
