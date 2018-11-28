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
typedef long long lint;
typedef vector<int> vi;
typedef vector<vi> vvi;
int main()
{
	ifstream input( "test.in" );
	ofstream output( "test.out" );
    int N; input >> N;
    for( int z = 0; z < N; ++z )
    {
        int n, A, B, C, D, x0, y0, M;
        input >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        lint result = 0;
        lint X = x0, Y = y0;
        vvi x(3, vi(3));
        ++x[X % 3][Y % 3];
        for( int i = 1; i < n; ++i )
        {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            ++x[X % 3][Y % 3];
        }
        int A1 = 0, A2 = 0, A3 = 0;
        for( int a = 0; a < 9; ++a )
        {
            A1 = x[a / 3][a % 3];
            if ( A1 > 0 )
                for( int b = a; b < 9; ++b )
                {
                    A2 = x[b / 3][b % 3] - (a == b);
                    if ( b == a && A1 > 1 ||
                        b > a && A2 > 0 )
                        for( int c = b; c < 9; ++c )
                        {
                            A3 = x[c / 3][c % 3] - (c == b) - (c == a);
                            if ( c == a && A1 > 2 ||
                                c == b && A2 > 1 ||
                                c > b && A3 > 0 )
                            {
                                lint current = A1 * A2;
                                if ( a == b )
                                    current /= 2;
                                current *= A3;
                                if ( c == a )
                                    current /= 3;
                                else if ( c == b )
                                    current /= 2;
                                int x1 = a / 3, y1 = a % 3;
                                int x2 = b / 3, y2 = b % 3;
                                int x3 = c / 3, y3 = c % 3;
                                if ( (x1 + x2 + x3) % 3 == 0 && (y1 + y2 + y3) % 3 == 0 )
                                    result += current;
                            }
                        }
                }
        }
        output << "Case #" << z + 1 << ": " << result << endl;
    }
	return 0;
}