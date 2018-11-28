#include <iostream>
using namespace std;

int main()
{
    int time;
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    
    scanf("%d", &time);
    for (int i = 0; i < time; ++i) {
        int n, k; scanf("%d%d", &n, &k); n = (1 << n) - 1;
        printf("Case #%d: ", i + 1);
        if ((k & n) == n) printf("ON\n");
        else printf("OFF\n");
    }
    
    return 0;
}
