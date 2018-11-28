#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
    int i, j, k;
    int min, max, pos, no;
    int t, tt;
    int v[32];
    char line[128];

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d\n", &tt);
    for (t = 1; t <= tt; ++t)
    {
        gets(line);
        j = 0;
        for (i = 0; i < strlen(line); ++i)
            if (line[i] >= '0' && line[i] <= '9')
                v[j++] = line[i] - '0';
//        for (i = no, j = 0; i > 0; i /= 10)
  //          v[j++] = i % 10;

//        reverse(v, v + j);

        for (i = j - 2, max = v[j - 1]; i >= 0; --i)
            if (v[i] < max)
            {
                max = v[i];
                break;
            }
            else
                max = v[i];

        if (i < 0)
        {
            v[j++] = 0;
            sort(v, v + j);
            for (i = 1; i < j; ++i)
                if (v[i] > 0)
                    break;
            k = v[i];
            v[i] = v[0];
            v[0] = k;
        }
        else
        {
            min = 0x3f3f3f3f;
            pos = i;
            for (k = i + 1; k < j; ++k)
                if (v[k] > v[i] && v[k] <= min)
                {
                    min = v[k];
                    pos = k;
                }
            k = v[i];
            v[i] = v[pos];
            v[pos] = k;
            sort(v + i + 1, v + j);
        }

 //       for (i = k = 0; i < j; ++i)
//            k = k * 10 + v[i];
        printf("Case #%d: ", t);
        for (i = 0; i < j; ++i)
            printf("%d", v[i]);
        printf("\n");
    }
}
