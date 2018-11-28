#include<stdio.h>
#include<map>
#include<algorithm>
#include<string.h>
#include<iostream>
using namespace std;

int main()
{
        freopen("a.txt","r",stdin);
        freopen("ao.txt","w",stdout);
        int i,j=1,k; char S[1001];
        scanf("%d ",&k);
        while(k--)
        {
            gets(S);
            printf("Case #%d: ",j++);
            for(i=0;S[i];i++)
            {
                if(S[i]=='a') printf("y");
               else if(S[i]=='y') printf("a");
               else if(S[i]=='b') printf("h");
                else if(S[i]=='c') printf("e");
                 else if(S[i]=='d') printf("s");
                  else if(S[i]=='e') printf("o");
                   else if(S[i]=='f') printf("c");
                    else if(S[i]=='g') printf("v");
                     else if(S[i]=='h') printf("x");
                      else if(S[i]=='i') printf("d");
                       else if(S[i]=='j') printf("u");
                        else if(S[i]=='u') printf("j");
                         else if(S[i]=='k') printf("i");
                         else if(S[i]=='l') printf("g");
               else if(S[i]=='m') printf("l");
                else if(S[i]=='n') printf("b");
                 else if(S[i]=='o') printf("k");
                  else if(S[i]=='p') printf("r");
                   else if(S[i]=='q') printf("z");
                    else if(S[i]=='r') printf("t");
                     else if(S[i]=='s') printf("n");
                      else if(S[i]=='t') printf("w");
                       else if(S[i]=='v') printf("p");
                        else if(S[i]=='w') printf("f");
                         else if(S[i]=='x') printf("m");
                         else if(S[i]=='z') printf("q");
                         else printf("%c",S[i]);
            }
            printf("\n");
        }
        return 0;
}
