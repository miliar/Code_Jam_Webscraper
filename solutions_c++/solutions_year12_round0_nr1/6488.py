#include<iostream>
#include<stdio.h>
#include<cstdio>
#include<sstream>
#include<stdlib.h>
#include<string.h>
using namespace std;
int main()
{
    FILE * pile;
    FILE * ans;
    pile = fopen("A-small-attempt1.in","r");
    ans = fopen("ans.txt","w");
    char inp[110];
    int T, i = 0, j = 0,flag = 0;
    char count[4];
    fgets(count,4,pile);
    T = atoi(count);
    int k = 1;
    while(k<=T)
    {
        char* temp;
        itoa(k,temp,10);
        fgets(inp,110,pile);
        fputs("Case #",ans);
        fputs(temp,ans);
        fputs(": ",ans);
        i = strlen(inp);
        j = 0;
        while(j < i)
        {
            switch(inp[j])
            {
                case 'a':{fputc( (int) 'y',ans);break;}
                case 'b':{fputc( (int) 'h',ans);break;}
                case 'c':{fputc( (int) 'e',ans);break;}
                case 'd':{fputc( (int) 's',ans);break;}
                case 'e':{fputc( (int) 'o',ans);break;}
                case 'f':{fputc( (int) 'c',ans);break;}
                case 'g':{fputc( (int) 'v',ans);break;}
                case 'h':{fputc( (int) 'x',ans);break;}
                case 'i':{fputc( (int) 'd',ans);break;}
                case 'j':{fputc( (int) 'u',ans);break;}
                case 'k':{fputc( (int) 'i',ans);break;}
                case 'l':{fputc( (int) 'g',ans);break;}
                case 'm':{fputc( (int) 'l',ans);break;}
                case 'n':{fputc( (int) 'b',ans);break;}
                case 'o':{fputc( (int) 'k',ans);break;}
                case 'p':{fputc( (int) 'r',ans);break;}
                case 'q':{fputc( (int) 'z',ans);break;}
                case 'r':{fputc( (int) 't',ans);break;}
                case 's':{fputc( (int) 'n',ans);break;}
                case 't':{fputc( (int) 'w',ans);break;}
                case 'u':{fputc( (int) 'j',ans);break;}
                case 'v':{fputc( (int) 'p',ans);break;}
                case 'w':{fputc( (int) 'f',ans);break;}
                case 'x':{fputc( (int) 'm',ans);break;}
                case 'y':{fputc( (int) 'a',ans);break;}
                case 'z':{fputc( (int) 'q',ans);break;}
                default: fputc( (int) ' ',ans);
            };
            j++;
        }
        fputc( (int) '\n',ans);
        k++;

    }

}
