#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* itoa(int val, int base){
	
	static char buf[32] = {0};
	
	int i = 30;
	
	for(; val && i ; --i, val /= base)
	
		buf[i] = "0123456789abcdef"[val % base];
	
	return &buf[i+1];
	
}

int main()
{
  FILE *input, *output;
  input = fopen ("input" , "r");
  output= fopen ("output", "w");
  int comp[2000000];
  
  
  char c[100];
  int i,j;
  
  i=0;
  do
  {
    c[i]=fgetc(input);
    i++;
  }while(c[i-1]!='\0' && c[i-1]!='\n');
  c[i-1]='\0';
  int cases=atoi(c);
  printf("%d",cases);
  
  for(int m=1;m<=cases;m++)
  {
    for(int k=0;k<2000000;k++)
      comp[k]=-1;
    int x=0;
    i=0;
    do
    {
      c[i]=fgetc(input);
      i++;
    }while(c[i-1]!=' ' && c[i-1]!='\n');
    c[i-1]='\0';
    int p1l=i-1;
    int part1=atoi(c);
    
    i=0;
    do
    {
      c[i]=fgetc(input);
      i++;
    }while(c[i-1]!=' ' && c[i-1]!='\n');
    c[i-1]='\0';
    int part2=atoi(c);
    
    for(int n=part1;n<=part2;n++)
    {
      char p1[100];
      strcpy(p1,itoa(n,10));
      
      for(int l=1;l<p1l;l++)
      {
	char p2[100];
	strcpy(p2,p1);
	i=0;
	do
	{
	 p2[i]=p1[p1l-l+i];
	 i++;
	}while(i<l);
	
	j=0;
	do
	{
	  p2[i+j]=p1[j];
	  j++;
	}while(j<(p1l-i));
	if(part1<=n && n<atoi(p2) && atoi(p2)<=part2)
	{
	  i=0;
	  while(comp[i]!=n || comp[i+1]!=atoi(p2))
	  {
	    if(comp[i]<0)
	    {
	      x++;
	      comp[i]=n;
	      comp[i+1]=atoi(p2);
	      break;
	    }
	    i+=2;
	  }
	}
      }
       
      
    }
    fprintf(output,"Case #%d: %d\n",m,x);
  }
  
  
  return 0;
}