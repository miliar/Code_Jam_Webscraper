#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define PI 3.1415926535897932384626433832795

const int size = 1000;
const int strsize = 5;

char st[size], rule[size][strsize], ban[size][strsize], invoke[size];

int main()
{
    int tc, t, i, j, c, d, k, len, n;
    bool flag;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf("%d", &tc);
    for (t = 0; t < tc; t++)
    {
        scanf("%d", &c);
        for (i = 0; i < c; i++)
            scanf("%s", rule[i]);
        scanf("%d", &d);
        for (i = 0; i < d; i++)
            scanf("%s", ban[i]);
        scanf("%d", &n);
        st[0] = '$';
        st[1] = '#';
        len = 2;
        scanf("%s", invoke);
        for (i = 0; i < n; i++)
        {
            st[len] = invoke[i];
            len++;
            flag = true;
            for (j = 0; j < c; j++)
                if ((st[len - 2] == rule[j][0] && st[len - 1] == rule[j][1]) || (st[len - 2] == rule[j][1] && st[len - 1] == rule[j][0]))
                {
                    len--;
                    st[len - 1] = rule[j][2];
                    flag = false;
                    break;
                }
            if (flag)
                for (j = 0; j < d; j++)
                    for (k = 2; k < len - 1; k++)
                        if ((st[len - 1] == ban[j][0] && st[k] == ban[j][1]) || (st[len - 1] == ban[j][1] && st[k] == ban[j][0]))
                        {
                            len = 2;
                            break;
                        }
        }
        printf("Case #%d: [", t + 1);
        for (i = 2; i < len - 1; i++)
            printf("%c, ", st[i]);
        if (len > 2)
            printf("%c", st[len - 1]);
        printf("]\n");
    }

    return 0;
}
