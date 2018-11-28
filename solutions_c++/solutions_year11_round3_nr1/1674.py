#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    int t;
    FILE *fin = fopen("Input.txt","r");
    FILE *fout = fopen("Output.txt","w+");
    fscanf(fin,"%d",&t);
    for(int k=1;k<=t;k++)
    {
              int r,c;
              fscanf(fin,"%d%d",&r,&c);
              char str[r][c];
              for(int i=0;i<r;i++)
              {
                      fscanf(fin,"%s",str[i]);  
              }
              bool b=1;
              for(int i=0;i<r&&b;i++)
              {
                      for(int j=0;j<c&&b;j++)
                      {
                              if(str[i][j]=='#')
                              {
                                                if(i+1>=r||j+1>=c) {b=0;break;}
                                                else if(str[i+1][j]!='#'||str[i][j+1]!='#'||str[i+1][j+1]!='#') {b=0;break;}
                                                else 
                                                {
                                                     str[i][j]='/';
                                                     str[i+1][j+1]='/';
                                                     str[i+1][j]='\\';
                                                     str[i][j+1]='\\';
                                                 }
                              }
                      }
              }
              if(!b) fprintf(fout,"Case #%d:\nImpossible\n",k);
              else {
                           fprintf(fout,"Case #%d:\n",k);
                           for(int i=0;i<r;i++)
                           {
                                   for(int j=0;j<c;j++)fprintf(fout,"%c",str[i][j]);
                                   fprintf(fout,"\n");
                           }
                   }
    }
}
