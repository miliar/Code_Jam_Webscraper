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
template<typename T> string ToString( T x )
{
	ostringstream S; S << x; return S.str();
}
string calc( int c, int N, int M, int A )
{
    int x1 = 0;
    for( int x2 = 0; x2 <= N; ++x2 )
        for( int x3 = 0; x3 <= N; ++x3 )
            for( int y1 = 0; y1 <= M; ++y1 )
                for( int y2 = 0; y2 <= M; ++y2 )
                    for( int y3 = 0; y3 <= M; ++y3 )
                        if ( abs(static_cast<int>(-x2*y1 + x3*y1 + x1*y2 - x3*y2 - x1*y3 + x2*y3)) == A )
                        {
                            return string("Case #") + ToString(c + 1) + ": " + 
                                ToString(x1) + " " + ToString(y1) + " " +
                                ToString(x2) + " " + ToString(y2) + " " +
                                ToString(x3) + " " + ToString(y3);
                        }
    return string(string("Case #") + ToString(c + 1) + ": IMPOSSIBLE");
}
int main()
{
	ifstream input( "test.in" );
	ofstream output( "test.out" );
    int C; input >> C;
    for( int c = 0; c < C; ++c )
    {
        int N, M, A; input >> N >> M >> A;
        output << calc(c, N, M, A) << endl;
    }        
	return 0;
}