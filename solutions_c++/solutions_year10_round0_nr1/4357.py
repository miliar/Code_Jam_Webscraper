#include <stdio.h>
#include <stdlib.h>
/*
 * 
 */
int main(int argc, char** argv) {
    int N,T,j;
    long int K,i;
    FILE *f;
    FILE *q;
    f=fopen("C:\\Users\\Rohit\\Desktop\\A-small-attempt3.in","r");
    q=fopen("C:\\Users\\Rohit\\Desktop\\A-small-attempt-answer.in","w");
    fscanf(f,"%d",&T);
    for(j=0;j<T;j++)
    {
        fscanf(f,"%d %ld",&N,&K);
        int *chain=(int *)calloc(N,sizeof(int));
        int *chain2=(int *)calloc(N,sizeof(int));
        int point;
        for(i=0;i<K;i++)
        {
            point=1;
            
            while(point<N)
            {
                if((*(chain+point)==0)&&(*(chain+point-1)==1))
                {
                    *(chain2+point)=1;
                    break;
                }
                if((*(chain+point)==1)&&(*(chain+point-1)==0))
                {
                    break;
                }
                if((*(chain+point)==1)&&(*(chain+point-1)==1))
                {
                    *(chain2+point)=0;
                }
                point++;
            }
             (*chain==0)?*chain2=1:*chain2=0;

             int x;
             for(x=0;x<N;x++)
             {
                 *(chain+x)=*(chain2+x);
             }
             //printf("\n");
        }
        int stat=0;
        for(i=0;i<N;i++)
        {
            if(*(chain+i)==1)
            {}
            else
            {
                stat=1;
                break;
            }
        }
        if(stat==0)
        {
            fprintf(q,"Case #%d: ON\n",j+1);
        }
        else
        {
            fprintf(q,"Case #%d: OFF\n",j+1);
        }
    }
    fclose(f);
    fclose(q);
    return (EXIT_SUCCESS);
}

