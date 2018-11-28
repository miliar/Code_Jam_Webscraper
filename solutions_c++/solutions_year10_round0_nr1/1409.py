#include <cstdio>
using namespace std;

int t, brt, n, clicks;

int main ()
{
    scanf ("%d", &t);
    while ( t-- )
    {
        scanf ("%d%d", &n, &clicks);
        printf ("Case #%d: ", ++brt);
        if ( (clicks % (1 << n)) == ((1 << n)-1) ) printf ("ON\n");
        else printf ("OFF\n");
    }
    return 0;
}
