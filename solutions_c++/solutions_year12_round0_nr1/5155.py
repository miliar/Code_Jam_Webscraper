#include <cstdlib>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;

char d[27] = "yhesocvxduiglbkrztnwjpfmaq";
char a[201], b[201];
int main()
{
    int n;
    scanf("%d\n",&n);
    for (int i=1; i<=n; i++)
    {
        memset(b,0,sizeof(b));
        cin.getline(a, 150);
        int l = strlen(a);
        for (int t=0; t<l; t++)
        {
            int c = a[t] - 'a';
            if (c < 26 && c > -1) b[t] = d[a[t] - 'a'];
            else b[t] = a[t];
        }
        printf("Case #%d: %s\n", i, b);
    }
    return 0;
}
