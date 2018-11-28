#include "stdio.h"
#include "conio.h"
#include "string.h"
#define L_Limit 15
#define D_Limit 500
#define N_Limit 500
int L,D,N;
char dic[D_Limit][L_Limit];
int validpattern(char pattern[L_Limit*L_Limit])
{
  int i=0,j=0;
  for(i=0;i<D;i++)
  {
   j=0;
   while(1==1)
   {
    if(pattern[j]=='(')
    {
     return 1;
    }
    if(dic[i][j]!=pattern[j])
    {
     break;
    }
    else
    {
     j++;
    }
    if(j>strlen(pattern))
    {
     return 1;
    }
   }
  }
  return 0;
}

int process(char pattern[L_Limit*L_Limit])
{
 char tokens[L_Limit][L_Limit];
 char newpattern[L_Limit*L_Limit];
 int i,j,k,p,q,r,multicar=2;
 int words=0;
 i=0,j=0,k=0;
 for(i=0;i<strlen(pattern);i++)
 {
  if(pattern[i]=='(')
  {
   multicar=1;
  }else if(pattern[i]==')')
  {
   multicar=0;
  }else
  {
   tokens[j][k++]=pattern[i];
  }
  if(multicar==0)
  {
   tokens[j][k++]='\0';
   //printf("token: %s\n",tokens[j]);
   for(p=0;p<strlen(tokens[j]);p++)
   {
    strcpy(newpattern,"");
    strncat(newpattern,pattern,j);
    strncat(newpattern,tokens[j]+p,1);
    strncat(newpattern,pattern+strlen(newpattern)+strlen(tokens[j])+1,strlen(pattern)-(strlen(newpattern)+strlen(tokens[j])+1));
    //printf("newpatern:%s\n",newpattern);
    if(validpattern(newpattern)==1)
    {
     words+=process(newpattern+'\0');
    }
   }
   j++;
   k=0;
   break;
  }
  if(multicar==2)
  {
   tokens[j][k++]='\0';
   j++;
   k=0;

  }
 }
 if(multicar==2)
 {
  return validpattern(pattern);
 }
 return words;
}
void main()
{
 clrscr();
 char * pattern;
 FILE * infile;
 FILE * outfile;
 int i,j,k;
 infile=fopen("D:\\GCJ\\2009\\A-small.in","r");
 outfile=fopen("D:\\GCJ\\2009\\A-small.out","w+");
 fscanf(infile,"%d %d %d\n",&L,&D,&N);
 //printf("%d %d %d",L,D,N);
 for(i=0;i<D;i++)
 {
  fscanf(infile,"%s\n",dic[i]);
  //fprintf(outfile,"%s\n",dic[i]);
  //printf("%s\n",dic[i]);
 }
 for(i=0;i<N;i++)
 {
  //pattern="";
  fscanf(infile,"%s\n",pattern);
  //printf("patern: %s\n",pattern);
  //printf("%d",validpattern("ab(bc)"));
  //fprintf(outfile,"Case #%d: %d\n",i+1,process(pattern));
  printf("Case #%d: %d\n",i+1,process(pattern));
 }
 fclose(infile);
 fclose(outfile);
 //printf("Hello World");
 getch();
}
