#include<stdio.h>
#include<stdlib.h>


int main()
{
  FILE *fp,*fp1;
  fp = fopen("A-small-attempt0.in","r");
  fp1 = fopen("output.txt","w");
  if(fp == NULL || fp1 == NULL){
    exit(0);
  }
  int T;
  
  fscanf(fp,"%d",&T);
  int count = T-1;
  int tCount = T;
  
  char ch_map[26][2] = {
  {'a','y'},
{'b','h'},
{'c','e'},
{'d','s'},
{'e','o'},
{'f','c'},
{'g','v'},
{'h','x'},
{'i','d'},
{'j','u'},
{'k','i'},
{'l','g'},
{'m','l'},
{'n','b'},
{'o','k'},
{'p','r'},
{'q','z'},
{'r','t'},
{'s','n'},
{'t','w'},
{'u','j'},
{'v','p'},
{'w','f'},
{'x','m'},
{'y','a'},
{'z','q'}
};
  char input[101];
  char output[101];
  int index = -1;
 fgetc(fp);
  while( tCount > 0 ){
    fscanf(fp,"%[^\n]",input);
    fgetc(fp);
  // printf("%s%d\n",input,sizeof(input));
   int i = 0;
    for( ; i < 100;i++){
        //printf("%c\n",input[i]);
    if(input[i] =='\0'){
    break;
    }
    if(input[i]==' '){
    output[i] = ' ';
    //printf("%c test \n",input[i]);
        continue;
    }
    index = (int)input[i] - 97 ;
    //printf("%d test \n",index);
    output[i] = ch_map[index][1];
    }
    output[i]='\0';
     fprintf(fp1,"Case #%d: %s\n",(T-count),output);
    
    count--;
    tCount--;
  }
  fclose(fp);
  fclose(fp1);
  return 1;
} 
