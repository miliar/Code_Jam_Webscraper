#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define STRLEN 1002
void main()
{
 int l,d,n,n1;
 char str[STRLEN],str1[16],*p,*p1;
 char **lang,**arr;
 int *len,*tmp,size,i,j,k,flag,flag1;
 long count;
 printf("Enter input file name:");
 scanf("%s",str);
 FILE *readf=fopen(str,"r");
 printf("Enter output file name:");
 scanf("%s",str);
 FILE *writef=fopen(str,"w");
 fgets(str,STRLEN,readf);
 l=atoi(str);
 p=strchr(str+1,' ');
 d=atoi(p);
 p=strchr(p+1,' ');
 n=atoi(p);
 lang=(char **)malloc(d*sizeof(char *));
 arr=(char **)malloc(l*sizeof(char *));
 len=new int[l];
 tmp=new int[l];
 for(i=0;i<d;i++)
 {
  fgets(str,STRLEN,readf);
  str[strlen(str)-1]='\0';
  lang[i]=(char *)malloc((l+1)*sizeof(char));
  strcpy(lang[i],str);
 }
 n1=n;
 while(n)
 {
  flag=0;
  n--;
  fgets(str,STRLEN,readf);
  p=str;
  for(i=0;i<l;i++)
  {
   while(*p==' ')
    p++;
   if(*p=='(')
   {
    p1=strchr(p,')');
    size=p1-p-1;
    p++;
   }
   else
    size=1;
   arr[i]=(char *)malloc(sizeof(char)*size);
   len[i]=size;
   tmp[i]=0;
   for(j=0;j<size;j++)
   {
    arr[i][j]=*p;
    p++;
   }
   k=i;
   do
   {
    flag1=0;
    do
    {
     str1[k]=arr[k][tmp[k]];
     for(j=0;j<d && strncmp(lang[j],str1,k+1);j++);
     if(j<d)
      break;
     tmp[k]++;
    }while(tmp[k]<len[k]);

    while(k>0 && tmp[k]==len[k])
    {
     tmp[k]=0;
     k--;
     tmp[k]++;
    }
    if(k==0 && tmp[k]==len[k])
     break;
    if(j<d && k!=i)
    {
     k++;
     flag1=1;
    }
   }while(k!=i||flag1);
   if(tmp[k]==len[k])
   {
     fprintf(writef,"Case #%d: 0\n",n1-n);
     for(k=i;k>=0;k--)
      free(arr[k]);
     flag=1;
     break;
   }
   if(*p==')')
    p++;

  }
  count=0;
  while(flag==0)
  {
   for(i=0;i<l;i++)
    str[i]=arr[i][tmp[i]];
   str[i]='\0';
   for(i=0;i<d && strcmp(str,lang[i]);i++);
   if(i<d)
    count++;
   for(i=l-1;i>=0;i--)
   {
    tmp[i]++;
    if(i<l-1)
     tmp[i+1]=0;
    if(len[i]!=tmp[i])
     break;
   }
   if(i==-1)
    break;

   k=i;
   do
   {
    flag1=0;
    do
    {
     str[k]=arr[k][tmp[k]];
     for(j=0;j<d && strncmp(lang[j],str,k+1);j++);
     if(j<d)
      break;
     tmp[k]++;
    }while(tmp[k]<len[k]);

    while(k>0 && tmp[k]==len[k])
    {
     tmp[k]=0;
     k--;
     tmp[k]++;
    }
    if(k==0 && tmp[k]==len[k])
     break;
    if(j<d && k!=i)
    {
     k++;
     flag1=1;
    }
   }while(k!=i||flag1);
   if(tmp[k]==len[k])
    break;
  }
  if(flag==0)
  {
   fprintf(writef,"Case #%d: %ld\n",n1-n,count);
   for(i=0;i<l;i++)
    free(arr[i]);
  }
 }
 free(lang);
 free(arr);
 delete len;
 delete tmp;
 fclose(readf);
 fclose(writef);
}
