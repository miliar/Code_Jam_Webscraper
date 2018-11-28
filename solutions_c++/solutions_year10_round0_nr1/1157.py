#include<stdio.h>

long pow(long a, long b)
{
    long ret=1;
    for(int i=0; i<b; i++) 
    {
        ret*=a;   
    }  
    return ret;
}

int main(void)
{
    FILE* fin = fopen("snapper.in", "r");
    FILE* fout = fopen("snapper.out", "w");  
    int n;
    fscanf(fin, "%d", &n);
    for(int i=1; i<=n; i++)
    {
        long a, b;
        fscanf(fin, "%ld %ld", &a, &b);
        fprintf(fout, "Case #%d: %s\n",  i, ((b+1)%pow(2, a)==0)?"ON":"OFF");
    }
}
