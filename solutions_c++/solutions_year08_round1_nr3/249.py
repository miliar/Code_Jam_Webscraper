#include    <cstdio>
char a[31][4]={"","005","027","143","751","935","607","903","991","335","047","943","471","055","447","463","991",
"095","607","263","151","855","527","743","351","135","407","903","791","135","647"};
int main()
{
    int t, n, i;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &t);
    for (i=1; i<=t; ++i) {
        scanf("%d", &n);
        printf("Case #%d: %s\n", i, a[n]);
    }
}
