#include <stdio.h>
int main()
{
    FILE *in,*out;
    in=fopen("input.in","r");
    out=fopen("output.out","w");
    long T,a[1000],b[1000],t_c,N,i,j;
    fscanf(in,"%ld",&T);

    for(t_c=1;t_c<=T;t_c++)

    {
        fscanf(in,"%ld",&N);
        for(i=0;i<N;i++)
            fscanf(in,"%ld %ld",&a[i],&b[i]);
        long count=0;
        for(i=0;i<N;i++)

            for(j=0;j<N;j++)
                if((a[i]<a[j]&&b[i]>b[j])||(a[i]>a[j]&&b[i]<b[j]))
                {
            count++;
        }
    fprintf(out,"Case #%ld: %ld\n",t_c,count/2);
    }
fclose(in);
fclose(out);
}
