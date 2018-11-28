#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getCount(int t, int p, bool surp)
{
    int avg=t/3;
    int mod=t%3;
    int best=avg;
    if (t==0)
    {
             best=0;
    }
    else if (t==1)
    {
             best=1;
    }
    else if (t==2)
    {
             best=2;
    }
    else if (surp)
    {
             switch (mod)
             {
                    case 0:
                         best=avg+1;
                         break;
                    case 1:
                         best=avg+1;
                         break;
                    case 2:
                         best=avg+2;
                         break;
             }
    }
    else
    {
        switch (mod)
        {
               case 0:
                    best=avg;
                    break;
               case 1:
                    best=avg+1;
                    break;
               case 2:
                    best=avg+1;
                    break;
        }
    }
    if (best>=p) return 1;
    else return 0;
}

int main()
{
    int T;
    scanf("%d\n",&T);
    for (int test=1;test<=T;test++)
    {
        int N,S,p;
        scanf("%d %d %d",&N,&S,&p);
        
        int map[N][S+1];
        for (int i=0;i<N;i++)
            for(int j=0;j<S+1;j++)
            map[i][j]=0;
        
        for (int i=0;i<N;i++)
        {
            int t;
            scanf("%d",&t);
            for (int j=0;j<S+1;j++)
            {
                int out=0;
                int notSurp=getCount(t,p,false);
                int Surp=getCount(t,p,true);
                if (i-1>=0)
                {
                           notSurp+=map[i-1][j];
                }
                if (j-1>=0)
                {
                   if (i-1>=0)
                      Surp+=map[i-1][j-1];
                }
                else Surp=0;
                
                if (notSurp>Surp) out=notSurp;
                else out=Surp;
                map[i][j]=out;
               // printf("%d ",map[i][j]);
            }
            //printf("\n");
        }
        
        int max=-1;
        for (int j=0;j<S+1;j++)
        {
            if (map[N-1][j]>max)
               max=map[N-1][j];
        }
        
        printf("Case #%d: %d\n",test,max);
    }
    
    return 0;
}
