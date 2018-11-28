#include<iostream.h>
#include<string.h>'
#include<stdio.h>
#include<conio.h>

char Map[50][50];

int breakDown(char A[]);
int search(char ,char a[]);

int main()
{
 FILE *in,*out;
 in=fopen("input.txt","r"); // change input file name here
 int L,D,N;
 char DA[5000][16];
 char testCase[500][500];
 int i;
 
 fscanf(in,"%d %d %d",&L,&D,&N);
 for(i=0;i<D;i++)
  fscanf(in,"%s",DA[i]);
  
 for(i=0;i<N;i++)
   fscanf(in,"%s",testCase[i]);
 
 fclose(in);

 out=fopen("out.txt","w");
 char temp[20];
 int caseNo=0,count=0,mapDepth,j,flag=1,maxj;
 
 for(i=0;i<50;i++)
 for(j=0;j<50;j++)
 Map[i][j]='\0';

 while(caseNo<N)
 {
  count=0;
  mapDepth=breakDown(testCase[caseNo]);
  
  for(i=0;i<D;i++)
  {
    j=0;
    maxj=strlen(DA[i]);
    while(j<maxj)
    {
         if(!search(DA[i][j],Map[j]))
         {
         flag=0;
         break;
         }
         j++;
    }
     if(flag)
     count++;
     flag=1;
   }
    
  fprintf(out,"Case #%d: %d \n",caseNo+1,count); 
  caseNo++;
  
  for(i=0;i<50;i++)
    for(j=0;j<50;j++)
       Map[i][j]='\0';
  cout<<"\nCase ::"<<caseNo;
 }//evaluates Each Case
 fclose(out);
 return 0;
}

int breakDown(char A[])
{
 int i=0,j=0,k=0,max=strlen(A);
 char c;
 while(i<max)
 {
  c=A[i];
  if(c=='(')
  {
      i++;      
      c=A[i];
      while(c!=')')
        {         
         Map[j][k]=c;
         i++;
         k++;
         c=A[i];
        }
      i++;
      Map[j][k]='\0';
      k=0;
      j++;
      continue;  
  }  
  Map[j][k]=c;
  k=0;  
  i++;
  j++;
 }
 return j;
}


int search(char c,char A[])
{
  int max=strlen(A),i;
  for(i=0;i<max;i++)
  {
    if(A[i]==c)
    return 1;
  }
  return 0;
}

