#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

char translate(char);


int main()
{

FILE * f, * g;
f=fopen("A-small-attempt4.in","r");
g=fopen("output.out","w");


int x,i=1;
char c,c_new;

fscanf (f,"%d",&x);

fscanf(f,"%c",&c);  
fprintf(g,"Case #%d: ",i);

for (;;)
    {
    fscanf(f,"%c",&c);  
    c_new=translate(c);
    
    if (i==x && c=='\n') break;
    
    if (feof(f)) break;
    
    fprintf(g,"%c",c_new);
    
    if (c=='\n' && i<x) {
                 i++;
                 fprintf(g,"Case #%d: ",i);
                 }
    }

return 0;
}



char translate(char c){

switch (c){
       
case 'a' : return 'y';
case 'b' : return 'h';
case 'c' : return 'e';
case 'd' : return 's';
case 'e' : return 'o';
case 'f' : return 'c';
case 'g' : return 'v';
case 'h' : return 'x';
case 'i' : return 'd';
case 'j' : return 'u';
case 'k' : return 'i';
case 'l' : return 'g';
case 'm' : return 'l';
case 'n' : return 'b';
case 'o' : return 'k';
case 'p' : return 'r';
case 'q' : return 'z';
case 'r' : return 't';
case 's' : return 'n';
case 't' : return 'w';
case 'u' : return 'j';
case 'v' : return 'p';
case 'w' : return 'f';
case 'x' : return 'm';
case 'y' : return 'a';
case 'z' : return 'q';
case '\n': return '\n';
case ' ' : return ' ';  
}     

}
