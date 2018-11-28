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
  int n,k;
  int i,j;
  char mat[50][50];
  char col[50];
  char msg[20];
  int c;
  int red,blue;
  char tmp;
  
  while(t<test_case)
  {
    t++;
    
    //read variables with rotation
    fscanf(infile,"%d %d",&n,&k);
    for(j=n-1;j>=0;j--)
      for(i=0;i<n;i++)
      {
	
	while((tmp=fgetc(infile))=='\n' || tmp=='\r') ;
	mat[i][j]=tmp;
      }
      
   // printf("read");
      
      //apply logic
      
    // gravity;
  for(j=0;j<n;j++)
  {
    //read
    c=0;
    for(i=0;i<n;i++)
    {
      if(mat[i][j]!='.')
      {
	col[c]=mat[i][j];
	c+=1;
      }
    }
    
    //store
    for(i=0;i<n-c;i++)
    {
      mat[i][j]='.';
    }
    for(i=n-c;i<n;i++)
    {
      mat[i][j]=col[i-n+c];
    }
  }
    
    
  red=0;
  blue=0;
    //search vertical
    int kount;
    kount=0;
    char ptype;
    
    
    for(j=0;j<n;j++)
    {
      ptype=':';
      kount=0;
      for(i=0;i<n;i++)
      {
	if(mat[i][j]=='.') 
	{
	  kount=0;
	  ptype=':';
	  continue ;
	}
	
	if(ptype==mat[i][j])
	{
	  kount+=1;
	  if(kount>=k)
	  {
	    if(ptype=='R')
	      red=1;
	    else if(ptype=='B')
	      blue=1;
	  }
	}
	else
	{
	  kount=1;
	}
	ptype=mat[i][j];
      }
    }
    
    if(red && blue) goto end__;
    //========================================//
    
    // search horizontal;
    
    for(i=0;i<n;i++)
    {
      ptype=':';
      kount=0;
      for(j=0;j<n;j++)
      {
	if(mat[i][j]=='.') 
	{
	  kount=0;
	  ptype=':';
	  continue;
	}
	
	if(ptype==mat[i][j])
	{
	  kount+=1;
	  if(kount>=k)
	  {
	    if(ptype=='R')
	      red=1;
	    else if(ptype=='B')
	      blue=1;
	  }
	}
	else
	{
	  kount=1;
	}
	ptype=mat[i][j];
      }
    } 
    
    if(red && blue) goto end__;
    //========================================//
    
    
    //search right slant;
    int tc,rr;
    //top search;
    for(j=k-1;j<n;j++)
    {
      tc=j;
      ptype=':';
      kount=0;
      for(i=0;tc>=0 && i<n ;i+=1 , tc-=1)
      {
	if(mat[i][tc]=='.') 
	{
	  kount=0;
	  ptype=':';
	  continue;
	}
	
	if(ptype==mat[i][tc])
	{
	  kount+=1;
	  if(kount>=k)
	  {
	    if(ptype=='R')
	      red=1;
	    else if(ptype=='B')
	      blue=1;
	  }
	}
	else
	{
	  kount=1;
	}
	ptype=mat[i][tc];
      }
    }
    
    // right col search
    
    for(i=1;n-i>=k;i++)
    {
      rr=i;
      ptype=':';
      kount=0;
      for(j=n-1;rr<n && j>=0 ;rr+=1, j--)
      {
	if(mat[rr][j]=='.') 
	{
	  kount=0;
	  ptype=':';
	  continue;
	}
	
	if(ptype==mat[rr][j])
	{
	  kount+=1;
	  if(kount>=k)
	  {
	    if(ptype=='R')
	      red=1;
	    else if(ptype=='B')
	      blue=1;
	  }
	}
	else
	{
	  kount=1;
	}
	ptype=mat[rr][j];
      }
    }
    
    if(red && blue) goto end__;
    //========================================//
    
    
    // search left slant
    
    
    
    

    //top search;
    for(j=0;n-j>=k;j++)
    {
      tc=j;
      ptype=':';
      kount=0;
      for(i=0;tc<n && i<n ;i+=1 , tc+=1)
      {
	if(mat[i][tc]=='.') 
	{
	  kount=0;
	  ptype=':';
	  continue;
	}
	
	if(ptype==mat[i][tc])
	{
	  kount+=1;
	  if(kount>=k)
	  {
	    if(ptype=='R')
	      red=1;
	    else if(ptype=='B')
	      blue=1;
	  }
	}
	else
	{
	  kount=1;
	}
	ptype=mat[i][tc];
      }
    }
    
    // left col search
    
    for(i=1;n-i>=k;i++)
    {
      rr=i;
      ptype=':';
      kount=0;
      for(j=0; rr<n && j<n ;rr+=1, j++)
      {
	if(mat[rr][j]=='.') 
	{
	  kount=0;
	  ptype=':';
	  continue;
	}
	
	if(ptype==mat[rr][j])
	{
	  kount+=1;
	  if(kount>=k)
	  {
	    if(ptype=='R')
	      red=1;
	    else if(ptype=='B')
	      blue=1;
	  }
	}
	else
	{
	  kount=1;
	}
	ptype=mat[rr][j];
      }
    }
    
    if(red && blue) goto end__;
    //========================================//
    
    //write output
    end__ :
    strcpy(msg,"");
    if(red && blue) strcpy(msg,"Both");
    else if(red) strcpy(msg,"Red");
    else if(blue) strcpy(msg,"Blue");
    else strcpy(msg,"Neither");
    fprintf(outfile,"Case #%d: %s\n",t,msg);
    printf("Case #%d: %s\n",t,msg);
  }
  
  fcloseall();
}