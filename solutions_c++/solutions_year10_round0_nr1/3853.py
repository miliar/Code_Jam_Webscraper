#include<stdio.h>
#include<math.h>

int main()
{
        int t,n,k;
        FILE* fout = fopen("A-large.in","r");
        FILE* fin = fopen("A-large.out", "w");
        fscanf(fout,"%d",&t);
        for(int i=0;i<t;i++)
        {
                fscanf(fout, "%d%d", &n,&k);
                if(int(k-(pow(2,n)-1))%(int)pow(2,n)==0)fprintf(fin,"Case #%d: ON\n",i+1);
                else fprintf(fin,"Case #%d: OFF\n",i+1);                
        }
        return 0;
}
