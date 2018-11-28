#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;

int main()
{

    int t,i,j,n;
    char g[200];


    freopen("A-small-attempt1.in","r",stdin);
    scanf("%d ",&t);
    freopen("out.txt","w",stdout);
    for(i=0;i<t;i++)
    {
        gets(g);
        n = strlen(g);

        printf("Case #%d: ",i+1);
        for(j=0;j<n;j++)
        {
                switch(g[j])
                {
                    case 'a':
                        printf("y");
                        break;
                    case 'b':
                        printf("h");
                        break;
                    case 'c':
                        printf("e");
                        break;
                    case 'd':
                        printf("s");
                        break;
                    case 'e':
                        printf("o");
                        break;
                    case 'f':
                        printf("c");
                        break;
                    case 'g':
                        printf("v");
                        break;
                    case 'h':
                        printf("x");
                        break;
                    case 'i':
                        printf("d");
                        break;
                    case 'j':
                        printf("u");
                        break;
                    case 'k':
                        printf("i");
                        break;
                    case 'l':
                        printf("g");
                        break;
                    case 'm':
                        printf("l");
                        break;
                    case 'n':
                        printf("b");
                        break;
                    case 'o':
                        printf("k");
                        break;
                    case 'p':
                        printf("r");
                        break;
                    case 'q':
                        printf("z");         //unknown
                        break;
                    case 'r':
                        printf("t");
                        break;
                    case 's':
                        printf("n");
                        break;
                    case 't':
                        printf("w");
                        break;
                    case 'u':
                        printf("j");
                        break;
                    case 'v':
                        printf("p");
                        break;
                    case 'w':
                        printf("f");
                        break;
                    case 'x':
                        printf("m");
                        break;
                    case 'y':
                        printf("a");
                        break;
                    case 'z':
                        printf("q");         //unknown
                        break;
                    case ' ':
                        printf(" ");
                        break;
                }
        }
        cout<<endl;

    }
}
