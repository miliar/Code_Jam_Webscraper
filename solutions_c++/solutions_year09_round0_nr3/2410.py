#include<stdio.h>
#include<stdlib.h>
#include<STRING.h>
#define STRLEN 501
char *ptr="welcome to code jam";
int count(char *str,char *p)
{
 int c=0;
 if(*p==NULL)
 {
  c+=1;
  p=ptr;
 }
 if(*str=='\n')
  return c;
 str=strchr(str,*p);
 if(!str)
  return c;
 return(c+count(str+1,p)+count(str+1,p+1));
}
void main()
{
 int n,n1,c;
 char str[STRLEN];
 printf("Enter input file name:");
 scanf("%s",str);
 FILE *readf=fopen(str,"r");
 printf("Enter output file name:");
 scanf("%s",str);
 FILE *writef=fopen(str,"w");
 fgets(str,STRLEN,readf);
 str[strlen(str)-1]='\0';
 n1=n=atoi(str);
 while(n)
 {
  n--;
  fgets(str,STRLEN,readf);
  c=count(str,ptr) %10000;
  fprintf(writef,"Case #%d: ",n1-n);
  for(int digits=1000;digits!=1&&c<digits;digits/=10)
   fprintf(writef,"0");
  fprintf(writef,"%d\n",c);
 }
 fclose(readf);
 fclose(writef);
}
