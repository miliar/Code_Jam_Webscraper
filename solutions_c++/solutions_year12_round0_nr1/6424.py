#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int main()
{
    int test,t=0;
    char ch[110],dmp[2];
    cin>>test;
    gets(dmp);
    while(test--)
    {
        gets(ch);
        printf("Case #%d: ",++t);
        for(int i=0; ch[i]!='\0'; i++)
        {
            if(ch[i]=='a')
                printf("y");
            if(ch[i]=='b')
                printf("h");
            if(ch[i]=='c')
                printf("e");
            if(ch[i]=='d')
                printf("s");
            if(ch[i]=='e')
                printf("o");
            if(ch[i]=='f')
                printf("c");
            if(ch[i]=='g')
                printf("v");
            if(ch[i]=='h')
                printf("x");
            if(ch[i]=='i')
                printf("d");
            if(ch[i]=='j')
                printf("u");
            if(ch[i]=='k')
                printf("i");
            if(ch[i]=='l')
                printf("g");
            if(ch[i]=='m')
                printf("l");
            if(ch[i]=='n')
                printf("b");
            if(ch[i]=='o')
                printf("k");
            if(ch[i]=='p')
                printf("r");
            if(ch[i]=='q')
                printf("z");
            if(ch[i]=='r')
                printf("t");
            if(ch[i]=='s')
                printf("n");
            if(ch[i]=='t')
                printf("w");
            if(ch[i]=='u')
                printf("j");
            if(ch[i]=='v')
                printf("p");
            if(ch[i]=='w')
                printf("f");
            if(ch[i]=='x')
                printf("m");
            if(ch[i]=='y')
                printf("a");
            if(ch[i]=='z')
                printf("q");
            if(ch[i]==' ')
                printf(" ");
        }
        printf("\n");
    }
}

