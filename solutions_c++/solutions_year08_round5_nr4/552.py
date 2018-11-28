#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <queue>
#include <vector>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
int main()
{
	ifstream input( "test.in" );
	ofstream output( "test.out" );
    int N; input >> N;
    for( int n = 0; n < N; ++n )
    {
        int result = 0;
        int H, W, R; input >> H >> W >> R;
        vvi M(H + 2, vi(W + 2));        
        for( int i = 0; i < R; ++i )
        {
            int x, y; input >> x >> y;
            M[x - 1][y - 1] = -1;
        }
        M[0][0] = 1;
        for( int x = 0; x < H; ++x )
            for( int y = 0; y < W; ++y )
                if ( M[x][y] != -1 )
                {
                    if ( M[x + 1][y + 2] != -1 )
                        M[x + 1][y + 2] = (M[x + 1][y + 2] + M[x][y]) % 10007;
                    if ( M[x + 2][y + 1] != -1 )
                        M[x + 2][y + 1] = (M[x + 2][y + 1] + M[x][y]) % 10007;
                }
        output << "Case #" << n + 1 << ": " << M[H - 1][W - 1] << endl;
    }
	return 0;
}