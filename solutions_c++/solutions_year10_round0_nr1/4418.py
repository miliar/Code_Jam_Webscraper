#include <stdio.h>\
using namespace std;
int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t,n,k;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        bool okay = true;
        scanf("%d%d", &n, &k);
        for (int j = 1; j <= n; j++)
        {
            if (k % 2 == 0)
            {
                okay = false;
                break;
            }
            k /= 2;
        }
        printf("Case #%d: ", i);
        if (okay) printf("ON\n");
        else printf("OFF\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
