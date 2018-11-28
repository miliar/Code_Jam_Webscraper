#include <stdio.h>
#include <map>
#include <string>

using namespace std;

char    buf[101];

void
zestaw()
{
    int     neng;
    int     nque;
    int     nused;
    int     nswitch = 0;
    static int  count = 1;

    map<string, bool>     used;

    scanf("%d\n", &neng);
    for (int it = 0; it < neng; ++it)
    {
        scanf("%[0-9A-Za-z ]\n", buf);
//        scanf("%[0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz]", buf);
//        scanf("%[^w]", buf);
        used[buf] = false;
    }

    scanf("%d\n", &nque);

    nused = 0;
    for (int it = 0; it < nque; ++it)
    {
        scanf("%[0-9A-Za-z ]\n", buf);
        if (!used[buf])
        {
            used[buf] = true;
            ++nused;
        }
        if (nused == neng)
        {
            /* reset, we switch to other than current, clear all except the
             * current one which will become the only currently used */
            ++nswitch;
            nused = 1;
            for (map<string, bool>::iterator iter = used.begin();
                iter != used.end();
                ++iter)
            {
                iter->second = false;
            }
            used[buf] = true;
        }
    }

    printf("Case #%d: %d\n", count++, nswitch);
}

int
main()
{
    int     ile;

    scanf("%d", &ile);

    while(ile--)
    {
        zestaw();
    }

    return 0;
}
