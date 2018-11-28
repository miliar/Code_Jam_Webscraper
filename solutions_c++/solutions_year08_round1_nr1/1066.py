#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
      FILE * pFile;
      FILE * wfile;
      
      pFile=fopen("A-small-attempt1.in","r+");
      wfile=fopen("Aans.in","a+");
      int n[1000],v1[1000][100],v2[1000][100],T,p=0,t;
      fscanf (pFile,"%d",&T);
      
      for (int i=0;i<T;i++)
      {
          p=0;
          fscanf (pFile,"%d",&n[i]);
          
          for (int j=0;j<n[i];j++)
          {
              fscanf (pFile,"%d",&v1[i][j]);
          }
          for (int j=0;j<n[i];j++)
          {
              fscanf (pFile,"%d",&v2[i][j]);
          }
          for (int j=0;j<n[i];j++)
          {
              for (int k=j+1;k<n[i];k++)
              {
                  if (v1[i][k]<v1[i][j])
                  {
                                        t=v1[i][j];
                                        v1[i][j]=v1[i][k];
                                        v1[i][k]=t;
                  }
              }
          }
          for (int j=0;j<n[i];j++)
          {
              for (int k=j+1;k<n[i];k++)
              {
                  if (v2[i][k]>v2[i][j])
                  {
                                        t=v2[i][j];
                                        v2[i][j]=v2[i][k];
                                        v2[i][k]=t;
                                       
                  }
              }
          }
          for (int j=0;j<n[i];j++)
          {
             
              p=p+(v1[i][j]*v2[i][j]);
              
          }
          fprintf (wfile,"Case #%d: %d\n",i+1,p);
         
          
      }
      fclose(pFile);
      fclose(wfile);
      
      return (0);
}
      
