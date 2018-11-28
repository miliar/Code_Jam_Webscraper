#include <stdio.h>
#include <vector>
#include <string>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;


int main()
{
    int T, test;
    scanf("%d", &T);
    for (test = 1;test<=T;test++)
    {
        int N, i, j, res = 0, x[40];
        scanf("%d\n", &N);
        for (i=0;i<N;i++)
        {
            x[i] = -1;
            for (j=0;j<N;j++)
            {
                char k;
                scanf("%c", &k);
                if (k=='1') x[i] = j;
            }
            getc(stdin);
        }

        for (i=0;i<N-1;i++)
        {
            int MinI = i;
            for (j=i;j<N;j++)
            {
                if (x[j]<=i)
                {
                    MinI = j;
                    break;
                }
            }
            if (MinI>i)
            {
                res+=MinI-i;
                for (j=MinI;j>i;j--)
                    swap(x[j], x[j-1]);
            }
        }
        printf("Case #%d: %d\n", test, res);


    }

    return 0;
}
