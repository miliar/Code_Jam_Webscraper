#include <stdio.h>


int main(){
    char lopp[27]={"yhesocvxduiglbkrztnwjpfmaq"};
    int mitu;
    FILE* sisse;
    sisse=fopen("input.txt","r");
    FILE* valja;
    valja=fopen("output.txt","w");
    fscanf(sisse,"%d\n",&mitu);
    char read[102];
    int rida;
    for(int a=0;a<mitu;a++){
       rida=0;
       fgets(read,102,sisse);
       for(int b=0;b<102;b++){
         if(read[b]=='\n'){
           rida=b;
           break;
         }
       }
       fprintf(valja,"Case #%d: ",a+1);
       for(int b=0;b<rida;b++){
         if(read[b]!=32)
           fprintf(valja,"%c",lopp[read[b]-97]);
         else if(read[b]==32)
           fprintf(valja," ");
       }
       for(int b=0;b<102;b++){
         read[b]=0;
       }
       if(a!=mitu-1) fprintf(valja,"\n");
    }
}
