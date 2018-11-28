#include <stdio.h>
#include <math.h>

int main()
{
    FILE *fp, *fp_write;
    fp = fopen("A-large.in","r");
    fp_write = fopen("snap_large.out","w");
    int t;
    fscanf(fp, "%d", &t);
    for(int i = 1; i <= t; ++i)
    {
       int n,k;
       fscanf(fp, "%d %d", &n, &k);
       int toggle_count = pow(2,n-1);
       int tar = k+1;
       if(tar%(2*toggle_count) == 0)
           fprintf(fp_write, "Case #%d: ON\n", i);
          //printf( "Case #%d: ON\n", i);
        else
          fprintf(fp_write, "Case #%d: OFF\n", i);          
          //printf("Case #%d: OFF\n", i);      
    }

    fclose(fp);
    fclose(fp_write);
    return 0;
}
