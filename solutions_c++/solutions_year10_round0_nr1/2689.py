#include <iostream>
#include<math.h>
using namespace std;

int main()
{
    FILE *in,*out;
    int i,n,k,j=1,t;
    in=fopen("input.txt","r");
    out=fopen("output.txt","w");
    fscanf(in,"%d",&i);
    while(j<=i)
    {
        fscanf(in,"%d%d",&n,&k);
        t=pow(2,n);
        printf("%d\n",t);
        k-=t-1;
        if(k%t==0)
        fprintf(out,"Case #%d: ON\n",j);
        else
        fprintf(out,"Case #%d: OFF\n",j);
        j++;
    }

    return 0;
}
