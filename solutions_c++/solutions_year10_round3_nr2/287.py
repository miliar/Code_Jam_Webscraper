#include <stdio.h>
#include <math.h>
int main()
{
    FILE *in = fopen("B-large.in", "r");
    FILE *out = fopen("B-large.out", "w");
    int t, count = 1, num;
    double l, p, c, res;
    if (in != NULL)
    {
        //scanf("%d", &t);
        fscanf(in, "%d", &t);
        while (t--)
        {
            //scanf("%lf %lf %lf", &l, &p, &c);
            fscanf(in, "%lf %lf %lf", &l, &p, &c);
            
            num = 0;
            res = p/l;
            
            while (res > c)
            {
                res = sqrt(res);
                num++;
            }
            
            //printf("Case #%d: %d\n", count++, num);
            fprintf(out, "Case #%d: %d\n", count++, num);
        } 
    }
    return 0;
}
