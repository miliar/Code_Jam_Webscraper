
#include<stdio.h>
#include<conio.h>

int main()
{
    int r, k, n, g[100000];
    FILE *fin, *fout;
    fin = fopen("c:\\C-small-attempt1.in","r");
    fout = fopen("c:\\output54.out","w");
    
    int t = 0;
    fscanf(fin,"%d",&t);
    printf("\n t = %d",t );
    for( int p = 1; p <= t; p++)
    {
        fscanf(fin,"%d%d%d",&r,&k,&n); 
        printf("\n r = %d,             k = %d,      n = %d",r,k,n);
        for( int j = 0; j < (100000); j++) g[j] = 0;
        for( int j = 0; j < n; j++)
        fscanf(fin,"%d",&g[j]);
        int index = 0, mkj = 0;
        int index2 = n;
        int count  = 0;
        for( int r1 = 0; r1 <  r; r1++)
        {
            mkj++;
            int tem = 0, d;
             for( d = 0; d < n; d++ )
             {
                   if(( tem + g[index]) > k) break;  
                   else tem = tem + g[index++];
             }
             int start = index - d;
             for( int j = 0; j < d; j++)
             g[index2++] = g[start++];
             count += tem;  
        }
        fprintf(fout,"Case #%d: %d\n",p,count);
    }
    printf("done");
     getch();
     return 0;
}
