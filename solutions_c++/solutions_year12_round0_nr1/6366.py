#include<stdio.h>
#include<string.h>
//#include<conio.h>

int main() 
{
freopen("A-small-attempt2.in","r",stdin);
freopen("recycleanssmal2.txt","w",stdout);
    int t,i=0;
    
    scanf("%d",&t);
    while(i<=t)
    {i++; 
              int j=0;
    char g[101];
//    memset (g,'0',100);
    gets(g);
   
    while(j<strlen(g)) 
    {
   if(j==0) {printf("Case #%d: ",(i-1));}                    
                       if(g[j]=='a') {
                                     printf("y");
                                     }
                                     else if(g[j]=='b') {
                                          printf("h");
                                          }
                                          
                                          else if(g[j]=='c') {
                                          printf("e");
                                          }
                                          
                                          else if(g[j]=='d') {
                                          printf("s");
                                          }
                                          
                                          else if(g[j]=='e') {
                                          printf("o");
                                          }
                                          
                                          else if(g[j]=='f') {
                                          printf("c");
                                          }
                                          else if(g[j]=='g') {
                                          printf("v");
                                          }
                                          else if(g[j]=='h') {
                                          printf("x");
                                          }
                                          else if(g[j]=='i') {
                                          printf("d");
                                          }
                                          else if(g[j]=='j') {
                                          printf("u");
                                          }
                                          else if(g[j]=='k') {
                                          printf("i");
                                          }
                                          else if(g[j]=='l') {
                                          printf("g");
                                          }
                                          else if(g[j]=='m') {
                                          printf("l");
                                          }
                                          else if(g[j]=='n') {
                                          printf("b");
                                          }
                                          else if(g[j]=='o') {
                                          printf("k");
                                          }
                                          else if(g[j]=='p') {
                                          printf("r");
                                          }
                                          else if(g[j]=='q') {
                                          printf("z");
                                          }
                                          else if(g[j]=='r') {
                                          printf("t");
                                          }
                                          else if(g[j]=='s') {
                                          printf("n");
                                          }
                                          else if(g[j]=='t') {
                                          printf("w");
                                          }
                                          else if(g[j]=='u') {
                                          printf("j");
                                          }
                                          else if(g[j]=='v') {
                                          printf("p");
                                          }
                                          else if(g[j]=='w') {
                                          printf("f");
                                          }
                                          else if(g[j]=='x') {
                                          printf("m");
                                          }
                                          else if(g[j]=='y') {
                                          printf("a");
                                          }
                                          else if(g[j]=='z') {
                                          printf("q");
                                          }
                                          
                                          else if(g[j]==' ') {
                                               printf(" ");
                                               }
                      if(j==strlen(g)-1) {printf("\n");}
                      j++; 
                       }
                       
    }
  //  printf("%d",i);
    //getch();
    return 0;
   
    
    }
