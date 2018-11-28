/**

*/

#include <stdio.h>

const int MAX_SNAPPERS = 50;


int
main(
    int argc,
    wchar_t* argv[]
)
{
    int t = 0;
    int n = 0;
    int k = 0;
    scanf("%d", &t);

    int snappers[MAX_SNAPPERS];

    for (int i = 0; i < MAX_SNAPPERS; i++)
    {
        snappers[i] = 0;
    }

    for (int i = 0; i < t; i++)
    {
        scanf("%d %d", &n, &k);
        if (0 == k)
        {
            printf("Case #%d: OFF\n", i + 1);
        }
        else
        {
            int power = 1 << n;
            if (0 == (k + 1) % power)
            {
                printf("Case #%d: ON\n", i + 1);
            }
            else
            {
                printf("Case #%d: OFF\n", i + 1);
            }
        }
    }
    return 0;
}
