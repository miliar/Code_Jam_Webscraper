#include<iostream.h>
#include<stdio.h>
#include<string.h>
#include<conio.h>

int Terrain[100][100],H,W,count=0;
char Map[100][100];

int findSink(int,int,char);
int findLowestNbr(int,int,int&,int&);
int changeMap(int,int,char);

int main()
{
 FILE *in,*out;
 in=fopen("input.txt","r"); // change input file name here
 out=fopen("out.txt","w");
 
 int T;
 fscanf(in,"%d",&T);
 
 int i,j,caseNo=0;
 char c='_',c2='a';

 while(caseNo<T)
 { 
 c='_';
 for(i=0;i<H;i++)
 {
  for(j=0;j<W;j++)
  {
   Map[i][j]='\0';
   Terrain[i][j]=-1;
  }
 }
 
 fscanf(in,"%d %d",&H,&W);
 
 for(i=0;i<H;i++)
  for(j=0;j<W;j++)
   fscanf(in,"%d",&Terrain[i][j]);
   
 i=j=0;  
 int h,k,max,flag=1;

 while(flag)
 {
       max=0;
       h=0,k=0;
       for(i=0;i<H;i++)
       {
        for(j=0;j<W;j++)
        {
            if((Map[i][j]=='\0')&&(max<=Terrain[i][j]))
            {
            max=Terrain[i][j];
            h=i;
            k=j;
            }
        }
       } 
       findSink(h,k,c);
       flag=0;
       for(i=0;i<H;i++)
       {
            for(j=0;j<W;j++)
            {
                 if(Map[i][j]=='\0')
                 {
                 flag=1;
                 break;
                 }
            }    
        }
       c--;
 }

 c2='a';
 
 
  for(i=0;i<H;i++)
    for(j=0;j<W;j++)
      if((Map[i][j]>'z')||(Map[i][j]<'a')||(c2<Map[i][j]))
      {
      changeMap(i,j,c2);
      c2++;
      }

    

 fprintf(out,"Case #%d:\n",caseNo+1); 

  for(i=0;i<H;i++)
  {
  for(j=0;j<W;j++)
   fprintf(out,"%c ",Map[i][j]); 
  fprintf(out,"\n"); 
 }

 count=0;
 c='a';
 caseNo++;  
 }
  
  fclose(in);
  fclose(out);
  //getch();  
    
}


int findSink(int i,int j,char c)
{
    int h=0,k=0;
    if(Map[i][j]=='\0')
     Map[i][j]=c;
    else
     changeMap(i,j,c);
     
    count++; 
    
    if(findLowestNbr(i,j,h,k))
     findSink(h,k,c);
}


int findLowestNbr(int i,int j,int &h,int &k)
{
    int min=Terrain[i][j];
    h=i;
    k=j;
    if((i+1)<H)
    {
           if(Terrain[i+1][j]<=min)
           {
             min=Terrain[i+1][j];
             h=i+1;
             k=j;
           }
    }
    if((j+1)<W)
    {
           if(Terrain[i][j+1]<=min)
           {
             min=Terrain[i][j+1];
             h=i;
             k=j+1;
           }
    }
    if((j-1)>=0)
    {
           if(Terrain[i][j-1]<=min)
           {
             min=Terrain[i][j-1];
             h=i;
             k=j-1;
           }
    }
    if((i-1)>=0)
    {
           if(Terrain[i-1][j]<=min)
           {
             min=Terrain[i-1][j];
             h=i-1;
             k=j;
           }
    }
    
    if(min==Terrain[i][j])
    return 0;
    
    return 1;
    
}


int changeMap(int h,int k,char c)
{
 int i,j;
 char a=Map[h][k];
 for(i=0;i<H;i++)
    for(j=0;j<W;j++)
      if(Map[i][j]==a)
         Map[i][j]=c;

 return 0;
}
