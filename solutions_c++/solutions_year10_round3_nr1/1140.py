#include<stdio.h>
#include<stdlib.h>
int i,j,k,l,m,n,t;
int a[1100],b[1100];
FILE *in, *out;
int main()
{
  //  scanf("%i",&t);
    in=fopen("A-large.in","r");
    out=fopen("out.txt","w");
    fscanf(in,"%i",&t);
    for(int cas=0;cas<t;cas++)
    {
        k=0;
        //scanf("%i",&n);
        fscanf(in,"%i",&n);
        for(i=0;i<n;i++)
           // scanf("%i%i",&a[i],&b[i]);
           fscanf(in,"%i%i",&a[i],&b[i]);
        for(i=0;i<n;i++)
            for(j=i+1;j<n;j++)
            {
                if(a[j]>a[i] && b[j]<b[i])
                    k++;
                if(a[j]<a[i] && b[j]>b[i])
                    k++;
            }

        printf("Case #%i: %i\n",cas+1,k);
        fprintf(out,"Case #%i: %i\n",cas+1,k);
    }
fclose(out);
return 0;
}
