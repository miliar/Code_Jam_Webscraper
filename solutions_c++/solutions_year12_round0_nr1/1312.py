#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;
string str;
int T;
int main()
{
    int i,len;
    int cc;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    while(cin >> T)
    {
        cc = 1;
        getline(cin,str);
        while(T--)
        {
            getline(cin,str);

            len = str.length();
            printf("Case #%d: ",cc++);
            for(i = 0; i < len; i++)
            {
                switch(str[i])
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
                    printf("z");
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
                    printf("q");
                    break;
                default:
                    printf("%c",str[i]);
                    break;
                }

            }
            printf("\n");
        }
    }
    return 0;
}
