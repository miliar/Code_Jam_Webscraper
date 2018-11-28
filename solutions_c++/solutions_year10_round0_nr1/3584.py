#include<iostream>
using namespace std;

int n, k;
int main()
{
    int t;
    int cs = 0;
    freopen("A_L.in", "r", stdin);
    freopen("A_L.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d", &n, &k);
        if( k % (1 << n) == (1 << n) - 1 )
        {
            printf("Case #%d: ON\n", ++cs );
        }
        else
        {
            printf("Case #%d: OFF\n", ++cs );
        }
    }
}
