#include<stdio.h>
#include<conio.h>
int main()
{
    int T, N, A[1000], B[1000],i,j,k,n,output;
    FILE *fp1, *fp2;
    fp1 = fopen ( "A-large(3).in", "r" ) ;
    fp2 = fopen ( "lattempt.txt", "w" ) ;
    fscanf(fp1,"%d",&T);
    for(n=0;n<T;n++)
    {
                    fscanf(fp1,"%d",&N);
                    for(i=0;i<N;i++)
                                    fscanf(fp1,"%d %d",&A[i],&B[i]);
                    output=0;
                    for(i=0;i<N;i++)
                                      for(j=0;j<N;j++)
                                                      if(A[i]<A[j] && B[i]>B[j])
                                                                   output++;
                    fprintf(fp2,"Case #%d: %d\n",n+1,output);
    }
    fclose(fp1);
    fclose(fp2);
}
