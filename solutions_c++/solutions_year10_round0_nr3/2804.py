#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>


uint64_t group[1000];

struct val
{
  uint64_t people;
  int next_start;
} stored[1000];


int main()
{

  uint64_t r,k,profit,current,j;
  int i,n, start , pstart, casenum , ncase;
  
  FILE * infile=fopen("try_inp_gcj.txt","r");
  FILE * outfile=fopen("gcjout4.txt","w");
  
  
  if(infile==NULL || outfile==NULL)
  {
    printf("File read/write error \n");
    exit(0);
  }
  
  fscanf(infile,"%d",&ncase);
  casenum=1;
  while(casenum<=ncase)
  {
   
    profit=0;
    
    fscanf(infile,"%llu %llu %d",&r,&k,&n);
    
    for(i=0;i<n;i++)
    {
      stored[i].people=0;
    }
    
    // read all group size
    
    for(i=0;i<n;i++)
    {
      fscanf(infile,"%llu",&group[i]);
    }
    
    pstart=0;
    
    // logic
    for(j=0;j<r;j++)  // number of rides
    {
      start=pstart;
      
      if(stored[start].people!=0)
      {
	current=stored[start].people;
	pstart=stored[start].next_start;
      }
     
     else
     {
      current=0;
      // get maximum number of passengers
     for(start=pstart;( (current=current+group[start])<=k ) && ((start!=pstart) || (current==group[start]) ) ;((start=start+1)<n)||( start%=n));                    
      current-=group[start];
      stored[pstart].people=current;
      stored[pstart].next_start=start;
      pstart=start;
   
     }
      profit+=current;
    }
    
    
    // end of logic
    printf("Case %d: %llu \n",casenum,profit);

      fprintf(outfile,"Case #%d: %llu\r\n",casenum,profit);
    
    // continue for next iteration
    casenum+=1;
  }
  
  fcloseall();
}