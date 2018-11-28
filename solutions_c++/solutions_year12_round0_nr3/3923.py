#include <bitset>
#include <cstdio>
#include <cmath>
#include <set>

using namespace std;

int main()
{
    int cases;

    scanf("%d", &cases);

    for ( int ii = 1; ii <= cases; ii++ )
    {
        int result = 0;
        int x;
        int y;
        int i_len;

        scanf("%d %d", &x, &y);

        for ( int i = x; i <= y; i++ )
        {
            i_len = (int)log10(i) + 1;
            set<int> S;

            for ( int j = 1; j < i_len; j++ )
            {
                int mult = (int)pow(10, j);
                int swapped = ((i % mult) * (int)pow(10, i_len - j)) + (i / mult);

                if ( swapped >= i )
                    continue;

                if ( ((int)log10(swapped) + 1) != i_len )
                    continue;

                if ( x <= swapped && swapped <= y )
                    S.insert(swapped);

            }

            result += S.size();
        }

        printf("Case #%d: %d\n", ii, result); 
    }

    return 0;
}
