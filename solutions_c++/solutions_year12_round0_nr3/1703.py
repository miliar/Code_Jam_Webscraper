#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for ( int t=1 ; t<=T ; ++t )
    {
        int a, b;
        scanf("%d %d", &a, &b);

        int res = 0;
        for ( int i=a ; i<=b ; ++i )
        {
            int c = i;
            int d = (int)pow(10.0, floor(log10(1.0*i)));
            do 
            {
                if ( c >= d && c > i && c <= b) 
                {
                    ++res;
                }
                c = (c % 10) * d + c / 10;
            } while ( c != i );
        }
        printf("Case #%d: %d\n", t, res);
    }
    return 0;
}
