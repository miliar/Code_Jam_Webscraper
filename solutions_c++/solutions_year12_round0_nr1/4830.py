/*
 Mahverik.Maven
 Using DevCpp 4.9.9.2
 Used input and output redirection instead of file I/O.
 Problem A : Bot Trust
*/
 
#include<stdio.h>
#define abs(x) (((x)>=0)?(x):-(x))
#define max(a,b) ((a)>=(b)?(a):(b))

main()
{
 int test,ttest; scanf("%d ",&ttest); 
 char *code= "yhesocvxduiglbkrztnwjpfmaq"; char c=0;
 
 for(test=1;test<=ttest;test++)
 {                    
  printf("Case #%d: ",test); c=0; 
  while((c=getchar())!='\n'&&c>0) { printf("%c",code[c-'a']); }
  printf("\n");
 }      
 printf("\b");
}
