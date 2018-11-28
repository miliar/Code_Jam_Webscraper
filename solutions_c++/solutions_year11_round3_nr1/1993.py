#include<stdio.h>
#include<conio.h>
FILE *fp,*fp2;
  
int main()
{
  int k,l,t;
  fp=fopen("f.in","r");
  fp2=fopen("f.out","w");  
  fscanf(fp,"%d",&t);
  for (int x=1;x<=t;x++)
  {int n,r,co;
   char c[50][50];
  fprintf(fp2,"Case #%d:\n",x);
  printf("Case #%d:\n",x);
  fscanf(fp,"%d%d",&r,&co);
  for(int i=0;i<r;i++)
  {
  for(int j=0;j<co;j++)
  {
  fscanf(fp,"%c",&c[i][j]);
  printf("%c",c[i][j]);
  if(c[i][j]!='#' && c[i][j]!='.')
  { j--;
    continue;
  }        
  }        
  } 
  int flag=1;
  for(int i=0;i<r && flag==1;i++)
  { 
  for(int j=0;j<co && flag==1 ;j++)
  {
          if(c[i][j] == '#')
          { 
            if(i+1<r && j+1<co && c[i][j+1] == '#' && c[i+1][j] == '#' && c[i+1][j+1] == '#')
            { c[i][j]='/';
              c[i][j+1]='\\';
              c[i+1][j]='\\';
              c[i+1][j+1]='/';
            }
            else
            {flag=0;}
          }
  }
  }
  if(flag==0)
  {fprintf(fp2,"Impossible\n");
  }
  else
  {
  for(int i=0;i<r && flag==1 ;i++)
  { 
  for(int j=0;j<co && flag==1 ;j++)
  { fprintf(fp2,"%c",c[i][j]);
  }
  fprintf(fp2,"\n");
  }
  }
  }
  getch();       
 return 0;   
}
