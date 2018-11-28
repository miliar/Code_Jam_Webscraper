#include<iostream>
#include<stdio.h>
#include<stdlib.h>



using namespace std;

int OFF=0,ON=1;
class snapper
{
  public :
    
  int power;
  int state;
  
  void reset()
  {
    power=0;
    state=OFF;
  }
};

int main()
{
  snapper snap[32];
  int i,j,n,k,ncase,casenum;
  
  FILE * infile=fopen("smallin.txt","r");
  FILE * outfile=fopen("gcjout2.txt","w");
  
  
  if(infile==NULL || outfile==NULL)
  {
    printf("File read/write error \n");
    exit(0);
  }
  
  fscanf(infile,"%d",&ncase);
  casenum=1;
  while(casenum<=ncase)
  {
    
    fscanf(infile,"%d %d",&n,&k);
      
    // reset all snappers
    
    for(i=0;i<n+2;i++)
    {
      snap[i].reset();
    }
    
    snap[0].power=1;
    snap[0].state=ON;
    
    snap[1].power=1;
    snap[1].state=OFF;
    
    snap[n+1].power=0;
    snap[n+1].state=ON;
    
    // logic
    for(i=0;i<k;i++)  // number of snaps
    {
      // set state of all possible snappers
      
      for(j=1;j<=n;j++) // first change state of switch 
      {
	if(snap[j].power==1) snap[j].state=1-snap[j].state;
	else break;
      }
      
      for(j=1;j<=n+1;j++)  // changin powered attribute
      {
	if(snap[j-1].power==1 && snap[j-1].state==ON) snap[j].power=1;  
	else break;
      }
      for(j;j<=n+1;j++) // make remaining snaps as off
      {
	snap[j].power=0;
      }
    }
    
    
    // end of logic
    if(snap[n+1].power==1)
    {
      fprintf(outfile,"Case #%d: ON\r\n",casenum);
    }
    else if(snap[n+1].power==0)
    {
      fprintf(outfile,"Case #%d: OFF\r\n",casenum);
    }
    
    else  // for debugging 
    {
      printf("Case #%d: %d\n",casenum,snap[k-1].power);
    }
    // continue for next iteration
    casenum+=1;
  }
  
  fcloseall();
}