#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

const int N = 10000;
int a[N];
int b[N];
char mark[N];

int main(int argc, char * argv[])
{
    int ca;
    scanf("%d", &ca);
    for (int tc = 1; tc <= ca; tc++)
    {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            b[i] = a[i];
        }

        sort(b, b + n);
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (a[i] == b[j])
                {
                    a[i] = j;
                    break;
                }
            }
        }

        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] == i) count ++;
        }

        printf("Case #%d: %.6f\n", tc, 1.0 * (n - count));
    }
    return 0;
}

