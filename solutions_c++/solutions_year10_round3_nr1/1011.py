#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<conio.h>
using namespace std;

int main()
{
    FILE *in, *out;
    in  = fopen("c:\\A-large.in","r");
    out = fopen("c:\\out.txt","w");
    int test = 0;
    fscanf(in,"%d",&test);
    cout <<"\n test = " << test;
    for ( int i = 0; i < test; i++)
    {
        
        int n = 0;
        int **p;
        fscanf(in,"%d",&n);
        p = new int*[n];
        //cout <<"\n n = " << n;
        for( int j = 0; j < n; j++)
        {
             p[j] = new int[2];
             fscanf(in,"%d%d",&p[j][0],&p[j][1]);
             //printf("\n p[%d][%d] = %d ,  p[%d][%d] = %d ",j,0,p[j][0],j,1,p[j][1]);
        }
        int sum = 0, chk1, chk2;
        for( int k = 0; k < n- 1; k++)
        {
             for ( int t = k + 1; t <= n - 1; t++)
             {
                  chk1 = p[k][0] - p[t][0];
                  chk2 = p[k][1] - p[t][1];
                  if( chk1*chk2 < 0 ) sum++;
             }
        }
        fprintf(out,"Case #%d: %d\n",i+1,sum);
    }
    cout <<"\n completed";
    fclose(in);
    fclose(out);
    getch();
    return 0;
}
