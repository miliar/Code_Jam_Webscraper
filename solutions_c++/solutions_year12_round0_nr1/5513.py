#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
char input[105];

void f()
{
    int i;
    for(i=0; input[i]; i++)
    {
        if(input[i]=='e') printf("o");
        else if(input[i]=='j') printf("u"); 
        else if(input[i]=='p') printf("r");
        else if(input[i]=='m') printf("l");   
        else if(input[i]=='y') printf("a");
        else if(input[i]=='s') printf("n");
        else if(input[i]=='l') printf("g");
        else if(input[i]=='c') printf("e");
        else if(input[i]=='k') printf("i");
        else if(input[i]=='t') printf("w");
        else if(input[i]=='d') printf("s");
        else if(input[i]=='x') printf("m");
        else if(input[i]=='v') printf("p");
        else if(input[i]=='n') printf("b");
        else if(input[i]=='r') printf("t");
        else if(input[i]=='i') printf("d");
        else if(input[i]=='w') printf("f");
        else if(input[i]=='f') printf("c");
        else if(input[i]=='a') printf("y");
        else if(input[i]=='u') printf("j");
        else if(input[i]=='z') printf("q");
        else if(input[i]=='b') printf("h");
        else if(input[i]=='g') printf("v");
        else if(input[i]=='h') printf("x");
        else if(input[i]=='o') printf("k");
        else if(input[i]=='q') printf("z");
        else printf(" ");
    }    
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,j;
    scanf("%d",&T);
    getchar();
    for(j=1; j<=T; j++)
    {
         gets(input);
         printf("Case #%d: ",j);
         f();
         printf("\n");
    }
    return 0;    
}
