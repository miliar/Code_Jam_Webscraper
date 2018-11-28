#include <stdio.h>
#define MAX 1010
int main()
{
    FILE *in = fopen("A-large.in", "r");
    FILE *out = fopen("A-large.out", "w");
    int t, count = 1;
    int n, i, j;
    int a[MAX], b[MAX], temp, total;
    if (in != NULL)
    {
        //scanf("%d", &t);
        fscanf(in, "%d", &t);
        while (t--)
        {
            //scanf("%d", &n);
            fscanf(in, "%d", &n);
            for (i = 0; i < n; i++)
                //scanf("%d %d", &a[i], &b[i]);
                fscanf(in, "%d %d", &a[i], &b[i]);
                
            for (i = 0; i < n; i++)
            {
                for (j = i + 1; j < n; j++)
                {
                    if (a[i] > a[j])
                    {
                        temp = a[i];
                        a[i] = a[j];
                        a[j] = temp;
                        temp = b[i];
                        b[i] = b[j];
                        b[j] = temp;
                    }
                }
            }
            
            total = 0;
            
            for (i = 0; i < n; i++)
            {
                for (j = 0; j < i; j++)
                {
                    if (b[j] > b[i])
                        total++;
                }
            }
            
            
            //printf("Case #%d: %d\n", count++, total);
            fprintf(out, "Case #%d: %d\n", count++, total);
        } 
    }
    return 0;
}
