#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

#include <boost/bind.hpp>

using namespace std;

struct cell
{
    cell() : a(-1), d(-1), c(0) {}

    int a;
    int d;
    char c; 
};
        
vector<vector<cell> > vec;

cell & v(int i, int j) { return vec.at(i).at(j); }

char calc(int i, int j)
{
    char & c = v(i, j).c;
    if ( c == 0 )
    {
        int d = v(i, j).d;
        if (d == 0)
            c = calc(i-1, j);
        else if (d == 1)
            c = calc(i, j-1);
        else if (d == 2)
            c = calc(i, j+1);
        else if (d == 3)
            c = calc(i+1, j);
    }

    return c;
}

int main()
{
    int T;
    cin >> T;

    for ( int n = 0 ; n != T; ++n )
    {
        int H, W;
        cin >> H >> W;

        vec.clear();
        vec.resize(H, vector<cell>(W));

        for (int i = 0; i != H; ++i)
            for (int j = 0; j != W; ++j)
                cin >> v(i,j).a;

        char C = 'a';

        for (int i = 0; i != H; ++i)
        {
            for (int j = 0; j != W; ++j)
            {
                int a = v(i, j).a;
                int dir = -1;

                if (i > 0 && a > v(i-1, j).a )
                    dir = 0, a = v(i-1, j).a; 
                    
                if (j > 0 && a > v(i, j-1).a )
                    dir = 1, a = v(i, j-1).a; 

                if (j < W-1 && a > v(i, j+1).a )
                    dir = 2,   a = v(i, j+1).a; 
                
                if (i < H-1 && a > v(i+1, j).a )
                    dir = 3,   a = v(i+1, j).a; 

                v(i, j).d = dir;
                
                if (dir == -1)
                    v(i,j).c = C++;
                
            }

        }

        for (int i = 0; i != H; ++i)
            for (int j = 0; j != W; ++j)
                calc(i, j);

        vector<char> m(26, 0);

        C = 'a';

        for (int i = 0; i != H; ++i)
            for (int j = 0; j != W; ++j)
            {
                char c = v(i,j).c - 'a';
                if( m[c] == 0 )
                    m[c] = C++;
            }

        cout << "Case #" << (n+1) << ":\n";
        for (int i = 0; i != H; ++i)
            for (int j = 0; j != W; ++j)
                cout << m.at(v(i,j).c - 'a') << (j < W-1 ? " " : "\n");
    }
}

