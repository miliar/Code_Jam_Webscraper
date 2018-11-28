#include <stdio.h>
#include <memory.h>
#include <map>
#include <string>
using namespace std;

int n, nn, s, q, i, j, k;
char st[105];
map<string, int> m;
int a[101][1000];

int main()
{
    FILE * f = fopen("input.txt", "rt");
    fgets(st, 105, f);
    sscanf(st, "%d", &n);
    for(nn = 1; nn <= n; ++nn)
    {
        m.clear();
        fgets(st, 105, f);
        sscanf(st, "%d", &s);
        for(i = 0; i < s; ++i)
        {
            fgets(st, 105, f);
            m[string(st)] = i + 1;
        }

        fgets(st, 105, f);
        sscanf(st, "%d", &q);
        for(i = 0; i < q; ++i)
        {
            fgets(st, 105, f);
            a[0][i] = m[string(st)];
        }

        for(i = 1; i <= s; ++i)
            if(i == a[0][q - 1]) a[i][q - 1] = 2000;
            else a[i][q - 1] = 0;
        for(i = q - 2; i >= 0; --i) 
            for(j = 1; j <= s; ++j)
                if(j == a[0][i]) a[j][i] = 2000;
                else
                {
                    a[j][i] = a[j][i + 1];
                    for(k = 1; k <= s; ++k)
                        if((a[k][i + 1] + 1) < a[j][i])
                            a[j][i] = a[k][i + 1] + 1;
                }

        j = 2000;
        for(i = 1; i <= s; ++i)
            if(a[i][0] < j) j = a[i][0];

        printf("Case #%d: %d\n", nn, j);
    }
    fclose(f);

    printf("Press any key...");
    gets(st);
    return 0;
}
