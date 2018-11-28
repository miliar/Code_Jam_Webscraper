#include <iostream>
#include <stdio.h>
using namespace std;
double abs(double a)
{
    if(a<0)
           a*=-1;
    return (a);
}
int main()
{
    int T,N,S,p,bathmos,tmpN;
    FILE*read=fopen("B-large.in","r");
    fscanf(read,"%d\n",&T);
    FILE*write=fopen("B-large.out","w");
    for(int i=1;i<=T;i++)
    {
            fprintf(write,"Case #%d: ", i);
            fscanf(read,"%d ",&N);
            tmpN=N;
            fscanf(read,"%d ",&S);
            fscanf(read,"%d ",&p);
            for(int j=0;j<N;j++)
            {
                    fscanf(read,"%d",&bathmos);
                    if(bathmos-p<0)
                        tmpN--;
                    else if(abs(p-(bathmos-p)/2)==2 and S>0 and 3*p>=bathmos)
                                          S--;
                    else if(abs(p-(bathmos-p)/2)==2 and S==0 and 3*p>=bathmos)
                         tmpN--;
                    else if(abs(p-(bathmos-p)/2)>2 and 3*p>=bathmos)
                         tmpN--;
            }
            fprintf(write,"%d\n",tmpN);
    }
    fclose(read);
    fclose(write);
    return 0;
}
