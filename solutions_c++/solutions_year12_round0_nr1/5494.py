#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *fr,*fw;
    fr = fopen("C:\\in2.in","r");
    fw = fopen("C:\\out2.out","w+");
    
    int t,k=0;
    fscanf(fr,"%d",&t);
    char* in;
    fgets(in,100,fr);
    
    while(k++<t){
          fgets(in,1000,fr);
          
          int len = strlen(in);
          
          fprintf(fw,"Case #%d: ",k);   
          
          for(int i = 0; i < len; i++){
            switch (in[i]) { 
                case 'a': fprintf(fw,"y");  break;
                case 'b': fprintf(fw,"h");  break;
                case 'c': fprintf(fw,"e");  break;
                case 'd': fprintf(fw,"s");  break;
                case 'e': fprintf(fw,"o");  break;
                case 'f': fprintf(fw,"c");  break;
                case 'g': fprintf(fw,"v");  break;
                case 'h': fprintf(fw,"x");  break;
                case 'i': fprintf(fw,"d");  break;
                case 'j': fprintf(fw,"u");  break;
                case 'k': fprintf(fw,"i");  break;
                case 'l': fprintf(fw,"g");  break;
                case 'm': fprintf(fw,"l");  break;
                case 'n': fprintf(fw,"b");  break;
                case 'o': fprintf(fw,"k");  break;
                case 'p': fprintf(fw,"r");  break;
                case 'q': fprintf(fw,"z");  break;
                case 'r': fprintf(fw,"t");  break;
                case 's': fprintf(fw,"n");  break;
                case 't': fprintf(fw,"w");  break;
                case 'u': fprintf(fw,"j");  break;
                case 'v': fprintf(fw,"p");  break;
                case 'w': fprintf(fw,"f");  break;
                case 'x': fprintf(fw,"m");  break;
                case 'y': fprintf(fw,"a");  break;
                case 'z': fprintf(fw,"q");  break;
                case ' ': fprintf(fw," ");  break;
                default : fprintf(fw,"%c",in[i]);
                }
          }    
    }
    fclose(fr);
    fclose(fw);
    
    //system("pause");
    
    return 0;   
}
