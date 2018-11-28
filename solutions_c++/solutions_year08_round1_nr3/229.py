#include <math.h>
#include <stdio.h>

char table[31][4]={"000","005","027","143",
                 "751","935","607","903",
                 "991","335","047","943",
                 "471","055","447","463",
                 "991","095","607","263",
                 "151","855","527","743",
                 "351","135","407","903",
                 "791","135","647"};
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out.txt", "w", stdout);
    int ks , n, kase;
    scanf("%d",&kase);
    for(ks = 1; ks <= kase; ks++)
    {
        scanf("%d",&n);
        printf("Case #%d: %s\n", ks, table[n]);
    }
    //system("pause");
    return 0;
}
