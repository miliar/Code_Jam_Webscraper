#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    int pin[26]={121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};
    char c;
    int l,T,tmp;
    FILE*read=fopen("A-small-attempt2.in","r");
    fscanf(read,"%d\n",&T);
    FILE*write=fopen("A-small-attempt2.out","w");
    for(int i=1;i<=T;i++)
    {
     fprintf(write , "Case #%d: ",i);
     do
     {
        c=fgetc(read);
        l=c;
        if(l==32)
                fprintf(write," ");
        else if (l!=10 and l != EOF)
             fputc (pin[l-97] , write );
     }while(l != 10 and l != EOF);
     fscanf(read,"\n");
     fprintf(write,"\n");
    }
    fclose(read);
    fclose(write);
    return 0;
}
