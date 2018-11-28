#include<stdio.h>
#include<string.h>
#define MAX 11
bool snap[MAX];
int main()
{
    FILE *in,*out;
    in=fopen("A-small-attempt1.in","r");
    //in=fopen("in.txt","r");
    out=fopen("out.txt","w");
    //out=stdout;
    int T;
    fscanf(in,"%d",&T);
    int caseno=1;
    while(T--)
    {
        int N,K;
        fscanf(in,"%d %d",&N,&K);
        //encode initial state as
        memset(snap,0,sizeof(snap));
        while(K--)
        {
            bool temp[MAX];
            temp[1]=!snap[1];
            for(int j=2;j<=N;j++)
            {
                //examining the jth bit
                //snap if its full powered
                bool flag=1;
                for(int k=1;k<j;k++)
                if(!snap[k])
                {
                    flag=0;
                    break;
                }
                if(flag)
                temp[j]=!snap[j];
                else
                temp[j]=snap[j];
            }
            for(int j=1;j<=N;j++)
            snap[j]=temp[j];
        }
        //and check if power of Nth bit is on
        bool flag=1;
        for(int k=1;k<=N;k++)
        if(!snap[k])
        {
            flag=0;
            break;
        }
        if(flag)
        fprintf(out,"Case #%d: ON\n",caseno++);
        else
        fprintf(out,"Case #%d: OFF\n",caseno++);

    }
    return 0;
}
