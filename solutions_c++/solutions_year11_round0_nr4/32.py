#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int teste, t;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        int count;
        scanf("%d", &count);
        int i;
        int out = 0;
        for (i = 0; i < count; i++)
        {
            int p;
            scanf("%d", &p);
            if ((i+1) != p)
                out++;
        }
        printf("Case #%d: %lf\n", t+1, (double)out);
    }
    return 0;
}
