#include <stdio.h>
#include <stdlib.h>
#include <string.h>



main() 
{
 FILE *fp1,*fp2;
 char tmpstr[20];
 int main[100][100];
 int min;
 char out[100][100],sink[100][100],dir[100][100];
 char c='0';
 
 int i,j,k,T,H,W,mc;
 int i1,j1,i2,j2;
 int sta[10000][2];
 int top=0;
 
 fp1 = fopen("B-large.in","r");
 fp2 = fopen("out.txt","w");
 
 //get T
 i=0;
 c=getc(fp1);
 while(c!='\n')
 {
  tmpstr[i]=c;
  i++;
  tmpstr[i]='\0';
  c=getc(fp1);
 }
 T=atoi(tmpstr);
 //printf("T=%d\n",T);
 
 for(mc=0;mc<T;mc++)
 {
  //printf("\nmc=%d\n",mc);
  //get H
  i=0;
  c=getc(fp1);
  while(c!=' ')
  {
   tmpstr[i]=c;
   i++;
   tmpstr[i]='\0';
   c=getc(fp1);
  }
  H=atoi(tmpstr);
  //printf("H=%d\n",H);
  
  //get W
  i=0;
  c=getc(fp1);
  while(c!='\n')
  {
   tmpstr[i]=c;
   i++;
   tmpstr[i]='\0';
   c=getc(fp1);
  }
  W=atoi(tmpstr);
  //printf("W=%d\n",W);
  
  //get altitudes
  for(i=0;i<H;i++)
  {
   for(j=0;j<W;j++)
   {
    //initiallization
    for(i1=0;i1<100;i1++)
    {
     for(j1=0;j1<100;j1++)
     {
      out[i1][j1]='0';
      dir[i1][j1]='0';
     }
    }
    k=0;
    c=getc(fp1);
    
    while(c!=' ' && c!='\n' && c!=EOF)
    {
     tmpstr[k]=c;
     k++;
     tmpstr[k]='\0';
     c=getc(fp1);
    }
    main[i][j]=atoi(tmpstr);
    //printf("(%d,%d)=%d ",i,j,main[i][j]);
   }
   //printf("\n");
  }
  
  //set direction for each number
  for(i=0;i<H;i++)
  {
   for(j=0;j<W;j++)
   {
    min=main[i][j];
    //check N
    if((i-1)>=0)
    {
     if(main[i-1][j]<min)
     {
      dir[i][j]='N';
      min=main[i-1][j];
     }
    }
    //check W
    if((j-1)>=0)
    {
     if(main[i][j-1]<min)
     {
      dir[i][j]='W';
      min=main[i][j-1];
     }
    }
    //check E
    if((j+1)<W)
    {
     if(main[i][j+1]<min)
     {
      dir[i][j]='E';
      min=main[i][j+1];
     }
    }
    //check S
    if((i+1)<H)
    {
     if(main[i+1][j]<min)
     {
      dir[i][j]='S';
      min=main[i+1][j];
     }
    }
   }
  }
  
  //generate output
  c='a';
  for(i=0;i<H;i++)
  {
   for(j=0;j<W;j++)
   {
    i1=i;
    j1=j;
    
    while(1)
    {
     if(out[i1][j1]=='0')
     {
      out[i1][j1]=c;
      //push it to stack
      sta[top][0]=i1;
      sta[top][1]=j1;
      top++;
      if(dir[i1][j1]=='N')
      {
       i1--;
      }
      else if(dir[i1][j1]=='E')
      {
       j1++;
      }
      else if(dir[i1][j1]=='W')
      {
       j1--;
      }
      else if(dir[i1][j1]=='S')
      {
       i1++;
      }
      else if(dir[i1][j1]=='0')
      {
       //empty stack and continue loop
       //printf(" %d %d %c ",i1,j1,out[i1][j1]);
       top=0;
       break;
      }
     }
     else
     {
      //start popping
      while(top!=0)
      {
       top--;
       i2=sta[top][0];
       j2=sta[top][1];
       //printf(" %d %d ",i2,j2);
       
       out[i2][j2]=out[i1][j1];
      }
      c--;
      break;
     }
    }
    c++;
   }
  }
  fprintf(fp2,"Case #%d:\n",mc+1);
  //test
  for(i=0;i<H;i++)
  {
   for(j=0;j<W;j++)
   {
    fprintf(fp2,"%c",out[i][j]);
    if(j!=W-1)
     fprintf(fp2," ");
   }
   fprintf(fp2,"\n");
  }
  
  
 }
 
 
 fclose(fp1);
 fclose(fp2);
 system("pause");
 return 0;
}
