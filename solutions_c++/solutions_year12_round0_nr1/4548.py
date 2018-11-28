#include<stdio.h>
#include<stdlib.h>


int n;
char t[1000];

int main(){
    freopen("output.txt","w",stdout);
    gets(t);
    n=atoi(t);
    
    for(int i=0;i<n;i++)
    {
        printf("Case #%d: ",i+1);
        gets(t);   
        for(int k=0;t[k]!='\0';k++)
        {
            char c=0;
            switch(t[k]){
            case 'a': printf("y"); break;
            case 'b': printf("h"); break;
            case 'c': printf("e"); break;
            case 'd': printf("s"); break;
            case 'e': printf("o"); break;
            case 'f': printf("c"); break;
            case 'g': printf("v"); break;
            case 'h': printf("x"); break;
            case 'i': printf("d"); break;
            case 'j': printf("u"); break;
            case 'k': printf("i"); break;
            case 'l': printf("g"); break;
            case 'm': printf("l"); break;
            case 'n': printf("b"); break;
            case 'o': printf("k"); break;
            case 'p': printf("r"); break;
            case 'q': printf("z"); break;
            case 'r': printf("t"); break;
            case 's': printf("n"); break;
            case 't': printf("w"); break;
            case 'u': printf("j"); break;
            case 'v': printf("p"); break;
            case 'w': printf("f"); break;
            case 'x': printf("m"); break;
            case 'y': printf("a"); break;
            case 'z': printf("q"); break;
            default: printf("%c",t[k]);
            }
        }
        printf("\n");   
    }
    

    system("pause");
    return 0;
}
