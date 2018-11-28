#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>

using namespace std;

int main()
{

  FILE *f = fopen("A-large.in","r");
  int n;

  if(f==NULL)
    printf("no file");
  fscanf(f,"%d",&n);
  printf("n = %d\n",n);
  for(int i=0;i<n;i++)
  {
    char engine[100][100],query[1000][100],temp[100];
    int ne=0,nq,answer=0;

    fscanf(f,"%d",&ne);
    printf("ne = %d\n",ne);
    int bits[ne];
    for(int x=0;x<ne;x++)
    {
      bits[x]=0;
    }
    fgets(temp,100,f);
    for(int j=0;j<ne;j++)
    {
     fgets(engine[j],100,f);
     printf("%s\n",engine[j]);
    }
    fscanf(f,"%d",&nq);
    printf("nq = %d\n",nq);

    fgets(temp,100,f);
    for(int j=0;j<nq;j++)
    {
     fgets(query[j],100,f);
     for(int k=0;k<ne;k++)
     {
      if(!strcmp(engine[k],query[j]))
      {
        bits[k]=1;
      }
      int sum=0;
      for(int x=0;x<ne;x++)
      {
       sum+=bits[x];
      }
      //printf("%d\n",sum);
      if(sum==ne)
      {
       answer+=1;
       for(int x=0;x<ne;x++)
         bits[x]=0;
       bits[k]=1;
      }
     }
    }
    FILE *fout=fopen("A-large.out","a");
    fprintf(fout,"Case #%d: %d\n",(i+1),answer);
    fclose(fout);
  }
  fclose(f);
  //cin.get();
}
