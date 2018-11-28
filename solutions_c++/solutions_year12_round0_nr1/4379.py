#include <iostream>
#include <string>

using namespace std;

int main()
{
    string st;
    int T,x;
    scanf("%d",&T);
    getline(cin,st);
    x=0;
    while(T--)
    {
        x++;
        getline(cin,st);
        printf("Case #%d: ",x);
        for(int a=0;a<st.length();a++)
        {
            if(st[a]=='a') printf("y");
            if(st[a]=='b') printf("h");
            if(st[a]=='c') printf("e");
            if(st[a]=='d') printf("s");
            if(st[a]=='e') printf("o");
            if(st[a]=='f') printf("c");
            if(st[a]=='g') printf("v");
            if(st[a]=='h') printf("x");
            if(st[a]=='i') printf("d");
            if(st[a]=='j') printf("u");
            if(st[a]=='k') printf("i");
            if(st[a]=='l') printf("g");
            if(st[a]=='m') printf("l");
            if(st[a]=='n') printf("b");
            if(st[a]=='o') printf("k");
            if(st[a]=='p') printf("r");
            if(st[a]=='q') printf("z");
            if(st[a]=='r') printf("t");
            if(st[a]=='s') printf("n");
            if(st[a]=='t') printf("w");
            if(st[a]=='u') printf("j");
            if(st[a]=='v') printf("p");
            if(st[a]=='w') printf("f");
            if(st[a]=='x') printf("m");
            if(st[a]=='y') printf("a");
            if(st[a]=='z') printf("q");
            if(st[a]==' ') printf(" ");
        }
        printf("\n");
    }
    return 0;
}
        
        
