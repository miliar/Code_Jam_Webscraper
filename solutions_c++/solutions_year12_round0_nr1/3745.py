#include<stdio.h>
int main ()
{
    int n;
    int i,j;
    char g[100];
    scanf( "%d " , &n ) ;
    for ( j = 0 ; j < n; j++ )
    {
        i=0;
        printf("Case #%d: ",j+1);
        do
        {
            scanf("%c",&g[i]);
            if(g[i]>='a' && g[i]<='z') 
            {
            if(g[i]=='a') printf("%c", 'y');
            if(g[i]=='b') printf("%c", 'h');
            if(g[i]=='c') printf("%c", 'e');
            if(g[i]=='d') printf("%c", 's');
            if(g[i]=='e') printf("%c", 'o');
            if(g[i]=='f') printf("%c", 'c');
            if(g[i]=='g') printf("%c", 'v');
            if(g[i]=='h') printf("%c", 'x');
            if(g[i]=='i') printf("%c", 'd');
            if(g[i]=='j') printf("%c", 'u');
            if(g[i]=='k') printf("%c", 'i');
            if(g[i]=='l') printf("%c", 'g');
            if(g[i]=='m') printf("%c", 'l');
            if(g[i]=='n') printf("%c", 'b');
            if(g[i]=='o') printf("%c", 'k');
            if(g[i]=='p') printf("%c", 'r');
            if(g[i]=='q') printf("%c", 'z');
            if(g[i]=='r') printf("%c", 't');
            if(g[i]=='s') printf("%c", 'n');
            if(g[i]=='t') printf("%c", 'w');
            if(g[i]=='u') printf("%c", 'j');
            if(g[i]=='v') printf("%c", 'p');
            if(g[i]=='w') printf("%c", 'f');
            if(g[i]=='x') printf("%c", 'm');
            if(g[i]=='y') printf("%c", 'a');
            if(g[i]=='z') printf("%c", 'q');
            }
            else
            printf("%c",g[i]);
        }while(g[i]!='\n');
    }
    return 0;
}
