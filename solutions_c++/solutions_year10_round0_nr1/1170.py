#include <stdio.h>

int main()
{
    int t, n, k, i;

    scanf("%d", &t);
    for(i = 1; i <= t; i++)
    {
        scanf("%d %d", &n, &k);

        //while(k && k > (1<<n)) k -= (1<<n);


        printf("Case #%d: %s\n", i, ((k&((1<<n)-1))==((1<<n)-1))?"ON":"OFF");
    }

    return 0;
}
