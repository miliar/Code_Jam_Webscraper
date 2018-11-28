#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

int t,n,pi,pj;


int main(void){
    double li,p_i,p_j;
    int wd,wt,j,f,pt;
    FILE *in,*out;
    in=fopen("A-small-attempt3.in","r");
    //in=fopen("in.in","r");
    out=fopen("out.txt","w");
    fscanf(in,"%d",&t);
    for (int i2=1;i2<=t;i2++){
        fscanf(in,"%d %d %d",&n,&pi,&pj);      
        f=0;     
        for (int i=1;i<=n&&f==0;i++){
            if (((i*pi)%100)==0){
               if ((pj==0&&pi==0)||(pj==100&&pi==100)||(pj!=0&&pj!=100))
                   f=1;
               }   
            }
        printf("%d\n",i2);
        if (f==1)
           fprintf(out,"Case #%d: Possible\n",i2);            
           else
                      fprintf(out,"Case #%d: Broken\n",i2);            
        }
    fclose (in);
    fclose (out);
    return 0;
    }
