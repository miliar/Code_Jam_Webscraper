#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <assert.h>
//Small dataset
//
//1 < L < 10
//1 < D < 25
//1 < N < 10
//
//Large dataset
//
//1 < L < 15
//1 < D < 5000
//1 < N < 500
#define DEBUG 0

#define name_no  D
#define name_len L
int main(int argc, char **argv)
{ int i,j,k;
  int L,D,N;
  char **names,*p,str[1024];
  char pttn[20][256];
  if (argc!=2) { printf("Usage %s file"); return(1); }
  FILE *fd=fopen(argv[1],"r");
  fscanf(fd,"%d %d %d",&L,&D,&N);
#if (DEBUG)
  printf("L=%d, D=%d, N=%d\n",L,D,N);
#endif
  names = (char**) malloc(sizeof (char *)*name_no);
  for (i=0;i<name_no;i++) {
    fscanf(fd,"%s",str);
    names[i]=(char*)malloc(sizeof (char)*strlen(str)+1);
    strcpy(names[i],str);
#if (DEBUG)
printf("A:%d %s\n",i,names[i]);
#endif
  }
 
  for (i=0;i<N;i++) {
    fscanf(fd,"%s",str);
#if (DEBUG)
printf("B:%d %s\n",i,str);
#endif
    for (k=0;k<name_len;k++)
     for (j=0;j<255;j++)
       pttn[k][j]=0;
    for (k=0,p=str;*p!='\0';p++) {
     if (*p=='(') {
       p++;
       while (*p!=')')
         pttn[k][*p++]=1;
     } else {
       pttn[k][*p]=1;
     }
     k++;
    }
#if (DEBUG)
printf("B:    k=%d \n",k);
#endif
    assert(k==name_len);
    int match=0;
    for (j=0;j<name_no;j++) {
      for (k=0;k<name_len;k++)
        if (pttn[k][names[j][k]]==0) 
          goto no_match;
      match++;
     no_match: ;
    }
    printf("Case #%d: %d\n",i+1,match);
  }
  return 0;
}
