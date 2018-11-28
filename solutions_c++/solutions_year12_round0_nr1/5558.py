#include<stdio.h>
#include<stdlib.h>

int T,TC=0,i=0;
char G[35][105];

int main()
{
    scanf("%d\n",&T);
    for(;TC<T;TC++)
    {   
        fgets(G[TC],105,stdin);        
    }
    for(TC=0;TC<T;TC++)
    {
        i=0;    
        while(G[TC][i]!='\0')
        {
            switch(G[TC][i])
            {
                case 'a': G[TC][i]='y'; break;
                case 'b': G[TC][i]='h'; break;
                case 'c': G[TC][i]='e'; break;
                case 'd': G[TC][i]='s'; break;
                case 'e': G[TC][i]='o'; break;
                case 'f': G[TC][i]='c'; break;
                case 'g': G[TC][i]='v'; break;
                case 'h': G[TC][i]='x'; break;
                case 'i': G[TC][i]='d'; break;
                case 'j': G[TC][i]='u'; break;
                case 'k': G[TC][i]='i'; break;
                case 'l': G[TC][i]='g'; break;
                case 'm': G[TC][i]='l'; break;
                case 'n': G[TC][i]='b'; break;
                case 'o': G[TC][i]='k'; break;
                case 'p': G[TC][i]='r'; break;
                case 'q': G[TC][i]='z'; break;
                case 'r': G[TC][i]='t'; break;
                case 's': G[TC][i]='n'; break;
                case 't': G[TC][i]='w'; break;
                case 'u': G[TC][i]='j'; break;
                case 'v': G[TC][i]='p'; break;
                case 'w': G[TC][i]='f'; break;
                case 'x': G[TC][i]='m'; break;
                case 'y': G[TC][i]='a'; break;
                case 'z': G[TC][i]='q'; break;
             }
            i++;
            
        }
        printf("Case #%d: %s\n",TC+1,G[TC]);
     }
     return 1;
}
                        
                        