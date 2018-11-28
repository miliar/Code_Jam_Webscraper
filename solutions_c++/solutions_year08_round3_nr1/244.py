#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
    FILE *in = fopen("input.txt", "r");
    FILE *out = fopen("output.txt", "w");
    int Test, t;
    fscanf(in, "%ld", &Test);
    for (t=1;t<=Test;t++)
    {
        int P, K, L, i, X[1100];
        __int64 res=0;
        fscanf(in, "%ld%ld%ld", &P, &K, &L);
        for (i=0;i<L;i++)
            fscanf(in, "%ld", &X[i]);
        
        if (P*K>=L)
        {
        
            sort(X, X+L);
            for (i=0;i<L;i++)
            {
                res+= (__int64)X[L-i-1]*(i/K + 1);
            }
            fprintf(out, "Case #%ld: %I64d\n", t, res);
        }
        else fprintf(out, "Case #%ld: Impossible\n");
    }

    fclose(in);
    fclose(out);   
    return 0;
}
