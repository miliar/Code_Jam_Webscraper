#include<stdio.h>
using namespace std;
char map[]="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
    int i,x;
    char c;
    char fname[32];
    char outfile[]="outputA.txt";
    printf("Enter name of input file: ");
    scanf("%s",fname);
    FILE *fin=fopen(fname,"r"), *fout=fopen(outfile,"w");
    fscanf(fin,"%d",&x);
    fgetc(fin);
      for(i=0;i<x;i++)
      {
                      fprintf(fout,"Case #%d: ",i+1);
                      c=fgetc(fin);
                      while((c!='\n')&&(c!=EOF))
                      {
                                    if(c!=' ')
                                    c=map[c-'a'];
                                    fputc((int)c,fout);
                                    c=fgetc(fin);
                      }
                      fputc((int)'\n',fout);
      }          
   return 0;
   
}                                         
                       
