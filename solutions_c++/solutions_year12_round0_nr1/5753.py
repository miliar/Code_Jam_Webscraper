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
    printf("%d\n",m);
    fprintf(output,"Case #%d: ",m);
    char c;
    do
    {
      c=fgetc(input);
      switch(c){
	case 'a':{c='y';}break;
	case 'b':{c='h';}break;
	case 'c':{c='e';}break;
	case 'd':{c='s';}break;
	case 'e':{c='o';}break;
	case 'f':{c='c';}break;
	case 'g':{c='v';}break;
	case 'h':{c='x';}break;
	case 'i':{c='d';}break;
	case 'j':{c='u';}break;
	case 'k':{c='i';}break;
	case 'l':{c='g';}break;
	case 'm':{c='l';}break;
	case 'n':{c='b';}break;
	case 'o':{c='k';}break;
	case 'p':{c='r';}break;
	case 'q':{c='z';}break;
	case 'r':{c='t';}break;
	case 's':{c='n';}break;
	case 't':{c='w';}break;
	case 'u':{c='j';}break;
	case 'v':{c='p';}break;
	case 'w':{c='f';}break;
	case 'x':{c='m';}break;
	case 'y':{c='a';}break;
	case 'z':{c='q';}break;
      }
      putc(c,output);
    }while((c!='\n') && (c!='\0'));
      
    
  }
  
  
  return 0;
}