#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

double v1[800], v2[800], produto;
int var;

void read()
{
    scanf("%d", &var);
    for(int i=0; i<var; i++)
        scanf("%lf", &v1[i]);
    for(int i=0; i<var; i++)
        scanf("%lf", &v2[i]);
}

void process()
{
    produto=0;
    sort(v1, v1+var);
    sort(v2, v2+var);
    for(int i=0; i<var; i++)
        produto+=v1[i]*v2[var-i-1];
    printf("%.lf\n", produto);
}

int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int n;
    scanf("%d", &n);
    for(int i=1; i<=n; i++)
    {
        printf("Case #%d: ", i);
        read();
        process();
    }
    return 0;
}
