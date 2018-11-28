#include <stdio.h>
int main(void)
{
    FILE *f,*f2;
    int i,j,c,N,T,NA,NB;
    f=fopen("B-large.in","r");
    f2=fopen("out.txt","w");
    fscanf(f,"%d",&N);
    for (i=0;i<N;i++)
    {
        int r[3],rasp;
        int tar[210][3];
        r[1]=r[2]=0;rasp=0;
        fscanf(f,"%d",&T);
        fscanf(f,"%d%d",&NA,&NB);
        for (j=0;j<NA+NB;j++)
        {
            int c1,c2;
            fscanf(f,"%d%c%d",&c1,&c,&c2);
            tar[j][0]=c1*60+c2;
            fscanf(f,"%d%c%d",&c1,&c,&c2);
            tar[j][1]=c1*60+c2+T;
            tar[j][2]=j<NA?1:2;
        }
        while (rasp<NA+NB)
        {
         int base,mind;
         for (mind=0;!tar[mind][2];mind++) ;
         for (j=mind+1;j<NA+NB;j++)
          if (tar[j][2]&&tar[j][0]<tar[mind][0]) mind=j;
         int tp=tar[mind][2];
         r[tp]++;
         tp=(tp%2)+1;
         rasp++;
         tar[mind][2]=0;
         base=tar[mind][1];
         while(1)
         {
          for (mind=0;mind<NA+NB&&(tar[mind][2]!=tp||tar[mind][0]<base);mind++);
          for (j=mind+1;j<NA+NB;j++)
           if (tar[j][2]==tp&&tar[j][0]<tar[mind][0]&&tar[j][0]>=base) mind=j;
          if (mind<NA+NB)
          {
         tp=(tp%2)+1;
         rasp++;
         tar[mind][2]=0;
         base=tar[mind][1];
           
          }
          else
           break;                      
         }     
        }
        fprintf(f2,"Case #%d: %d %d\n",i+1,r[1],r[2]);
    }
    fclose(f);
    fclose(f2);
}
