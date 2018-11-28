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
        printf("Case #%d: %s\n", ++cs, k % (1 << n) == (1 << n) - 1 ? "ON" : "OFF");
    }
}
