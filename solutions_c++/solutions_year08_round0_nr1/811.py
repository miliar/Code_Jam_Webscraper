#include <stdio.h>
#include <string.h>
#define fn "A-large.in"
#define fn2 "out.txt"
int main(void)
{
    FILE *f,*f2;
    int N,i,j,k,l;
        char buf[200];
            f=fopen(fn,"r");
    f2=fopen(fn2,"w");
    sscanf(fgets(buf,110,f),"%d",&N);
    for (i=0;i<N;i++)
    {
        char names[110][110];
        int S;
        sscanf(fgets(buf,110,f),"%d",&S);
//        fprintf(f2,"%s.%d",buf,S);
        int map[110];
        for (j=0;j<S;j++)
        {
  //          fprintf(f2,"%d\n",j);
         fgets(names[j],110,f);
         if (names[j][strlen(names[j])-1]=='\n') names[j][strlen(names[j])-1]=0;
         map[j]=0;
    //     fprintf(f2,names[j]);
        }
        int Q;
        int res=0;
        int zan=0;
        sscanf(fgets(buf,110,f),"%d",&Q);
        for (j=0;j<Q;j++)
        {
         fgets(buf,110,f);
         if (buf[strlen(buf)-1]=='\n') buf[strlen(buf)-1]=0;
         for (k=0;k<S;k++)
          if (!strcmp(buf,names[k])) break;
      //   fprintf(f2,"%d\n",k);
         if (map[k]==0) {zan++;map[k]=1;}
         if (zan==S)
         {
            for (l=0;l<S;l++)
             map[l]=0;
            map[k]=1;
            zan=1;
            res++;
         }
        }
        fprintf(f2,"Case #%d: %d\n",i+1,res);
    }
    fclose(f);
    fclose(f2);
}
