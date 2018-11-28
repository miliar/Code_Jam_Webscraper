#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>

using namespace std;

int main()
{

  FILE *f = fopen("B-large.in","r");
  int n;

  if(f==NULL)
    printf("no file");
  fscanf(f,"%d",&n);
  
  for(int i=0;i<n;i++)
  {
    int NA=0,NB=0,y=0,presentA=0,needA=0,presentB=0,needB=0,turnaround;
    fscanf(f,"%d",&turnaround);
    fscanf(f,"%d %d",&NA,&NB);
    printf("NA=%d NB=%d\n",NA,NB);
    int depA[NA],arrB[NA],depB[NB],arrA[NB],allTimes[(2*(NA+NB))];
    for(int j=0;j<NA;j++)
    {
     int h,m;
     fscanf(f,"%d:%d",&h,&m);
     printf("%d %d\n",h,m);
     depA[j]=(60*h)+m;
     allTimes[y++]=(60*h)+m;
     fscanf(f,"%d:%d",&h,&m);
     arrB[j]=(60*h)+m+turnaround;
     allTimes[y++]=(60*h)+m+turnaround;
    }
    for(int j=0;j<NB;j++)
    {
     int h,m;
     fscanf(f,"%d:%d",&h,&m);
     depB[j]=(60*h)+m;
     allTimes[y++]=(60*h)+m;
     fscanf(f,"%d:%d",&h,&m);
     arrA[j]=(60*h)+m+turnaround;
     allTimes[y++]=(60*h)+m+turnaround;
    }
    for(int j=0;j<(2*(NA+NB)-1);j++)
    {
     for(int k=j+1;k<(2*(NA+NB));k++)
     {
      if(allTimes[k]<allTimes[j])
      {
        int temp=allTimes[k];
        allTimes[k]=allTimes[j];
        allTimes[j]=temp;
      }
     }
    }
    for(int j=0;j<(2*(NA+NB));j++)
    {
     int done=0;
     for(int k=0;k<NA;k++)
     {
      if(allTimes[j]==arrB[k])
      {
        presentB++;
        arrB[k]=-1;
        done=1;
        break;
      }
     }
     if(done)
       continue;
     for(int k=0;k<NB;k++)
     {
      if(allTimes[j]==arrA[k])
      {
        presentA++;
        arrA[k]=-1;
        done=1;
        break;
      }
     }
     if(done)
       continue;
     for(int k=0;k<NA;k++)
     {
      if(allTimes[j]==depA[k])
      {
        if(presentA>0)
          presentA--;
        else
          needA++;
        depA[k]=-1;
        done=1;
        break;
      }
     }
     if(done)
       continue;
     for(int k=0;k<NB;k++)
     {
      if(allTimes[j]==depB[k])
      {
        if(presentB>0)
          presentB--;
        else
          needB++;
        depB[k]=-1;
        break;
      }
     }
    }
    FILE *fout=fopen("B-large.out","a");
    fprintf(fout,"Case #%d: %d %d\n",(i+1),needA,needB);
    fclose(fout);
  }
    
  fclose(f);
  
}
