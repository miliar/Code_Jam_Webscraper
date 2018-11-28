#include <algorithm>
#include <iostream>
#include <vector>

int solve() {
    int tests = 0;
    std::cin >> tests;

    for( int test = 1; test <= tests; ++test )
    {
        int a = 0, b = 0;
        std::cin >> a >> b;

        int ans = 0;

        for( int x = a; x <= b; ++ x )
        {
            int p = 1, n = 0;
            for( int i = x; i > 0; i /= 10 )
            {
                p *= 10;
                ++ n;
            }
            p /= 10;

            std::vector<int> r;

            int y = x;
            for( int i = 1; i < n; ++ i )
            {
                y = y/10 + p * (y % 10 );
                if( y >= p && a <= y && y <= b && y > x && std::find( r.begin(), r.end(), y ) == r.end() )
                {
                    r.push_back( y );
                    ++ ans;
                }
            }
        }

        std::cout << "Case #" << test << ": " << ans << std::endl;
    }
    return 0;
}

int main()
{
    return solve();
}

