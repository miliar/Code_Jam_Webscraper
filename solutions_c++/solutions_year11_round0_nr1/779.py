#include <stdlib.h>
#include <vector>
#include <iostream>

using namespace std;

struct Node {
        int bot;
        int pos;
};

int getmin( const vector<Node>& v )
{
        char bot0 = 2;
        int pos[2];
        pos[0]=pos[1]=1;
        int T=0, TSum=0;

        for ( size_t i=0; i< v.size(); ++i )
        {
                if( v[i].bot == bot0 )
                {
                        T += abs( v[i].pos - pos[bot0] ) + 1;
                }
                else
                {
                        TSum += T;
                        bot0 = v[i].bot;
                        if( abs(v[i].pos -pos[bot0]) <= T )
                                T = 1;
                        else
                                T = abs(v[i].pos -pos[bot0])-T + 1;
                }

                pos[bot0] = v[i].pos;
        }
        TSum += T;

        return TSum;
}



int main( int argc, char* argv[])
{
        int n, m;

        cin >> n;
        char R;
        vector<Node> nodes;
        for( int i=1; i< n+1; ++i )
        {
                cin >> m;
                nodes.resize(m);
                for( int j =0; j< m; ++j )
                {
                        cin >> R >> nodes[j].pos;
                        nodes[j].bot = ( R == 'B' ? 0 : 1 );
                }
                cout << "Case #" << i << ": " << getmin( nodes) << endl;
        }

        return 0;
}
