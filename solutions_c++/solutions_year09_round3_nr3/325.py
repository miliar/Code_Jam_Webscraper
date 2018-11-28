#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    int T, test;
    scanf("%d", &T);
    for (test=1;test<=T;test++)
    {
        int P, Q, x[100], Min = -1, i;
        scanf("%d%d", &P, &Q);
        for (i = 0;i<Q;i++)
        {
            scanf("%d", &x[i]);
            x[i]--;
        }

        sort(x, x+Q);
        do
        {
            bool st[100];
            int sum = 0, j;

            for (i=0;i<P;i++) st[i] = true;
            for (i=0;i<Q;i++)
            {
                st[x[i]] = false;
                for (j=x[i]-1;j>=0 && st[j];j--)
                    sum++;
                for (j=x[i]+1;j<P && st[j];j++)
                    sum++;
            }
            if (Min==-1 || sum < Min) Min = sum;
        }
        while(next_permutation(x, x+Q) );
        if (Min==-1) Min = 0;
        printf("Case #%d: %d\n", test, Min);

    }
    return 0;
}
