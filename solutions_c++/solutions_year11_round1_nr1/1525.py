#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    FILE *inp=fopen("input.txt","r");
    FILE *out=fopen("output.txt","w");
    int t,i,n,pd,pg,j;
    fscanf(inp,"%d",&t);
    for(i=0;i<t;i++)
    {
                    fscanf(inp,"%d %d %d",&n,&pd,&pg);
                    float perd=(float)pd/100.0;
                    float perg=(float)pg/100.0;
                    for(j=1;j<=n;j++)
                    {
                            float wind=perd*j;
                            if((wind-(int)wind)!=0)
                                    continue;
                            if(pg==100 && pd<100 || pg==0 && pd>0)
                            {           
                                    fprintf(out,"Case #%d: Broken\n",i+1);
                                    break;
                                    }        
                            else{
                                    fprintf(out,"Case #%d: Possible\n",i+1); 
                                    break;
                                    }
                    }                                                                                                   
                    if(j==n+1)
                             fprintf(out,"Case #%d: Broken\n",i+1);
    }
}
