#include<stdio.h>
#include<iostream>
using namespace std;

main()
{
    FILE * fi=fopen("input.txt","r");
    FILE * fo=fopen("output.txt","w");
    int T;
    fscanf(fi,"%d\n",&T);
    char read_line[350];
    for(int i=0;i<T;i++)
    {
        int N,S,P,t[100],out_count=0;
        fscanf(fi,"%d %d %d ",&N,&S,&P);
        for(int j=0;j<N;j++)
        {
            fscanf(fi,"%d",&t[j]);
            if(t[j]>=(3*P-2) )
            {
                out_count++;
            }
            else if(t[j]<(3*P-4))
            {
                continue;
            }
            else if(S>0)
            {
                int num;
                num= (t[j]-P)/2;
                if(num+2>=P && t[j]-P>=0)
                {
                    out_count++;
                    S--;
                }
            }
        }
        fprintf(fo,"Case #%d: %d\n",(i+1),out_count);
    }
    fclose(fi);
    fclose(fo);
}

