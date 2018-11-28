#include<stdio.h>
#include<string.h>
int t;
int T;
char s[102];
int main()
{
   freopen("A-small-attempt3.in.txt", "r", stdin);
   freopen("A-small-attempt3.out", "w", stdout);
    scanf("%d",&t);
    getchar();
    T=1;
    while(t--)
    {
        gets(s);
        printf("Case #%d: ",T++);
        for(int i=0;i<=strlen(s);i++)
        {
            if(s[i]=='a') printf("y");
            else if(s[i]=='b') printf("h");
            else if(s[i]=='c') printf("e");
            else if(s[i]=='d') printf("s");
            else if(s[i]=='e') printf("o");
            else if(s[i]=='f') printf("c");
            else if(s[i]=='g') printf("v");
            else if(s[i]=='h') printf("x");
            else if(s[i]=='i') printf("d");
            else if(s[i]=='j') printf("u");
            else if(s[i]=='k') printf("i");
            else if(s[i]=='l') printf("g");
            else if(s[i]=='m') printf("l");
            else if(s[i]=='n') printf("b");
            else if(s[i]=='o') printf("k");
            else if(s[i]=='p') printf("r");
            else if(s[i]=='q') printf("z");
            else if(s[i]=='r') printf("t");
            else if(s[i]=='s') printf("n");
            else if(s[i]=='t') printf("w");
            else if(s[i]=='u') printf("j");
            else if(s[i]=='v') printf("p");
            else if(s[i]=='w') printf("f");
            else if(s[i]=='x') printf("m");
            else if(s[i]=='y') printf("a");
            else if(s[i]=='z') printf("q");
            else if(s[i]==' ') printf(" ");
            else printf("\n");
        }
    }
    return 0;
}
