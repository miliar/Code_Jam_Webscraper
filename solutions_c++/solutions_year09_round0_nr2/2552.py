#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define STRLEN 602
int **arr,h,w;
char **res;

void readarr(char *str,int *arr,int w)
{
 for(int i=0;i<w;i++)
 {
  arr[i]=atoi(str);
  str=strchr(str+1,' ')+1;
 }
}

void out(int &i,int &j)
{
 int k=i,l=j;
 int min=arr[i][j];
 if(i-1>=0 && arr[i-1][j]<min)
 {
  k=i-1;
  l=j;
  min=arr[k][l];
 }
 if(j-1>=0 && arr[i][j-1]<min)
 {
  k=i;
  l=j-1;
  min=arr[k][l];
 }
 if(j+1<w && arr[i][j+1]<min)
 {
  k=i;
  l=j+1;
  min=arr[k][l];
 }
 if(i+1<h && arr[i+1][j]<min)
 {
  k=i+1;
  l=j;
  min=arr[k][l];
 }
 i=k;
 j=l;
}

void in(int i,int j,char c)
{
 int k,l;
 if(i-1>=0 && arr[i-1][j]>arr[i][j])
 {
  k=i-1;
  l=j;
  out(k,l);
  if(i==k && j==l && res[k-1][l]==0)
  {
   res[k-1][l]=c;
   in(k-1,l,c);
  }
 }
 if(j-1>=0 && arr[i][j-1]>arr[i][j])
 {
  k=i;
  l=j-1;
  out(k,l);
  if(i==k && j==l && res[k][l-1]==0)
  {
   res[k][l-1]=c;
   in(k,l-1,c);
  }
 }
 if(j+1<w && arr[i][j+1]>arr[i][j])
 {
  k=i;
  l=j+1;
  out(k,l);
  if(i==k && j==l && res[k][l+1]==0)
  {
   res[k][l+1]=c;
   in(k,l+1,c);
  }
 }
 if(i+1<h && arr[i+1][j]>arr[i][j])
 {
  k=i+1;
  l=j;
  out(k,l);
  if(i==k && j==l && res[k+1][l]==0)
  {
   res[k+1][l]=c;
   in(k+1,l,c);
  }
 }
 out(i,j);
 if(res[i][j]==0)
 {
  res[i][j]=c;
  in(i,j,c);
 }
}

void main()
{
 int t,t1,i,j;
 char str[STRLEN],*p,c;
 printf("Enter input file name:");
 scanf("%s",str);
 FILE *readf=fopen(str,"r");
 printf("Enter output file name:");
 scanf("%s",str);
 FILE *writef=fopen(str,"w");
 fgets(str,STRLEN,readf);
 str[strlen(str)-1]='\0';
 t=atoi(str);
 t1=t;
 while(t)
 {
  t--;
  c='a';
  fgets(str,STRLEN,readf);
  h=atoi(str);
  p=str;
  p=strchr(p+1,' ');
  w=atoi(p);
  arr=(int **)malloc(sizeof(int *)*h);
  res=(char **)malloc(sizeof(char *)*h);
  for(i=0;i<h;i++)
  {
   arr[i]=(int *)malloc(sizeof(int)*w);
   res[i]=(char *)calloc(w,sizeof(char));
   fgets(str,STRLEN,readf);
   readarr(str,arr[i],w);
  }
  for(i=0;i<h;i++)
   for(j=0;j<w;j++)
    if(res[i][j]==0)
    {
     res[i][j]=c;
     in(i,j,c);
     c++;
    }
  fprintf(writef,"Case #%d:\n",t1-t);
  for(i=0;i<h;i++)
  {
   for(j=0;j<w;j++)
   {
    fprintf(writef,"%c",res[i][j]);
    if(j<w-1)
     fprintf(writef," ");
   }
   fprintf(writef,"\n");
   free(res[i]);
   free(arr[i]);
  }
  free(arr);
  free(res);
 }
 fclose(readf);
 fclose(writef);
}


