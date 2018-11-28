#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<algorithm>

using namespace std;

int main()
{
  FILE * infile;
  FILE * outfile;
  int test_case;
  int t;
  
  infile=fopen("in.txt","r");
  outfile=fopen("out.txt","w");
  
  
  if(!infile || !outfile)
  {
    printf("Unable to read/write file\n");
    exit(0);
  }
  fscanf(infile,"%d",&test_case);
  
  
  t=0;
  int lines[1000][2];
  int n;
  int i,j,k;
  int count;
  int left,right;
  
  while(t<test_case)
  {
    t++;
    fscanf(infile,"%d",&n);
  
    for(i=0;i<n;i++)
      fscanf(infile,"%d %d",&lines[i][0],&lines[i][1]);
        
    //read variables;
    
    count=0;
    for(i=0;i<n;i++)
      for(j=0;j<n;j++)
      {
	  if(j==i) continue;
	  {
	  //  printf("%d %d %d %d\n",lines[j][0],lines[i][0],lines[j][1],lines[j][1]);
	      if(lines[j][0]>lines[i][0]) left=1;
	      else left=-1;
	      
	      if(lines[j][1]>lines[i][1]) right=1;
	      else right=-1;
		
		if(left!=right) count+=1;
		//printf("%d %d\n",left,right);
	  }
      }
    
    
    //apply logic
    
    
    
    
    //write output
    count/=2;
    fprintf(outfile,"Case #%d: %d\n",t,count);
    printf("Case #%d: %d\n",t,count);
  }
  
  fcloseall();
}