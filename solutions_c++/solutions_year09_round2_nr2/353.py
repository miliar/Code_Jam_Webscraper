#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

int t, k;
char a[30];
char b[30];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d\n", &t);
    for (int tt = 1; tt <= t; tt ++)
    {
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        gets(a);

        k = strlen(a);

        for (int i = 0; i < k; i ++) b[i] = a[i];
        next_permutation(b, b + k);

        bool good = true;

        for (int i = 0; i < k; i ++)
            if (a[i] < b[i]) break; else
            if (a[i] > b[i]) 
            {
                good = false;
                break;
            }

        int x = 0;

        for (int i = 0; i < k; i ++)
            if (a[i] == b[i]) x ++;

        if (x == k) good = false;

        if (good) printf("Case #%d: %s\n", tt, b); else
        {
            b[k] = '0';
            sort(b, b + k + 1);
            for (int i = 1; i < k + 1; i ++)
                if (b[i] != '0')
                {
                    swap(b[0], b[i]);
                    break;
                }
                printf("Case #%d: %s\n", tt, b);
        }
    }
    return 0;
}