// Furshing Tsai  fstsai@gmail.com
// Welcome to code jam
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <assert.h>

//your answer to make it exactly 4 digits long.
//Limits
//1 . N . 100

//Small dataset
//Each line will be no longer than 30 characters. 

//Large dataset
//Each line will be no longer than 500 characters. 


#define DEBUG 1
int debug=0;

int count_pttn(char *pp,char *sp)
{ int matched=0;
 
#if (DEBUG)
   if (debug) {
     printf("{ matching '%s' '%s'\n",pp,sp);
   }
#endif
  while (*sp!='\0') {
   if (*pp=='\0') break;
#if (DEBUG)
   if (debug) {
     printf(" try '%s' '%s'\n",pp,sp);
   }
#endif
   if (*pp==*sp) {
    if (pp[1]=='\0') 
      matched++; // done matched
    else
      matched+= count_pttn(pp+1,sp+1);
   } else {
      // matched+= count_pttn(pp,sp+1);
   }
   sp=sp+1;
  }
#if (DEBUG)
   if (debug) {
     printf("match '%s' '%s' = %d }\n",pp,sp,matched);
   }
#endif
  return matched;
}
  
char *pttn="welcome to code jam";
//char *pttn="abc";
char string[1024];
int main(int argc, char **argv)
{ int i,j,k;
  int  N;
  if (argc<2) { printf("Usage %s file"); return(1); }
  FILE *fd=fopen(argv[1],"r");
  fscanf(fd,"%d\n",&N);
#if (DEBUG)
  if (argc>2) {
    debug=1;
    printf("N=%d\n",N);
  }
#endif

  for (i=0;i<N;i++) {
  char line[1024];
  int read;

    // READ input
    fgets(line,1024, fd);
    line[strlen(line)-1]='\0';
#if (DEBUG)
  if (argc>2) {
    printf("A:%d str='%s'\n",i,line);
  }
#endif
 
    // print result
    int count = count_pttn(pttn,line);
    int c0=count%10, c1=(count/10)%10,  c2=(count/100)%10, c3=(count/1000)%10;
    printf("Case #%d: %d%d%d%d\n",i+1,c3,c2,c1,c0);
    //free(line);
  }
  return 0;
}
