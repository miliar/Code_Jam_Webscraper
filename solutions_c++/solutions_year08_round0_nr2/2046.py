#include<stdio.h>
#include<string.h>


int main()
{
    int N,T[105],NA[105],NB[105],t;
    int dephA[105],dephB[105],arrhA[105],arrhB[105],depmA[105],depmB[105],arrmA[105],arrmB[105];
      char A[10],B[10],C[10],D[10];
      int hour,min;
      int outA;
      int outB;
      FILE * pFile;
      FILE * wFile;
      pFile=fopen("B-large.in","r+");
      wFile=fopen("Bans.in","a+");
      fscanf (pFile,"%d",&N);

      for (int h=0;h<N;h++)
      {
      fscanf (pFile,"%d",&T[h]);
      fscanf (pFile,"%d",&NA[h]);
      fscanf (pFile,"%d",&NB[h]);
      
      
      for (int i=0;i<NA[h];i++)
      {
          fscanf (pFile,"%s",A);
          dephA[i]=(A[1]-'0')+((A[0]-'0')*10);
          depmA[i]=(A[4]-'0')+((A[3]-'0')*10);
          fscanf (pFile,"%s",C);
          arrhA[i]=(C[1]-'0')+((C[0]-'0')*10);
          arrmA[i]=(C[4]-'0')+((C[3]-'0')*10);
      }
      
      int j=0;
      for (int i=NA[h];i<(NB[h]+NA[h]);i++)
      {
          fscanf (pFile,"%s",B);
          dephB[j]=(B[1]-'0')+((B[0]-'0')*10);
          depmB[j]=(B[4]-'0')+((B[3]-'0')*10);
          fscanf (pFile,"%s",D);
          arrhB[j]=(D[1]-'0')+((D[0]-'0')*10);
          arrmB[j]=(D[4]-'0')+((D[3]-'0')*10);
          j++;
      }
     
      outA=NA[h];
      outB=NB[h];
      for (int i=0;i<NA[h];i++)
      {
          for (int z=i+1;z<NA[h];z++)
          {
              if (dephA[z]<dephA[i])
              {
                                    t=dephA[z];
                                    dephA[z]=dephA[i];
                                    dephA[i]=t;
                                    t=depmA[z];
                                    depmA[z]=depmA[i];
                                    depmA[i]=t;
              }
              else if (dephA[z]==dephA[i])
              {
                   if (depmA[z]<depmA[i])
                   {
                                    t=dephA[z];
                                    dephA[z]=dephA[i];
                                    dephA[i]=t;
                                    t=depmA[z];
                                    depmA[z]=depmA[i];
                                    depmA[i]=t;
                   }
              }
          }
      }
      for (int i=0;i<NB[h];i++)
      {
          for (int z=i+1;z<NB[h];z++)
          {
              if (dephB[z]<dephB[i])
              {
                                    t=dephB[z];
                                    dephB[z]=dephB[i];
                                    dephB[i]=t;
                                    t=depmB[z];
                                    depmB[z]=depmB[i];
                                    depmB[i]=t;
              }
              else if (dephB[z]==dephB[i])
              {
                   if (depmB[z]<depmB[i])
                   {
                                    t=dephB[z];
                                    dephB[z]=dephB[i];
                                    dephB[i]=t;
                                    t=depmB[z];
                                    depmB[z]=depmB[i];
                                    depmB[i]=t;
                   }
              }
          }
      }
      int stop[120];
      int y=0;
      int flag=1;
       for (int i=0;i<NB[h];i++)
      {
          min=arrmB[i]+T[h];
          if (min>=60)
          {
          min=min-60;
          hour=arrhB[i]+1;
          }
          else
          hour=arrhB[i];
          for (int k=0;k<NA[h];k++)
          {
              for (int x=0;x<y;x++)
              {
                  flag=1;
                  if (stop[x]==k)
                  {
                                 flag=0;
                                 break;
                  }
              }
              if (flag==1)
              {
              if (dephA[k]>hour )
              {
                                 outA--;
                                stop[y++]=k;
                                 break;
              }
              else if (dephA[k]==hour  )
              {
                   if (depmA[k]>=min )
                   {
                                 outA--;
                                 stop[y++]=k;
                                 break;
                   }
              }
              }
          }
      }
      int stope[120];
      int f=0;
      flag=1;
      
      for (int i=0;i<NA[h];i++)
      {
          min=arrmA[i]+T[h];
          if (min>=60)
          {
          min=min-60;
          hour=arrhA[i]+1;
          }
          else
          hour=arrhA[i];
          
     
         
          for (int k=0;k<NB[h];k++)
          {
              for (int e=0;e<f;e++)
              {
                  flag=1;
                  if (stope[e]==k)
                  {
                                 flag=0;
                                 break;
                  }
              }
              
             if (flag==1)
             {
              if (dephB[k]>hour )
              {
                                
                                 outB--;
                                 stope[f++]=k;
                                 break;
              }
              else if (dephB[k]==hour)
              {
                   if (depmB[k]>=min )
                   {
                                 outB--;
                                 stope[f++]=k;
                                 break;
                   }
              }
              }
          }
      }
     
      
     fprintf (wFile,"Case #%d: %d %d\n",h+1,outA,outB);
     
     
      }
      fclose (pFile);
      fclose (wFile);
            return 0;
}
