#include <cstdio>
using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    for(int caso = 1; caso <= t; caso++) {
        int n, k;
        scanf("%d %d", &n, &k);
        int i = 0;
        while(k & (1 << i)) {

            i++;
        }
        char off[] = "OFF";
        char on[] = "ON";
        char* out;
        out = (i >= n) ? on : off;
        printf("Case #%d: %s\n", caso, out);
    }
    return 0;
}

