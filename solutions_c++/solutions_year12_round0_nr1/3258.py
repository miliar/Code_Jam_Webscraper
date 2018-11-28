#include <iostream>
#include <stdio.h>
using namespace std;

char odwz[]={'y',//a
            'h',//b
            'e',//c
            's',//d
            'o',//e
            'c',//f
            'v',//g
            'x',//h
            'd',//i
            'u',//j
            'i',//k
            'g',//l
            'l',//m
            'b',//n
            'k',//o
            'r',//p
            'z',//q
            't',//r
            'n',//s
            'w',//t
            'j',//u
            'p',//v
            'f',//w
            'm',//x
            'a',//y
            'q',//z
            };

void odkoduj(char *we,char *wy)
{
    for(int i =0;i<1000;i++)
    {
        if(we[i]=='\0')
        {
            wy[i]='\0';
            return;
        }
        if(we[i]==' ')
        {
            wy[i]=' ';
        }
        else
        {
            wy[i]=odwz[we[i]-'a'];
        }
    }
}
int main()
{
    char Swyj[1000], Swej[1000];
    int T, N;
    cin >> T;
    getchar();
    for(int t=0;t<T;t++)
    {
        cin.getline(Swej,1000);
        odkoduj(Swej,Swyj);

        cout << "Case #"<<t+1<<": "<< Swyj<<endl;

    }

    return 0;
}
