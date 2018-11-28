#include <stdio.h>
#include <stdlib.h>
int main()
{
    int t, n, k, count = 1, i;
    FILE *finp = fopen("A-large.in","r");
	FILE *foutp = fopen("A.out","w");
    fscanf(finp, "%d", &t);
    //scanf("%d", &t);
    //printf("%d\n", t);
    //system("pause");
    while (t--)
    {
        fscanf(finp, "%d %d", &n, &k);
        fprintf(foutp, "Case #%d: ", count++);
        //scanf("%d %d", &n, &k);
        //printf("Case #%d: ", count++);
        for (i = 0; i < n; i++)
        {
            if (k%2 == 0) break;
            k /= 2;
        }
        if (i == n) fprintf(foutp, "ON\n");
        else fprintf(foutp, "OFF\n");
        //if (i == n) printf("ON\n");
        //else printf("OFF\n");
    } 
    return 0;
}
