#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

int t, n, k;

int main()
{
    int i, tag;

    scanf("%d", &t);
    for (i = 0; i < t; i++) {
        scanf("%d %d", &n, &k);
        tag = 1;
        while (n-- > 0) {
            if ((k & 1) == 0)
                tag = 0;
            k >>= 1;
        }    
        printf("Case #%d: %s\n", i + 1, tag ? "ON" : "OFF");
    }

    return (0);
}

